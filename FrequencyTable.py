import numpy as np

# Frequency Table Class 
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

    # Populate Data Method
    def Populate(self):
    # Initiating Used List
        top = []
        bottom = []
        top_limit = []
        bottom_limit = []

        frequency = []
        data_range = []
        data_limit = []
        data_midpoint = []

        bot_cumulative_frequency = []
        top_cumulative_frequency = []
        relative_frequency = []

        # Initiating Used Parameter
        interval = self.interval # 4
        current_number = self.base - 1 # 156
        old_number = 0

        while current_number <= self.top-3:
            # Finding Class Lowest Value
            old_number = current_number + 1
            bottom.append(old_number) # 155
            
            # Finding Class Highest Value 
            current_number = current_number + interval
            top.append(current_number)
            
            # Append Class Bottom Limit
            current_bot_limit = old_number - 0.5
            bottom_limit.append(current_bot_limit)

            # Append Class Top Limit
            current_top_limit = current_number + 0.5
            top_limit.append(current_top_limit)

            # Finding The Frequency That Range
            current_frequency = self.find_frequency(old_number, current_number)
            frequency.append(current_frequency)

            # Adding The Number Range From Both Frequency
            current_data_range = f"{old_number} ~ {current_number}"
            data_range.append(current_data_range)

            # Adding Data Range Limit Of The Class Frequency
            current_data_limit = f"{current_bot_limit} ~ {current_top_limit}"
            data_limit.append(current_data_limit)   

            # Adding Data Midpoint of The Class Frequency
            current_data_midpoint = (old_number + current_number) / 2
            data_midpoint.append(current_data_midpoint)

            # Adding Bottom Cumulative Frequency of The Class 
            current_bot_cumulative_frequency = self.find_frequency(self.lowest, old_number)
            bot_cumulative_frequency.append(current_bot_cumulative_frequency)

            # Adding Bottom Cumulative Frequency of The Class 
            current_top_cumulative_frequency = self.find_frequency(old_number, self.highest)
            top_cumulative_frequency.append(current_top_cumulative_frequency)
        
            # Counting the Relative Frequency in Percentage
            current_relative_frequency = np.round((current_frequency / self.amount) * 100)
            relative_frequency.append(current_relative_frequency)
            

        # Append Processed Data into Data Attributes
        self.final = ProcessedData(bottom, top, bottom_limit, top_limit, frequency, data_range, data_limit, data_midpoint, bot_cumulative_frequency, top_cumulative_frequency, relative_frequency)

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
    
# Processed Data Assignment 
class ProcessedData:
    # Limit (L), Frequency (F), Ranges (R), Midpoint (M), Cumulative (C), Relative (R) 
    def __init__(self, bot, top, bot_L, top_L, F, R, L, M, bot_CF, top_CF, RF):
        self.bottom = bot
        self.top = top
        self.bottom_limit = bot_L
        self.top_limit = top_L
        self.midpoint = M
        self.ranges = R      
        self.limit = L     

        self.frequency = F
        self.bottom_cumulative_frequency = bot_CF
        self.top_cumulative_frequency = top_CF
        self.relative_frequency = RF
 
