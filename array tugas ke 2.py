#mendefinisikan array hari
hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

# mengambil input dari pengguna
input_hari = int(input("masukkan angka (1-7 untuk menampilkan hari: "))

#menampilkan hasil yang sesuai dengan input
if 1<=input_hari <= 7:
    print("hari:", hari[input_hari - 1])
else:
    print("input tidak valid! masukkan angka dari 1-7")