import numpy as np

class StatisticalCalculations:
    @staticmethod
    def mean(dataset):
        return sum(dataset) / len(dataset)

    @staticmethod
    def variance(dataset, mean):
        return sum((x - mean) ** 2 for x in dataset) / len(dataset)

    @staticmethod
    def standard_deviation(variance):
        return variance ** 0.5

    @staticmethod
    def skewness(dataset, mean, deviation):
        n = len(dataset)
        return (n / ((n - 1) * (n - 2))) * sum(((x - mean) / deviation) ** 3 for x in dataset)

    @staticmethod
    def kurtosis(dataset, mean, deviation):
        n = len(dataset)
        return (n * (n + 1) * sum(((x - mean) / deviation) ** 4 for x in dataset) /
                ((n - 1) * (n - 2) * (n - 3))) - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    
    @staticmethod
    def median(dataset):
        sorted_data = sorted(dataset)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:  # If even, return the average of the two middle numbers
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:  # If odd, return the middle number
            return sorted_data[mid]

# Processed Data Assignment 
class ProcessedData:
    def __init__(self, data, bot, top, bot_L, top_L, F, R, L, M, bot_CF, top_CF, RF, mode):
        self.top = top
        self.limit = L     
        self.ranges = R      
        self.bottom = bot
        self.midpoint = M
        self.frequency = F
        self.classval = data
        self.top_limit = top_L
        self.bottom_limit = bot_L
        self.mode = mode
        self.bottom_cumulative_frequency = bot_CF
        self.top_cumulative_frequency = top_CF
        self.relative_frequency = RF
        self.percentage_relative_frequency = [f"{rf:.2f}%" for rf in self.relative_frequency]

# Frequency Table Class 
class FrequencyTable:
    def __init__(self, dataset):
        # Check for mixed data types
        if any(isinstance(item, str) for item in dataset) and any(isinstance(item, (int, float)) for item in dataset):
            raise ValueError("Data is corrupted: contains both numeric and string values.")

        # Data Initiation
        self.dataset = sorted(dataset)
        self.length = len(dataset)
        self.lowest = min(dataset) if isinstance(dataset[0], (int, float)) else None
        self.highest = max(dataset) if isinstance(dataset[0], (int, float)) else None

        if self.lowest is not None:  # Only calculate classes for numeric data
            self.calculate_statistics()
            self.calculate_classes()

    def calculate_statistics(self):
        self.sum = sum(self.dataset)
        self.mean = StatisticalCalculations.mean(self.dataset)
        self.median = StatisticalCalculations.median(self.dataset)
        self.variance = StatisticalCalculations.variance(self.dataset, self.mean)
        self.deviation = StatisticalCalculations.standard_deviation(self.variance)
        self.skewness = StatisticalCalculations.skewness(self.dataset, self.mean, self.deviation)
        self.kurtosis = StatisticalCalculations.kurtosis(self.dataset, self.mean, self.deviation)

    def calculate_classes(self):
        self.classes = 1 + (3.222 * np.log10(self.length))
        self.classes = round(self.classes - 0.5)
        self.range = self.highest - self.lowest
        self.interval = round((self.range / self.classes) + 0.5)
        self.base = self.roundy(self.lowest - 3)

    # Base 5 Rounding
    def roundy(self, x, base=5):
        return base * round(x / base)

    def reset(self):
        # Clear all internal attributes
        self.bottom = []
        self.top = []
        self.top_limit = []
        self.bottom_limit = []
        self.frequency = []
        self.data_range = []
        self.data_limit = []
        self.data_midpoint = []
        self.bot_cumulative_frequency = []
        self.top_cumulative_frequency = []
        self.relative_frequency = []
        self.mode = []

    def find_frequency(self, bot, top):
        return sum(1 for x in self.dataset if bot <= x < top)

    def populate_grouped(self):
        self.reset()
        
        # Initiating Variables for Frequency Table
        current_number = self.base - 1

        while True:
            old_number = current_number + 1
            self.bottom.append(old_number)

            current_number += self.interval
            self.top.append(current_number)

            self.bottom_limit.append(old_number - 0.5)
            self.top_limit.append(current_number + 0.5)

            current_frequency = self.find_frequency(old_number, current_number + 1)
            self.frequency.append(current_frequency)

            current_data_range = f"{old_number:.2f} ~ {current_number:.2f}"
            self.data_range.append(current_data_range)

            current_data_limit = f"{old_number - 0.5:.2f} ~ {current_number + 0.5:.2f}"
            self.data_limit.append(current_data_limit)

            self.data_midpoint.append((old_number + current_number) / 2)

            bot_cumulative_freq = self.find_frequency(self.lowest - 1, old_number)
            self.bot_cumulative_frequency.append(bot_cumulative_freq)

            top_cumulative_freq = self.find_frequency(current_number + 1, self.highest + 1)
            self.top_cumulative_frequency.append(top_cumulative_freq)

            current_relative_frequency = np.round((current_frequency / self.length) * 100)
            self.relative_frequency.append(current_relative_frequency)

            if current_frequency == 0:
                break

        # Find Mode
        mode_index = [i for i, val in enumerate(self.frequency) if val == max(self.frequency)]
        self.mode = [self.data_range[i] for i in mode_index]

        # Create ProcessedData object
        self.grouped = ProcessedData(None, self.bottom, self.top, self.bottom_limit, self.top_limit,
                                     self.frequency, self.data_range, self.data_limit, self.data_midpoint,
                                     self.bot_cumulative_frequency, self.top_cumulative_frequency,
                                     self.relative_frequency, self.mode,
                                     )

    def populate_simple(self):
        self.reset()
        unique_data = sorted(set(self.dataset))

        for current_class in unique_data:
            current_frequency = self.dataset.count(current_class)
            self.frequency.append(current_frequency)

            current_relative_frequency = np.round((current_frequency / self.length) * 100)
            self.relative_frequency.append(current_relative_frequency)

            current_bottom_limit = current_class - 0.5
            current_top_limit = current_class + 0.5
            self.bottom_limit.append(current_bottom_limit)
            self.top_limit.append(current_top_limit)

            bot_cumulative_freq = self.find_frequency(self.lowest - 1, current_class)
            self.bot_cumulative_frequency.append(bot_cumulative_freq)

            top_cumulative_freq = self.find_frequency(current_class + 1, self.highest + 1)
            self.top_cumulative_frequency.append(top_cumulative_freq)

        # Find Mode
        mode_index = [i for i, val in enumerate(self.frequency) if val == max(self.frequency)]
        self.mode = [unique_data[i] for i in mode_index]

        # Create ProcessedData object
        self.simple = ProcessedData(
            unique_data, None, None, self.bottom_limit, self.top_limit, 
            self.frequency, None, None, None, 
            self.bot_cumulative_frequency, self.top_cumulative_frequency, 
            self.relative_frequency, self.mode, 
            )