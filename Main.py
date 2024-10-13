# EXAMPLE PROGRAM
import FrequencyTable as ft
import pandas as pd
import tabulate as tabulate
 
# Raw Data
dataset = [1.2, 2.5, 3.1, 4.7, 1.2, 2.5, 3.8, 4.5, 2.1, 3.3, 4.8, 5.0]


# Initiate Object From The Raw Data
data = ft.FrequencyTable(dataset)

# Processing Raw Data to Frequency Grouped Frequency Table
# data.PopulateGrouped() # Grouped Data
data.PopulateSimple() # Simple Data

# Transform The Data To A Frequency Table
# Initiating The Data Using Pandas
# Grouped Populated Data
# dfg = pd.DataFrame(
#     {
#         "Class Interval" : data.grouped.ranges,
#         "Class Limit" : data.grouped.limit,
#         "Frequency" : data.grouped.frequency,
#         "Midpoint" : data.grouped.midpoint,
        
#         "C <" : data.grouped.bottom_limit,
#         "CF <" : data.grouped.bottom_cumulative_frequency,
#         "C >" : data.grouped.top_limit,
#         "CF >" : data.grouped.top_cumulative_frequency,
#         "Relative Frequency" : data.grouped.percentage_relative_frequency
#     }
# )

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

# tablegrouped = tabulate.tabulate(
#     dfg,
#     headers='keys',
#     tablefmt='pipe',
# )

# Print The Processed Data
print(tablesimple)
# print(tablegrouped)



