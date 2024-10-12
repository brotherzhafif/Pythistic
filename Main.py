# EXAMPLE PROGRAM
import FrequencyTable as ft
import pandas as pd
import tabulate as tabulate
 
# Raw Data
dataset = (
  58, 67, 45, 89, 72, 60, 76, 93, 
  55, 48, 62, 85, 79, 56, 41, 90, 
  77, 54, 68, 82, 46, 73, 57, 92, 
  81, 53, 66, 74, 64, 52, 91, 78, 
  49, 87, 88, 50, 69, 84, 43, 65, 
  83, 70, 44, 61, 75, 80, 71, 63, 47,51)

# Initiate Object From The Raw Data
data = ft.FrequencyTable(dataset)

# Processing Raw Data to Frequency Grouped Frequency Table
data.PopulateGrouped()

# Transform The Data To A Frequency Table
# Initiating The Data Using Pandas
df = pd.DataFrame(
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

# Converting Pandas Data Into Tabulate
table = tabulate.tabulate(
    df,
    headers='keys',
    tablefmt='pipe'
) 

# Print Output Data
print(table)

