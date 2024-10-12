# EXAMPLE PROGRAM
import FrequencyTable as ft
import pandas as pd
import tabulate as tabulate
 
# Raw Data
dataset = (1,1,1,4,6,7,3,6,7,1,2,2,5,3,1,8,3,2)

# Initiate Object From The Raw Data
data = ft.FrequencyTable(dataset)

# Processing Raw Data to Frequency Grouped Frequency Table
data.PopulateSimple()

# Transform The Data To A Frequency Table
# Initiating The Data Using Pandas
# df = pd.DataFrame(
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

df = pd.DataFrame(
    {
        "Class" : data.simple.classval,
        "Frequency" : data.simple.frequency,
        
        "C <" : data.simple.bottom_limit,
        "CF <" : data.simple.bottom_cumulative_frequency,
        "C >" : data.simple.top_limit,
        "CF >" : data.simple.top_cumulative_frequency,
        "Relative Frequency" : data.simple.percentage_relative_frequency
    }
)


# Converting Pandas Data Into Tabulate
table = tabulate.tabulate(
    df,
    headers='keys',
    tablefmt='pipe'
) 

# Print Output Data
print(table)


