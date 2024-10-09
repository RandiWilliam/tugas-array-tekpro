# Mengambil input dari pengguna
input_nilai = input("Masukkan nilai (pisahkan dengan koma): ")

# Mengubah input string menjadi list dan mengonversi ke integer
nilai_array = [int(x) for x in input_nilai.split(",")]

# Menghitung total
total = sum(nilai_array)

# Menampilkan hasil
print("Total:", total)