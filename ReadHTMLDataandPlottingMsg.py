'''
The goal is to read a set of x, y coordinates and
draw a scatter plot with the corresponding values. 

The input file is an HTML.
'''

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Location of the data
target_url = "NA"

# Read HTML data: to see how table1 looks, check the png image HTMLtable1.png
table1 = pd.read_html(target_url)
print("table1 = ", table1) 

'''
1. This print statement shows there is an extra header row
    which is not necessary and hiding the actual header. So, 
    I am adding the heading parameter.
2. Also, all the values in the 'Character' column is showing 
    as a-cap, which cannot be the case. I know this because 
    I saw the data file. Hence, including an encoding value.
'''

# To see how table2 looks, check the png image HTMLtable2.png
table2 = pd.read_html(target_url, header = 0, encoding = 'utf-8')
print("table2 = ", table2)
print(type(table2))

'''
This is a 3D list with dimension [1x331x3]
Hence it is important to convert this to a 2D one
before creating a pandas DataFrame.

First, I am converting this to a numpy array and
reshaping it before creating the dataframe. Because 
numpy array does not have header, I am saving the 
header from table2 to use later.
'''
# Save table2 header
df = table2[0]
headers = df.columns.to_list()
print(headers)

# Convert 3D -> 2D
data_3d = np.array(table2)
data_2d_numpy = data_3d.reshape(-1, data_3d.shape[2])

# Create DataFrame: to see how data looks, check the png image HTMLdata.png
data = pd.DataFrame(data_2d_numpy, columns=headers)
print("data = ", data)


'''
The dataframe has string values in all columns. 
Converting the coordinate columns to numeric.
'''

# Convert to integer and calculate the maximum range
data['x-coordinate'] = pd.to_numeric(data['x-coordinate'])
data['y-coordinate'] = pd.to_numeric(data['y-coordinate'])
x_range, y_range = max(data['x-coordinate']), max(data['y-coordinate'])

'''
Because scatter plot does not accept unicode symbols as markers,
I am plotting 'texts' instead of markers.
'''

# Plotting: to see how the figure looks, check the png image HTMLmsgPlot.png
fig, ax = plt.subplots()
for _, row in data.iterrows():
    ax.text(row[0], row[2], row[1], ha='center', va= 'center')
ax.set_xlim(0, x_range)
ax.set_ylim(0, y_range)
ax.set_aspect('equal')
ax.set_title('*** Data to message ***')

plt.show()

