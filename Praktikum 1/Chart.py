import matplotlib.pyplot as plt

# Data preferensi minuman
minuman = ['Soda', 'Teh', 'Kopi', 'Air Putih', 'Jus']
frekuensi = [10, 25, 30, 20, 15]

#Hitung persentase
total_minuman = sum(frekuensi)
persentase = [(jumlah / total_minuman) * 100 for jumlah in frekuensi]

#Konstruksi diagram lingkaran
plt.figure(figsize=(6, 6))
plt.pie(persentase, labels=minuman, autopct='%1.1f%%', startangle=90)
plt.title('Diagram Lingkaran Jumlah Minuman')
plt.axis('equal') # Agar lingkaran menjadi Lingkaran sejati

# Menampilkan diagram pie
plt.show()
