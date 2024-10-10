import matplotlib.pyplot as plt

# Data dari tabel
rentang_nilai = ['155 ~ 158', '159 ~ 162', 
                 '163 ~ 166', '167 ~ 170', 
                 '171 ~ 174', '175 ~ 178', 
                 '179 ~ 182', '183 ~ 186']
frekuensi = [1, 12, 11, 15, 16, 14, 10, 1]

# Membuat histogram
plt.bar(rentang_nilai, frekuensi, color='blue', edgecolor='black')

# Menambahkan judul dan label sumbu
plt.title('Histogram Rentang Nilai')
plt.xlabel('Rentang Nilai')
plt.ylabel('Frekuensi')

# Menampilkan histogram
plt.show()
