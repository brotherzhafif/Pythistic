# Transform.py
import numpy as np
from scipy.stats import boxcox, yeojohnson

class Transform:
    def __init__(self, data):
        # Initialize the Transform class with the raw data.
        self.data = np.array(data)

    def log_transform(self):
        # Apply logarithmic transformation to the data.
        if np.any(self.data <= 0):
            raise ValueError("Log transformation requires positive data values.")
        return np.log(self.data)

    def square_root_transform(self):
        # Apply square root transformation to the data.
        if np.any(self.data < 0):
            raise ValueError("Square root transformation requires non-negative data values.")
        return np.sqrt(self.data)

    def cube_root_transform(self):
        # Apply cube root transformation to the data.
        return np.cbrt(self.data)

    def reciprocal_transform(self):
        # Apply reciprocal transformation to the data.
        if np.any(self.data == 0):
            raise ValueError("Reciprocal transformation cannot be applied to data containing zero.")
        return 1 / self.data

    def box_cox_transform(self, lmbda=None):
        # Apply Box-Cox transformation to the data.
        if np.any(self.data <= 0):
            raise ValueError("Box-Cox transformation requires positive data values.")
        transformed_data, best_lambda = boxcox(self.data, lmbda)
        return transformed_data, best_lambda

    def yeo_johnson_transform(self, lmbda=None):
        # Apply Yeo-Johnson transformation to the data.
        transformed_data, best_lambda = yeojohnson(self.data, lmbda)
        return transformed_data, best_lambda

    def z_score_standardization(self):
        # Apply Z-score standardization to the data.
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        return (self.data - mean) / std_dev

    def min_max_scaling(self, feature_range=(0, 1)):
        # Apply Min-Max scaling to the data.
        min_val = np.min(self.data)
        max_val = np.max(self.data)
        scale = feature_range[1] - feature_range[0]
        return feature_range[0] + ((self.data - min_val) / (max_val - min_val)) * scale

    def rank_transform(self):
        # Apply rank transformation to the data.
        return np.argsort(np.argsort(self.data))

    def arcsine_transform(self):
        # Apply arcsine transformation to the data.
        if np.any((self.data < 0) | (self.data > 1)):
            raise ValueError("Arcsine transformation requires data in the range [0, 1].")
        return np.arcsin(np.sqrt(self.data))

    def exponential_transform(self, base=np.e):
        # Apply exponential transformation to the data.
        return np.power(base, self.data)

    def logit_transform(self):
        # Apply logit transformation to the data.
        if np.any((self.data <= 0) | (self.data >= 1)):
            raise ValueError("Logit transformation requires data between 0 and 1 (exclusive).")
        return np.log(self.data / (1 - self.data))
