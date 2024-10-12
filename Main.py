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

# Processing Raw Data to Frequency Table
data.Populate()

# Adding Percent Symbol into The Relative Frequency Coloumn
relative_frequency_with_percentage = [
    f"{rf * 1:.2f}%" for rf in data.final.relative_frequency
]

# Transform The Data To A Frequency Table
# Initiating The Data Using Pandas
df = pd.DataFrame(
    {
        "Class Interval" : data.final.ranges,
        "Class Limit" : data.final.limit,
        "Frequency" : data.final.frequency,
        "Midpoint" : data.final.midpoint,
        
        "C <" : data.final.bottom_limit,
        "CF <" : data.final.bottom_cumulative_frequency,
        "C >" : data.final.top_cumulative_frequency,
        "CF >" : data.final.top_cumulative_frequency,
        "Relative Frequency" : relative_frequency_with_percentage
    }
)

# Converting Pandas Data Into Tabulate
table = tabulate.tabulate(
    df,
    headers='keys',
    tablefmt='pipe'
) 

# print(table)
print(data.final.ranges)

