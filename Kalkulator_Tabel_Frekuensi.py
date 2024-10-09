import math

# Soal No 1
dataset = (
  165, 170, 172, 160, 175, 168, 180, 174, 169, 177,
  162, 167, 173, 178, 164, 171, 176, 166, 182, 159,
  161, 172, 169, 163, 179, 177, 158, 180, 170, 173,
  174, 168, 171, 178, 166, 160, 181, 165, 167, 176,
  159, 183, 161, 175, 169, 172, 164, 162, 174, 173,
  171, 178, 164, 167, 181, 166, 170, 177, 180, 176,
  182, 175, 161, 160, 165, 168, 172, 170, 179, 177,
  162, 169, 174, 168, 173, 176, 182, 165, 159, 171)

# Inisiasi data
dataset = sorted(dataset)
jumlah = len(dataset) # 80 Orang
dataset = sorted(dataset)
ranges = max(dataset) - min(dataset) # Rangenya 25
print("Ranges = " + str(ranges))

# Kelas dibulatkan kebawah
# Math Log Basis 10 Di Python Biar Akurat
kelas = 1 + (3.222 * math.log(jumlah, 10)) # 7.13
print("Kelas = " + str(kelas))

# Interval dibulatkan keatas
interval = ranges / kelas # 3.5
print("Interval = " + str(interval))

# Kode Untuk Mencari Frekuensi Belum Automatis
batas_bawah = 183
batas_atas = 186
total_frekuensi = 0

for i in range(batas_bawah, batas_atas + 1):
    frekuensi = dataset.count(i)
    total_frekuensi = total_frekuensi + frekuensi

print(total_frekuensi)
