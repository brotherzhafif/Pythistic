import numpy as np

# Global Variable Used in Frequency Table Data Processing
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
mode = []

# Frequency Table Class 
class FrequencyTable:
    def __init__(self, dataset):
        # Check for mixed data types (both numeric and string)
        if any(isinstance(item, str) for item in dataset) and any(isinstance(item, (int, float)) for item in dataset):
            raise ValueError("Data is corrupted: contains both numeric and string values.")

        # Data Initiation
        self.dataset = sorted(dataset)
        self.length = len(dataset)
        self.lowest = min(dataset) if isinstance(dataset[0], (int, float)) else None
        self.highest = max(dataset) if isinstance(dataset[0], (int, float)) else None

        if self.lowest is not None:  # Only calculate classes for numeric data
            # Classes is Rounding Down
            self.classes = 1 + (3.222 * np.log10(self.length))
            self.classes = round(self.classes - 0.5)

            # Sum of the data and range
            self.sum = sum(dataset)
            self.range = self.highest - self.lowest

            # Interval is Rounding Up
            self.interval = self.range / self.classes 
            self.interval = round(self.interval + 0.5)

            # Rounding Both Limits So The Data Would Be Simple And Easier To Read
            self.base = self.roundy(self.lowest - 3)
            self.top = self.roundy(self.highest + 3)

            # Mean or Average
            self.mean = (self.sum / self.length)

            # Formula for Variance
            self.variance = sum((x - self.mean) ** 2 for x in dataset) / self.length

            # Formula for Standard Deviation
            self.deviation = (self.variance ** 0.5)

            # Formula to find Dataset Skewness
            self.skewness = (self.length / ((self.length - 1) * (self.length - 2))) * \
                            sum(((x - self.mean) / self.deviation) ** 3 for x in self.dataset)

            # Formula to find Dataset Kurtosis
            self.kurtosis = (self.length * (self.length + 1) * sum(((x - self.mean) / self.deviation) ** 4 for x in self.dataset) / 
                            ((self.length - 1) * (self.length - 2) * (self.length - 3))) - \
                            (3 * (self.length - 1) ** 2) / ((self.length - 2) * (self.length - 3))

    # Base 5 Rounding
    def roundy(self, x, base=5):
        return base * round(x / base)

    # Function to Reset Frequency Table Data
    def reset(self):
        global top, bottom, top_limit, bottom_limit, frequency
        global data_range, data_limit, data_midpoint
        global bot_cumulative_frequency, top_cumulative_frequency, relative_frequency, mode
        
        top.clear()
        bottom.clear()
        top_limit.clear()
        bottom_limit.clear()
        frequency.clear()
        data_range.clear()
        data_limit.clear()
        data_midpoint.clear()
        bot_cumulative_frequency.clear()
        top_cumulative_frequency.clear()
        relative_frequency.clear()
        mode.clear()

    # Function To Find Frequency in Dataset with Desired Range (Top and Down Limit)
    def find_frequency(self, bot, top):
        total_frequency = 0
        # Check if the dataset contains only integers
        is_integer_data = all(isinstance(x, int) for x in self.dataset)

        if is_integer_data:
            # Loop for integers
            for i in range(bot, top):
                frequency = self.dataset.count(i)
                total_frequency += frequency
        else:
            # Loop for decimals
            current = bot
            while current < top:
                frequency = self.dataset.count(round(current, 2))  # Round for matching
                total_frequency += frequency
                current += 0.01  # Increment by 0.01 for decimals

        return total_frequency    

    # Populate Grouped Table Frequency Data Method
    def PopulateGrouped(self):
        try:
            # Check if the dataset contains text
            if any(isinstance(item, str) for item in self.dataset):
                raise ValueError("Text data is not allowed for grouped frequency tables. Please provide numeric data only.")

            self.reset()  # Reset the frequency table data before processing

            # Initiating Used Parameter for Frequency Table
            old_number = 0
            interval = self.interval
            current_number = self.base - 1
            current_top_cumulative_frequency = 1

            # Processing the Frequency Table Data
            while current_top_cumulative_frequency != 0:
                # Finding Class Lowest Value
                old_number = current_number + 1
                bottom.append(old_number)
                
                # Finding Class Highest Value 
                current_number = current_number + interval
                top.append(current_number)
                
                # Append Class Bottom Limit
                current_bottom_limit = old_number - 0.5
                bottom_limit.append(current_bottom_limit)

                # Append Class Top Limit
                current_top_limit = current_number + 0.5
                top_limit.append(current_top_limit)

                # Finding The Frequency That Range
                current_frequency = self.find_frequency(old_number, current_number + 1)
                frequency.append(current_frequency)

                # Adding The Number Range From Both Frequency
                current_data_range = f"{old_number:.2f} ~ {current_number:.2f}" if not all(isinstance(x, int) for x in self.dataset) else f"{old_number} ~ {current_number}"
                data_range.append(current_data_range)

                # Adding Data Range Limit Of The Class Frequency
                current_data_limit = f"{current_bottom_limit:.2f} ~ {current_top_limit:.2f}" if not all(isinstance(x, int) for x in self.dataset) else f"{current_bottom_limit} ~ {current_top_limit}"
                data_limit.append(current_data_limit)   

                # Adding Data Midpoint of The Class Frequency
                current_data_midpoint = (old_number + current_number) / 2
                data_midpoint.append(current_data_midpoint)

                # Adding Bottom Cumulative Frequency of The Class 
                current_bot_cumulative_frequency = self.find_frequency(self.lowest - 1, old_number)
                bot_cumulative_frequency.append(current_bot_cumulative_frequency)

                # Adding Top Cumulative Frequency of The Class 
                current_top_cumulative_frequency = self.find_frequency(current_number + 1, self.highest + 1)
                top_cumulative_frequency.append(current_top_cumulative_frequency)
            
                # Counting the Relative Frequency in Percentage
                current_relative_frequency = np.round((current_frequency / self.length) * 100)
                relative_frequency.append(current_relative_frequency)    

            # Find Mode or Data that appears most frequently 
            mode_index = [i for i, val in enumerate(frequency) if val == max(frequency)]
            mode = [data_range[i] for i in mode_index]
            
            # Append Processed Data into Data Attributes
            self.grouped = ProcessedData(None, bottom, top, bottom_limit, top_limit, 
                                         frequency, data_range, data_limit, data_midpoint, 
                                         bot_cumulative_frequency, top_cumulative_frequency, 
                                         relative_frequency, mode)

        except ValueError as e:
            print(f"Error: {e}")

    # Populate Simple Table Frequency Data Method    
    def PopulateSimple(self):
        self.reset()  # Reset the frequency table data before processing

        # Initialize general variables
        data = sorted(set(self.dataset))  # Remove duplicates and sort the data
        
        # Initialize limits for numeric data
        top_limit = []
        bottom_limit = []

        # Single loop to process both numeric and string data
        for current_class in data:
            # Calculate the frequency of the current class
            current_frequency = self.dataset.count(current_class)
            frequency.append(current_frequency)

            # Calculate the relative frequency for the current class
            current_relative_frequency = np.round((current_frequency / self.length) * 100)
            relative_frequency.append(current_relative_frequency)

            # If the data is numeric, calculate limits and cumulative frequencies
            if not all(isinstance(item, str) for item in self.dataset):
                # Calculate top and bottom limits for numeric data
                current_top_limit = current_class + 0.5
                current_bottom_limit = current_class - 0.5
                top_limit.append(current_top_limit)
                bottom_limit.append(current_bottom_limit)

                # Calculate bottom cumulative frequency for numeric data
                current_bot_cumulative_frequency = self.find_frequency(self.lowest - 1, current_class)
                bot_cumulative_frequency.append(current_bot_cumulative_frequency)

                # Calculate top cumulative frequency for numeric data
                current_top_cumulative_frequency = self.find_frequency(current_class + 1, self.highest + 1)
                top_cumulative_frequency.append(current_top_cumulative_frequency)

            else:
                # If the data is string-based, calculate cumulative frequencies
                # Calculate bottom cumulative frequency for strings
                current_bot_cumulative_frequency = self.dataset.count(current_class)
                bot_cumulative_frequency.append(current_bot_cumulative_frequency)

                # Calculate top cumulative frequency for strings
                current_top_cumulative_frequency = sum(frequency) - current_bot_cumulative_frequency
                top_cumulative_frequency.append(current_top_cumulative_frequency)

        # Find the mode (the class with the highest frequency)
        mode_index = [i for i, val in enumerate(frequency) if val == max(frequency)]
        mode = [data[i] for i in mode_index]

        # Create the ProcessedData object based on the data type
        self.simple = ProcessedData(
            data, None, None, bottom_limit, top_limit, 
            frequency, None, None, None, 
            bot_cumulative_frequency, top_cumulative_frequency, 
            relative_frequency, mode
        )

# Processed Data Assignment 
class ProcessedData:
    # Limit (L), Frequency (F), Ranges (R), Midpoint (M), Cumulative (C), Relative (R) 
    def __init__(self, data, bot, top, bot_L, top_L, F, R, L, M, bot_CF, top_CF, RF, mode):
        self.classval = data
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
        self.percentage_relative_frequency = [f"{rf * 1:.2f}%" for rf in self.relative_frequency]
        self.mode = mode
