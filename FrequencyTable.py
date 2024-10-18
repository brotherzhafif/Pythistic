import numpy as np
from Calculations import Describe
from Summary import Result

class Classify:
    def __init__(self, dataset):
        if any(isinstance(item, str) for item in dataset) and any(isinstance(item, (int, float)) for item in dataset):
            raise ValueError("Data is corrupted: contains both numeric and string values.")

        self.dataset = sorted(dataset)
        self.length = len(dataset)
        self.lowest = min(dataset) if isinstance(dataset[0], (int, float)) else None
        self.highest = max(dataset) if isinstance(dataset[0], (int, float)) else None

        if self.lowest is not None:
            self._calculate_statistics()
            self._calculate_classes()

    def _calculate_statistics(self):
        self.sum = sum(self.dataset)
        self.mean = Describe.mean(self.dataset)
        self.median = Describe.median(self.dataset)
        self.variance = Describe.variance(self.dataset, self.mean)
        self.deviation = Describe.standard_deviation(self.variance)
        self.skewness = Describe.skewness(self.dataset, self.mean, self.deviation)
        self.kurtosis = Describe.kurtosis(self.dataset, self.mean, self.deviation)

    def _calculate_classes(self):
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
        top_cumulative_freq = 1

        while top_cumulative_freq != 0:
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

        # Find Mode
        mode_index = [i for i, val in enumerate(self.frequency) if val == max(self.frequency)]
        self.mode = [self.data_range[i] for i in mode_index]

        # Create Result object
        self.grouped = Result(None, self.bottom, self.top, self.bottom_limit, self.top_limit,
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

        # Create Result object
        self.simple = Result(
            unique_data, None, None, self.bottom_limit, self.top_limit, 
            self.frequency, None, None, None, 
            self.bot_cumulative_frequency, self.top_cumulative_frequency, 
            self.relative_frequency, self.mode, 
            )