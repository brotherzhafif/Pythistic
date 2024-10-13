import numpy as np

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

        # Classes is Rounding Down
        if self.lowest is not None:  # Only calculate classes for numeric data
            self.classes = 1 + (3.222 * np.log10(self.length))
            self.classes = round(self.classes - 0.5)

            # Sum of the data and range
            self.sum = sum(dataset)
            self.range = self.highest - self.lowest

            # Interval is Rounding Up
            self.interval = self.range / self.classes 
            self.interval = round(self.interval + 0.5, 2)  # Keep two decimal places

            # Rounding Both Limits
            self.base = self.roundy(self.lowest - 0.5)
            self.top = self.roundy(self.highest + 0.5)

            # Mean or Average
            self.mean = (self.sum / self.length)

            # Variance and Standard Deviation
            self.variance = sum((x - self.mean) ** 2 for x in dataset) / self.length
            self.deviation = (self.variance ** 0.5)

            # Skewness
            self.skewness = (self.length / ((self.length - 1) * (self.length - 2))) * \
                            sum(((x - self.mean) / self.deviation) ** 3 for x in self.dataset)

            # Kurtosis
            self.kurtosis = (self.length * (self.length + 1) * sum(((x - self.mean) / self.deviation) ** 4 for x in self.dataset) / 
                            ((self.length - 1) * (self.length - 2) * (self.length - 3))) - \
                            (3 * (self.length - 1) ** 2) / ((self.length - 2) * (self.length - 3))

    # Base Rounding
    def roundy(self, x, base=0.5):
        return base * round(x / base)

    # Function To Find Frequency in Dataset with Desired Range
    def find_frequency(self, bot, top):
        total_frequency = sum(1 for x in self.dataset if bot < x <= top)
        return total_frequency

    # Populate Grouped Frequency Table Data Method
    def PopulateGrouped(self):
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
        mode = []

        # Frequency Table Initialization
        interval = self.interval
        current_number = self.base - 0.5
        old_number = 0

        # Processing the Frequency Table Data
        while current_number <= self.top:
            # Finding Class Lowest Value
            old_number = current_number + 0.5
            bottom.append(old_number) 
            
            # Finding Class Highest Value 
            current_number = current_number + interval
            top.append(current_number)
            
            # Class Limits
            current_bottom_limit = old_number - 0.5
            bottom_limit.append(current_bottom_limit)
            current_top_limit = current_number + 0.5
            top_limit.append(current_top_limit)

            # Frequency Calculation
            current_frequency = self.find_frequency(old_number, current_number)
            frequency.append(current_frequency)

            # Data Range and Limits
            current_data_range = f"{old_number:.2f} ~ {current_number:.2f}"
            data_range.append(current_data_range)
            current_data_limit = f"{current_bottom_limit:.2f} ~ {current_top_limit:.2f}"
            data_limit.append(current_data_limit)   

            # Midpoint Calculation
            current_data_midpoint = (old_number + current_number) / 2
            data_midpoint.append(current_data_midpoint)

            # Cumulative Frequencies
            current_bot_cumulative_frequency = self.find_frequency(self.lowest - 0.5, old_number)
            bot_cumulative_frequency.append(current_bot_cumulative_frequency)
            current_top_cumulative_frequency = self.find_frequency(current_number, self.highest + 0.5)
            top_cumulative_frequency.append(current_top_cumulative_frequency)

            # Relative Frequency Calculation
            current_relative_frequency = np.round((current_frequency / self.length) * 100, 2)
            relative_frequency.append(current_relative_frequency)    
        
        # Find Mode
        mode_index = [i for i, val in enumerate(frequency) if val == max(frequency)]
        mode = [data_range[i] for i in mode_index]
        
        # Store Processed Data
        self.grouped = ProcessedData(None, bottom, top, bottom_limit, top_limit, 
                                     frequency, data_range, data_limit, data_midpoint, 
                                     bot_cumulative_frequency, top_cumulative_frequency, 
                                     relative_frequency, mode)
  
    # Populate Simple Frequency Table Data Method    
    def PopulateSimple(self):
        # Initialize variables
        data = sorted(set(self.dataset))  
        frequency = []  
        top_cumulative_frequency = []  
        bot_cumulative_frequency = []  
        relative_frequency = []  
        mode = []  

        # Check for numeric data
        top_limit = None
        bottom_limit = None

        if not all(isinstance(item, str) for item in self.dataset):
            top_limit = []
            bottom_limit = []

        # Process each class
        for current_class in data:
            current_frequency = self.dataset.count(current_class)
            frequency.append(current_frequency)

            current_relative_frequency = np.round((current_frequency / self.length) * 100, 2)
            relative_frequency.append(current_relative_frequency)

            if top_limit is not None and bottom_limit is not None:
                current_top_limit = current_class + 0.5
                current_bottom_limit = current_class - 0.5
                top_limit.append(current_top_limit)
                bottom_limit.append(current_bottom_limit)

                current_bot_cumulative_frequency = self.find_frequency(self.lowest - 0.5, current_class)
                bot_cumulative_frequency.append(current_bot_cumulative_frequency)

                current_top_cumulative_frequency = self.find_frequency(current_class, self.highest + 0.5)
                top_cumulative_frequency.append(current_top_cumulative_frequency)

            else:
                current_bot_cumulative_frequency = self.dataset.count(current_class)
                bot_cumulative_frequency.append(current_bot_cumulative_frequency)
                current_top_cumulative_frequency = sum(frequency) - current_bot_cumulative_frequency
                top_cumulative_frequency.append(current_top_cumulative_frequency)

        mode_index = [i for i, val in enumerate(frequency) if val == max(frequency)]
        mode = [data[i] for i in mode_index]

        self.simple = ProcessedData(
            data, None, None, bottom_limit, top_limit, 
            frequency, None, None, None, 
            bot_cumulative_frequency, top_cumulative_frequency, 
            relative_frequency, mode
        )
        
# Processed Data Assignment 
class ProcessedData:
    # Constructor for processed data
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
        
        self.percentage_relative_frequency = [ f"{rf * 1:.2f}%" for rf in self.relative_frequency ]
        self.mode = mode