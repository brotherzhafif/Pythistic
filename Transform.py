import numpy as np
from scipy import stats

class Transform:
    def __init__(self, dataset):
        # Initialize the Transform class with the raw data.
        self.dataset = sorted(dataset)

        # Basic Statistic Variable 
        self.mean = np.mean(dataset)
        self.std = np.std(dataset)
        self.min_value = np.min(dataset)
        self.max_value = np.max(dataset)
        self.length = len(dataset)
        self.lambda_value = None

        self.transformed_data = []  # Store transformed data here
    
    def logaritmic(self):
        self.transformed_data = [np.log10(x) for x in self.data]

    def sqrt_root(self):
        self.transformed_data = [np.sqrt(x) for x in self.data]

    def power_two(self):
        self.transformed_data = [x**2 for x in self.dataset]
    
    def reciprocal(self):
        self.transformed_data = [1 / (x + 1e-9) for x in self.dataset]

    def z_score(self):
        self.transformed_data = [(x - self.mean) / self.std for x in self.dataset]
    
    def min_max(self):
        self.transformed_data = [(x - self.min_value) / (self.max_value - self.min_value) for x in self.dataset]
    
    def boxcox(self):
        self.transformed_data, self.lambda_value = stats.boxcox([x for x in self.data if x > 0])  # Box-Cox hanya untuk data positif
        self.transformed_data = self.transformed_data.tolist()  # Mengonversi hasil ke list

    def logit(self):
        self.transformed_data = [np.log(x / (1 - x + 1e-9)) for x in self.dataset]  # Menambahkan epsilon untuk menghindari log(0)

    def yeo_johnshon(self):
        self.transformed_data = stats.yeojohnson(self.dataset)
        self.transformed_data = self.transformed_data.tolist()