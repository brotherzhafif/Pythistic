# EXAMPLE PROGRAM
import FrequencyTable as ft
import pandas as pd
import tabulate as tabulate
 
# Raw Data
dataset = [
    'Mango', 'Pineapple', 'Banana', 'Banana', 'Pineapple', 'Banana', 
    'Banana', 'Grapes', 'Pear', 'Pineapple', 'Orange', 'Strawberry', 
    'Orange', 'Mango', 'Banana', 'Pineapple', 'Orange', 'Banana', 
    'Strawberry', 'Pear', 'Apple', 'Banana', 'Pineapple', 'Orange', 
    'Mango', 'Apple', 'Pear', 'Pear', 'Pear', 'Grapes', 'Pear', 
    'Orange', 'Grapes', 'Strawberry', 'Mango', 'Orange', 'Orange', 
    'Mango', 'Pear', 'Strawberry', 'Pear', 'Orange', 'Mango', 
    'Mango', 'Pear', 'Grapes', 'Apple', 'Mango', 'Pineapple', 
    'Strawberry', 'Strawberry', 'Grapes', 'Apple', 'Banana', 
    'Grapes', 'Banana', 'Strawberry', 'Mango', 'Strawberry', 
    'Orange', 'Pear', 'Grapes', 'Orange', 'Apple'
]

# Initiate Object From The Raw Data
data = ft.FrequencyTable(dataset)

# Processing Raw Data to Frequency Grouped Frequency Table
data.PopulateGrouped() # Grouped Data
data.PopulateSimple() # Simple Data

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

tablegrouped = tabulate.tabulate(
    dfg,
    headers='keys',
    tablefmt='pipe',
)

# Print The Processed Data
print(tablesimple)
print(tablegrouped)



