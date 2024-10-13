# EXAMPLE PROGRAM
import FrequencyTable as ft
import pandas as pd
import tabulate as tabulate
 
# Raw Data
dataset = [12.5, 43.2, 56.7, 12.1, 98.3, 34.2, 78.4, 67.9, 23.5, 45.6,
    78.1, 89.0, 32.4, 56.8, 44.5, 77.2, 12.6, 35.8, 67.1, 23.3,
    56.5, 78.9, 99.5, 22.4, 10.2, 35.1, 48.6, 59.9, 71.3, 84.2,
    45.3, 67.8, 89.1, 33.3, 76.4, 88.7, 41.2, 12.7, 34.4, 67.4,
    23.8, 55.1, 77.3, 90.4, 13.5, 14.6, 55.7, 22.2, 33.1, 66.5,
    78.2, 39.5, 41.8, 91.2, 12.4, 64.7, 49.9, 80.5, 92.3, 38.8,
    14.5, 99.1, 25.4, 26.8, 37.5, 52.3, 43.8, 76.8, 28.7, 64.8,
    14.9, 15.3, 48.5, 82.2, 93.4, 56.3, 88.3, 60.5, 72.9, 38.3,
    57.2, 70.1, 84.4, 97.2, 18.6, 45.1, 66.1, 31.9, 94.5, 29.4,
    11.9, 16.7, 21.1, 88.9, 99.7, 53.6, 62.0, 34.9, 82.8, 18.9,]


# Initiate Object From The Raw Data
data = ft.FrequencyTable(dataset)

# Processing Raw Data to Frequency Grouped Frequency Table
data.PopulateGrouped() # Grouped Data
# data.PopulateSimple() # Simple Data

# Transform The Data To A Frequency Table
# Initiating The Data Using Pandas
# Grouped Populated Data
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

# Simple Populated Data
# dfs = pd.DataFrame(
#     {
#         "Class" : data.simple.classval,
#         "Frequency" : data.simple.frequency,
#         "Relative Frequency" : data.simple.percentage_relative_frequency
#     }
# )

# Converting Pandas Data Into Tabulate
# tablesimple = tabulate.tabulate(
#     dfs,
#     headers='keys',
#     tablefmt='pipe'
# ) 

tablegrouped = tabulate.tabulate(
    dfg,
    headers='keys',
    tablefmt='pipe',
)

# Print The Processed Data
# print(tablesimple)
print(tablegrouped)
print(data.length)

