import numpy as np

class Transform:
    def __init__(self, data):
        # Initialize the Transform class with the raw data.
        self.data = np.array(data, dtype=float)
        self.transformed_data = []  # Store transformed data here

    def log_transform(self):
        # Apply logarithmic transformation manually.
        if np.any(self.data <= 0):
            raise ValueError("Log transformation requires positive data values.")
        transformed = [np.log(x) for x in self.data]
        self.transformed_data.append(transformed)
        return transformed

    def square_root_transform(self):
        # Apply square root transformation manually.
        if np.any(self.data < 0):
            raise ValueError("Square root transformation requires non-negative data values.")
        transformed = [np.sqrt(x) for x in self.data]
        self.transformed_data.append(transformed)
        return transformed

    def cube_root_transform(self):
        # Apply cube root transformation manually.
        transformed = [x ** (1/3) for x in self.data]
        self.transformed_data.append(transformed)
        return transformed

    def reciprocal_transform(self):
        # Apply reciprocal transformation manually.
        if np.any(self.data == 0):
            raise ValueError("Reciprocal transformation cannot be applied to data containing zero.")
        transformed = [1 / x for x in self.data]
        self.transformed_data.append(transformed)
        return transformed

    def box_cox_transform(self, lmbda=None):
        # Apply Box-Cox transformation manually.
        if np.any(self.data <= 0):
            raise ValueError("Box-Cox transformation requires positive data values.")
        if lmbda is None:
            lmbda = 0  # Default to zero for natural log transform as an example
        if lmbda == 0:
            transformed = [np.log(x) for x in self.data]
        else:
            transformed = [(x ** lmbda - 1) / lmbda for x in self.data]
        self.transformed_data.append(transformed)
        return transformed, lmbda

    def yeo_johnson_transform(self, lmbda=None):
        # Apply Yeo-Johnson transformation manually.
        if lmbda is None:
            lmbda = 0  # Default to zero for natural log transform of y + 1
        transformed = [
            (x + 1) ** lmbda - 1 / lmbda if lmbda != 0 else np.log(x + 1)
            for x in self.data
        ]
        self.transformed_data.append(transformed)
        return transformed, lmbda

    def z_score_standardization(self):
        # Apply Z-score standardization manually.
        mean = np.mean(self.data)
        std_dev = np.std(self.data)
        transformed = [(x - mean) / std_dev for x in self.data]
        self.transformed_data.append(transformed)
        return transformed

    def min_max_scaling(self, feature_range=(0, 1)):
        # Apply Min-Max scaling manually.
        min_val = np.min(self.data)
        max_val = np.max(self.data)
        scale = feature_range[1] - feature_range[0]
        transformed = [
            feature_range[0] + ((x - min_val) / (max_val - min_val)) * scale
            for x in self.data
        ]
        self.transformed_data.append(transformed)
        return transformed

    def rank_transform(self):
        # Apply rank transformation manually.
        sorted_indices = np.argsort(self.data)
        ranks = np.argsort(sorted_indices)
        transformed = ranks.tolist()
        self.transformed_data.append(transformed)
        return transformed

    def arcsine_transform(self):
        # Apply arcsine transformation manually.
        if np.any((self.data < 0) | (self.data > 1)):
            raise ValueError("Arcsine transformation requires data in the range [0, 1].")
        transformed = [np.arcsin(np.sqrt(x)) for x in self.data]
        self.transformed_data.append(transformed)
        return transformed

    def exponential_transform(self, base=np.e):
        # Apply exponential transformation manually.
        transformed = [base ** x for x in self.data]
        self.transformed_data.append(transformed)
        return transformed

    def logit_transform(self):
        # Apply logit transformation manually.
        if np.any((self.data <= 0) | (self.data >= 1)):
            raise ValueError("Logit transformation requires data between 0 and 1 (exclusive).")
        transformed = [np.log(x / (1 - x)) for x in self.data]
        self.transformed_data.append(transformed)
        return transformed
