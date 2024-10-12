import numpy as np

class FrequencyTable:
    def __init__(self, dataset):
        # Data Initiation
        self.dataset = sorted(dataset)
        self.amount = len(dataset)
        self.lowest = min(dataset)
        self.highest = max(dataset)

        # Counting Data Range
        self.range = self.highest - self.lowest 

        # Classes is Rounding Down
        # Math Log Base 10 In Python For Accurate Result
        self.classes = 1 + (3.222 * np.log10(self.amount))
        self.classes = round(self.classes - 0.5)

        # Interval is Rounding Up
        self.interval = self.range / self.classes 
        self.interval = round(self.interval + 0.5)

        # Rounding Both Limit So The Data Would Be Simple And Easier To Read
        self.base = self.roundy(self.lowest - 3)
        self.top = self.roundy(self.highest + 3)

    def Populate(self):
    # Initiating Used List
        lower = []
        upper = []
        frequency = []
        data_range = []
        data_limit = []
        data_midpoint = []

        # Initiating Used Parameter
        interval = self.interval # 4
        current_number = self.base - 1 # 156
        old_number = 0

        while current_number <= self.top-3:
            # Finding Botom Limit Data
            old_number = current_number + 1
            lower.append(old_number) # 155
            
            # Finding Top Limit Data
            current_number = current_number + interval
            upper.append(current_number)
            
            # Finding The Frequency That Range
            range_frequency = self.find_frequency(old_number, current_number)
            frequency.append(range_frequency)

            # Adding The Number Range From Both Frequency
            data_range.append(str(old_number) + " ~ " + str(current_number))

            # Adding Data Range Limit Of The Class Frequency
            data_limit.append(str(old_number - 0.5) + " ~ " + str(current_number + 0.5))   

        # Assign Value Each Processed Data
        self.bottom_limit = lower
        self.top_limit = upper
        self.frequency = frequency
        self.ranges = data_range
        self.limit = data_limit
        
        # Append Processed Data into Data Attributes
        self.data = ProcessedData(self.bottom_limit, self.top_limit, self.frequency, self.ranges, self.limit)

    # Base 5 Rounding
    def roundy(self, x, base = 5):
        return base * round(x/base)
    
    # Function To Find Frequency in Dataset with Desired Range (Top and Down Limit)
    def find_frequency(self, bot, top):
        total_frequency = 0
        for i in range(bot, top + 1):
            frequency = self.dataset.count(i)
            total_frequency = total_frequency + frequency
        return total_frequency
    
class ProcessedData:
    def __init__(self, bottoms, tops, frequency, ranges, limit):
        self.bottom = bottoms
        self.top = tops
        self.frequency = frequency  # frekuensi terproses
        self.ranges = ranges         # rentang terproses
        self.limit = limit          # batas kelas terproses

