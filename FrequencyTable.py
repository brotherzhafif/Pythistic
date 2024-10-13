import numpy as np
from scipy import stats

# Frequency Table Class 
class FrequencyTable:
    def __init__(self, dataset):
        # Data Initiation
        self.dataset = sorted(dataset)
        self.length = len(dataset)
        self.lowest = min(dataset)
        self.highest = max(dataset)
        
         # Classes is Rounding Down
        # Math Log Base 10 In Python For Accurate Result
        self.classes = 1 + (3.222 * np.log10(self.length))
        self.classes = round(self.classes - 0.5)
            
        # Condition if the data is contain string
        if not any(isinstance(item, str) for item in self.dataset):  
            # Sum of the data and range
            self.sum = sum(dataset)
            self.range = self.highest - self.lowest

            # Interval is Rounding Up
            self.interval = self.range / self.classes 
            self.interval = round(self.interval + 0.5)

            # Rounding Both Limit So The Data Would Be Simple And Easier To Read
            self.base = self.roundy(self.lowest - 3)
            self.top = self.roundy(self.highest + 3)
            
            # Mean or Average
            self.mean = (self.sum / self.length)

            # Formula for Variance
            self.variance = sum((x - self.mean) ** 2 for x in dataset) / self.length

            # Formula for Standard Deviation
            self.deviation = (self.variance ** 0.5)
            
            # Formula to find Dataset Skewness
            self.skewness = (self.length / ((self.length - 1) * (self.length - 2))) * sum(((x - self.mean) / self.deviation) ** 3 for x in self.dataset)

            # Formula to find Dataset Kurtosis
            self.kurtosis = (self.length * (self.length + 1) * sum(((x - self.mean) / self.deviation) ** 4 for x in self.dataset) / ((self.length - 1) * (self.length - 2) * (self.length - 3))) - \
                    (3 * (self.length - 1) ** 2) / ((self.length - 2) * (self.length - 3))
  
    # Populate Grouped Table Frequency Data Method
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

        # Initiating Used Parameter for Frequency Table
        interval = self.interval
        current_number = self.base - 1
        old_number = 0

        # Processing the Frequency Table Data
        while current_number <= self.top-3:
            # Finding Class Lowest Value
            old_number = current_number + 1
            bottom.append(old_number) # 155
            
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
            current_data_range = f"{old_number} ~ {current_number}"
            data_range.append(current_data_range)

            # Adding Data Range Limit Of The Class Frequency
            current_data_limit = f"{current_bottom_limit} ~ {current_top_limit}"
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
            # Adding Percent Symbol into The Relative Frequency Coloumn
            relative_frequency.append(current_relative_frequency)    
        
        # Find Mode or Data that appears most frequently 
        mode_index = [i for i, val in enumerate(frequency) if val == max(frequency)]
        mode = [data_range[i] for i in mode_index]
        
        # Append Processed Data into Data Attributes
        self.grouped = ProcessedData(None, bottom, top, bottom_limit, top_limit, 
                                     frequency, data_range, data_limit, data_midpoint, 
                                     bot_cumulative_frequency, top_cumulative_frequency, 
                                     relative_frequency, mode)
  
    # Populate Simple Table Frequency Data Method    
    def PopulateSimple(self):
        # Deleting Duplicate and Sort the Data
        data = sorted(set(self.dataset))
        
        # Initiating Used Variable
        top_limit = []
        bottom_limit = []
        frequency = []
        top_cumulative_frequency = []
        bot_cumulative_frequency = []
        relative_frequency = []
        mode = []

        for current_class in data:
            # Bottom Limit of the Class
            current_top_limit = current_class + 0.5
            current_bottom_limit = current_class - 0.5
            
            # Top Limit of the Class
            top_limit.append(current_top_limit)
            bottom_limit.append(current_bottom_limit)

            # Calculate Current Class Frequency 
            current_frequency = self.dataset.count(current_class)
            frequency.append(current_frequency)

            # Calculate Current Class Bottom Cumulative Frequency
            current_bot_cumulative_frequency = self.find_frequency(self.lowest -1 , current_class)
            bot_cumulative_frequency.append(current_bot_cumulative_frequency)

            # Calculate Current Class Top Cumulative Frequency
            current_top_cumulative_frequency = self.find_frequency(current_class + 1, self.highest + 1)
            top_cumulative_frequency.append(current_top_cumulative_frequency)
            
            # Calculate Current Class Relative Frequency 
            current_relative_frequency = np.round((current_frequency / self.length) * 100)
            relative_frequency.append(current_relative_frequency)

        # Temukan modus
        mode_index = [i for i, val in enumerate(frequency) if val == max(frequency)]
        mode = [data[i] for i in mode_index]

        # Buat objek ProcessedData
        self.simple = ProcessedData(data, None, None, bottom_limit, top_limit, 
                                    frequency, None, None, None, 
                                    bot_cumulative_frequency, top_cumulative_frequency, 
                                    relative_frequency, mode)

    # Populate Simple String Table Frequency Data Method 
    def PopulateString(self):
        # Memastikan bahwa dataset berisi string
        if not all(isinstance(item, str) for item in self.dataset):
            raise ValueError("Dataset harus berisi string saja untuk menggunakan PopulateString.")
        
        # Menghapus duplikat dan mengurutkan data secara alfabetis
        data = sorted(set(self.dataset))
        
        # Variabel yang diperlukan
        frequency = []
        top_cumulative_frequency = []
        bot_cumulative_frequency = []
        relative_frequency = []
        mode = []

        # Menghitung frekuensi untuk setiap string unik dalam dataset
        for current_class in data:
            # Menghitung frekuensi dari string saat ini
            current_frequency = self.dataset.count(current_class)
            frequency.append(current_frequency)

            # Menghitung cumulative frequency (bawah)
            current_bot_cumulative_frequency = self.find_frequency_string(self.dataset, current_class)
            bot_cumulative_frequency.append(current_bot_cumulative_frequency)

            # Menghitung cumulative frequency (atas)
            current_top_cumulative_frequency = sum(frequency) - current_bot_cumulative_frequency
            top_cumulative_frequency.append(current_top_cumulative_frequency)

            # Menghitung relative frequency
            current_relative_frequency = np.round((current_frequency / self.length) * 100)
            relative_frequency.append(current_relative_frequency)

        # Menemukan modus (nilai string yang paling sering muncul)
        mode_index = [i for i, val in enumerate(frequency) if val == max(frequency)]
        mode = [data[i] for i in mode_index]

        # Menyimpan data yang diproses ke dalam atribut simple
        self.text = ProcessedData(data, None, None, None, None, 
                                         frequency, None, None, None, 
                                         bot_cumulative_frequency, top_cumulative_frequency, 
                                         relative_frequency, mode)
        
    def find_frequency_string(self, dataset, value):
        # Fungsi untuk menghitung frekuensi cumulative string dari dataset
        frequency = dataset.count(value)
        return frequency

    # Base 5 Rounding
    def roundy(self, x, base = 5):
        return base * round(x/base)
    
    # Function To Find Frequency in Dataset with Desired Range (Top and Down Limit)
    def find_frequency(self, bot, top):
        try:
            bot = int(bot)
            top = int(top)
        except (ValueError, TypeError) as e:
            print(f"Error converting to int: {e}")
    
        total_frequency = 0
        for i in range(bot, top):
            frequency = self.dataset.count(i)
            total_frequency = total_frequency + frequency
        return total_frequency
    
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
        
        self.percentage_relative_frequency = [ f"{rf * 1:.2f}%" for rf in self.relative_frequency ]
        self.mode = mode
        
 
