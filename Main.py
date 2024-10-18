# EXAMPLE PROGRAM
import FrequencyTable as ft
import tabulate as tabulate
import Transform as tf
import pandas as pd
 
# Raw Data
dataset = [
    12.5, 12.5, 12.1, 12.6, 12.7, 12.5, 43.2, 43.2, 43.2, 43.5,
    34.2, 34.1, 34.3, 34.2, 34.0, 34.5, 56.7, 56.8, 56.5, 56.6,
    56.9, 57.0, 67.9, 67.8, 67.5, 67.6, 67.7, 78.4, 78.1, 78.3,
    78.2, 78.9, 78.8, 89.0, 89.1, 89.2, 90.5, 91.2, 90.3, 90.0,
    98.3, 98.1, 98.0, 99.5, 99.4, 99.6, 99.1, 99.2, 99.3, 99.0,
    22.4, 22.3, 22.5, 22.2, 22.1, 22.0, 25.4, 25.5, 25.6, 25.0,
    32.4, 32.5, 32.3, 32.2, 32.1, 32.0, 45.6, 45.5, 45.4, 45.0,
    56.3, 56.4, 56.2, 56.1, 56.0, 60.5, 64.0, 64.1, 64.2, 64.3,
    71.3, 71.4, 71.5, 71.6, 71.7, 71.8, 84.2, 84.3, 84.1, 84.0,
    12.9, 12.8, 12.7, 12.6, 12.5, 12.4
]


# Initiate Object From The Raw Data
data = ft.FrequencyTable(dataset)
data.populate_simple() # Simple Data

# Simple Populated Data
dfs = pd.DataFrame(
    {
        "Class" : data.simple.classval,
        "Frequency" : data.simple.frequency,
        "Relative Frequency" : data.simple.percentage_relative_frequency
    }
)

# Converting Pandas Data Into Tabulate
tablesimple = tabulate.tabulate(
    dfs,
    headers='keys',
    tablefmt='pipe'
) 

# Print The Processed Data
print(tablesimple)
print(data.simple.mode)
print(data.mean)
print(data.median)


data.populate_grouped() # Grouped Data
dfg = pd.DataFrame(
    {
        "Class Interval" : data.grouped.ranges,
        "Class Limit" : data.grouped.limit,
        "Frequency" : data.grouped.frequency,
        "Midpoint" : data.grouped.midpoint,
        
        "C <" : data.grouped.bottom_limit,
        "CF <" : data.grouped.bottom_cumulative_frequency,
        "C >" : data.grouped.top_limit,
        "CF >" : data.grouped.top_cumulative_frequency,
        "Relative Frequency" : data.grouped.percentage_relative_frequency
    }
)

tablegrouped = tabulate.tabulate(
    dfg,
    headers='keys',
    tablefmt='pipe',
)
print(tablegrouped)
print(data.grouped.mode)
print(data.mean)


