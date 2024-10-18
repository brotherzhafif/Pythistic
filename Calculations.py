class Describe:
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

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
