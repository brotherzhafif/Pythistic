import matplotlib.pyplot as plt

# Data
# Array Berat Badan (BB)
BB = [
    55, 64, 50, 58, 79,
    60, 70, 53, 64, 65,
    65, 73, 56, 68, 63,
    70, 66, 63, 75, 55,
    58, 78, 66, 69, 60,
    62, 85, 74, 73, 57,
    75, 90, 82, 81, 70,
    80, 72, 67, 78, 80,
    68, 76, 71, 88, 86,
    59, 81, 77, 83, 90
]

# Array Tinggi Badan (TB)
TB = [
    160, 168, 155, 164, 177,
    162, 173, 158, 169, 167,
    165, 176, 161, 173, 166,
    170, 171, 169, 179, 159,
    163, 177, 170, 170, 162,
    167, 183, 178, 177, 165,
    180, 185, 180, 182, 172,
    175, 174, 172, 178, 181,
    172, 179, 175, 184, 185,
    161, 181, 182, 180, 188
]

# Mengatur warna berdasarkan kondisi berat badan
colors = ['red' if weight > 70 else 'blue' for weight in BB]

# Membuat scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(BB, TB, c=colors)

plt.title('Hubungan Berat Badan dan Tinggi Badan')
plt.xlabel('Berat Badan (kg)')
plt.ylabel('Tinggi Badan (cm)')
plt.grid(True)
plt.show()
