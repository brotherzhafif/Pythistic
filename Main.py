# EXAMPLE PROGRAM
import FrequencyTable as ft
 
# Raw Data
data = (
  58, 67, 45, 89, 72, 60, 76, 93, 
  55, 48, 62, 85, 79, 56, 41, 90, 
  77, 54, 68, 82, 46, 73, 57, 92, 
  81, 53, 66, 74, 64, 52, 91, 78, 
  49, 87, 88, 50, 69, 84, 43, 65, 
  83, 70, 44, 61, 75, 80, 71, 63, 47,51)

# Initiate Object From The Raw Data
table = ft.FrequencyTable(data)

# Processing Raw Data to Frequency Table
table.Populate()

# Print The Data
print(table.data.ranges) 
print(table.data.frequency)
