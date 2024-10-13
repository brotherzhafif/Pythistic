# EXAMPLE PROGRAM
import FrequencyTable as ft
import pandas as pd
import tabulate as tabulate
 
# Raw Data
dataset = (
           "Apel", "Pisang", "Jeruk", "Mangga", "Semangka", 
    "Melon", "Pepaya", "Nanas", "Anggur", "Stroberi",
    "Durian", "Salak", "Rambutan", "Sirsak", "Alpukat",
    "Jambu Biji", "Pir", "Kelengkeng", "Markisa", "Leci",
    "Ceri", "Blueberry", "Raspberry", "Kedondong", "Belimbing",
    "Duku", "Manggis", "Kismis", "Kelengkeng", "Cempedak",
    "Srikaya", "Delima", "Kiwi", "Plum", "Kurma", 
    "Aprikot", "Persik", "Buah Naga", "Nangka", "Pepino"
)

# Initiate Object From The Raw Data
data = ft.FrequencyTable(dataset)

# Processing Raw Data to Frequency Grouped Frequency Table
data.PopulateGrouped() # Grouped Data
data.PopulateSimple() # Simple Data
data.PopulateString() # String Data

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

# # Simple Populated Data
dfs = pd.DataFrame(
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

# Simple Populated Data
dfa = pd.DataFrame(
    {
        "Class" : data.text.classval,
        "Frequency" : data.text.frequency,
        
        "C <" : data.text.bottom_limit,
        "CF <" : data.text.bottom_cumulative_frequency,
        "C >" : data.text.top_limit,
        "CF >" : data.text.top_cumulative_frequency,
        "Relative Frequency" : data.text.percentage_relative_frequency
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

tablestring = tabulate.tabulate(
    dfa,
    headers='keys',
    tablefmt='pipe',
)

# Print The Processed Data
print(tablesimple)
print(tablegrouped)
print(tablestring)



