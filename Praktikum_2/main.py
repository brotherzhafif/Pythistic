import numpy as np
import scipy.stats as boxcox

# Logaritmik
data_pengeluaran = [100, 200, 150, 300, 250, 400, 350, 500]
data_log = np.log10(data_pengeluaran)

print(data_pengeluaran)
print(data_log)

# Quadratic
data_tinggi_badan = [150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
data_tinggi_badan_akar = [np.sqrt(x) for x in data_tinggi_badan]

print(data_tinggi_badan)
print(data_tinggi_badan_akar)

# Reciprocal
def reciprocal_transform(data):
    reciprocal_data = [1/x for x in data]
    return reciprocal_data

data_awal = [2,4,6,8,10]

# Box Cox
data_pengeluaran = [100, 200, 150, 300, 250, 400, 350, 500]

data_transormed, lam = boxcox(data_pengeluaran)

print(data_pengeluaran)
print(data_transormed)
print(lam)

