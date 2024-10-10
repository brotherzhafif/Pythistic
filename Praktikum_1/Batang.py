import matplotlib.pyplot as plt

# Data preferensi minuman

minuman = ['Soda', 'Teh', 'Kopi', 'Air Putih', 'Jus']
frekuensi = [10, 25, 30, 20, 15]

# Membuat diagram batang
plt.bar(minuman, frekuensi, color='blue', edgecolor='black')

# Menambahkan judul dan label sumbu
plt.title('Preferensi Minuman')
plt.xlabel('Jenis Minuman')
plt.ylabel('Jumlah Orang')

# Menampilkan diagram batang
plt.show()
