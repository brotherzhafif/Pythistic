import FrequencyTable as ft

# Misalnya, Anda punya data mentah seperti ini:
data = (
  58, 67, 45, 89, 72, 60, 76, 93, 
  55, 48, 62, 85, 79, 56, 41, 90, 
  77, 54, 68, 82, 46, 73, 57, 92, 
  81, 53, 66, 74, 64, 52, 91, 78, 
  49, 87, 88, 50, 69, 84, 43, 65, 
  83, 70, 44, 61, 75, 80, 71, 63, 47,51)

# Membuat objek dari FrequencyTable dengan data mentah
table = ft.FrequencyTable(data)

# Memproses data mentah menjadi tabel frekuensi
table.Populate()

print(table.data.ranges)      # Output: [0, 10, 20, 30] (data terproses)
print(table.data.frequency)      # Output: [10, 20, 30, 40] (data terproses)
