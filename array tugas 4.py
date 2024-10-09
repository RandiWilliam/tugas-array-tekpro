# Mengambil input dari pengguna
input_nilai = input("Masukkan nilai (pisahkan dengan koma): ")

# Mengubah input string menjadi list dan mengonversi ke integer
nilai_array = [int(x) for x in input_nilai.split(",")]

# Mengurutkan array dari kecil ke besar
nilai_array.sort()

# Menampilkan hasil
print("Array setelah diurutkan:", nilai_array)