# Tugas ketiga 
def cek (nama):
    Karyawan = ["budi", "bunga", "alex", "mawar", "dani", "sultan"]
    if nama.lower() in Karyawan:
        return f"{nama.capitalize()} adalah karyawan."
    else:
        return f"{nama.capitalize()} bukan karyawan."

nama = input("Input Nama Karyawan: ")
print (cek(nama))