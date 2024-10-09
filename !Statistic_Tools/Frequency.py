import math
import Dataset

# Data Initiation
dataset = sorted(Dataset.data)
amount = len(dataset)
lowest = min(dataset)
highest = max(dataset)

# Counting Data Range
ranges = highest - lowest # Rangenya 25
# print("Ranges = " + str(ranges))

# Classes is Rounding Down
# Math Log Base 10 In Python For Accurate Result
classes = 1 + (3.222 * math.log(amount, 10))
classes = round(classes - 0.5)
# print("Kelas = " + str(classes))

# Interval is Rounding Up
interval = ranges / classes 
interval = round(interval + 0.5)
# print("Interval = " + str(interval))

# Function To Find Frequency in Dataset with Desired Range (Top and Down Limit)
def find_frequency(bot, top):
  total_frequency = 0
  for i in range(bot, top + 1):
      frequency = dataset.count(i)
      total_frequency = total_frequency + frequency
  return total_frequency

# Base 5 Rounding
def roundy(x, base=5):
    return base * round(x/base)

# Rounding Both Limit So The Data Would Be Simple And Easier To Read
base = roundy(lowest - 3)
top = roundy(highest + 3)

# Populate List For Base and Top Range Limit and The Frequency
def populate_frequency(base, top, interval):
  # Initiating Used List
  lower = []
  upper = []
  frequency = []
  data_range = []

  # Initiating Used Parameter
  interval = interval # 4
  current_number = base - 1 # 156
  old_number = 0

  while current_number < top:
    # Finding Botom Limit Data
    old_number = current_number + 1
    lower.append(old_number) # 155
    
    # Finding Top Limit Data
    current_number = current_number + interval
    upper.append(current_number)
    
    # Finding The Frequency That Range
    range_frequency = find_frequency(old_number, current_number)
    frequency.append(range_frequency)

    # Adding The Number Range From Both Frequency
    data_range.append(str(old_number) + " ~ " + str(current_number))
  
  return lower, upper, frequency,data_range

data_lower, data_upper, data_frequency, data_range = populate_frequency(base, top, interval)
