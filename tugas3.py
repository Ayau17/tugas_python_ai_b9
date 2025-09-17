"""
NO 1
"""
# String (teks)
nama = "Ayudya"

# Integer (bilangan bulat)
umur = 20

# Float (bilangan desimal)
tinggi = 153.5

# Boolean (nilai benar atau salah)
is_mahasiswa = True

# List (kumpulan data)
hobi = ["menyanyi", "menonton"]

print(nama,umur,tinggi,is_mahasiswa,hobi[0],hobi[1])

"""
NO 2
"""
# String dasar
teks1 = "Halo"
teks2 = "Nama"
teks3 = "Saya"
teks4 = "Ayudya"
# 1. Menggabungkan string
gabung = teks1 + " " + teks2 + " " + teks3 + " " + teks4
print("Gabungan string:", gabung)

# 2. Menghitung panjang string
panjang = len(gabung)
print("Panjang string:", panjang)

# 3. Mengubah huruf jadi besar semua
print("Uppercase:", gabung.upper())

# 4. Mengubah huruf jadi kecil semua
print("Lowercase:", gabung.lower())

"""
NO 3
"""
# Deklarasi variabel angka
a = 12
b = 17

# Operasi dasar
print("Penjumlahan:", a + b)   # +
print("Pengurangan:", a - b)   # -
print("Perkalian:", a * b)    # *
print("Pembagian:", a / b)    # /
print("Pembagian bulat:", a // b)  # //
print("Sisa bagi:", a % b)    # %

"""
NO 4
"""
# Membuat list dengan 5 item
Alat = ["Pena", "Buku", "Meja", "Tas", "Penggaris"]

# 1. Menampilkan list
print("Daftar Alat:", Alat)

# 2. Mengakses elemen tertentu (index dimulai dari 0)
print("Alat pertama:", Alat[0])   # Pena
print("Alat ketiga:", Alat[2])   # Buku
print("Alat terakhir:", Alat[-1]) # Meja

# 3. Menambahkan item baru
Alat.append("Meja")
print("Setelah ditambah:", Alat)

# 4. Menghapus item dengan nama (remove)
Alat.remove("Meja")
print("Setelah menghapus 'Meja':", Alat)

# 5. Menghapus item berdasarkan index (pop)
Alat.pop(2)   # menghapus item ke-3 (index 2)
print("Setelah pop index 2:", Alat)

"""
NO 5
"""
# Meminta input dari user
nama = input("Masukkan nama:")
umur = input("Masukkan umur:")
tinggal = input("Masukkan tinggal:")
hobi = input("Masukkan hobi:")

# Menampilkan kalimat perkenalan
print(f"Halo, nama saya {nama} dan umur saya {umur} tahun. Saya tinggal di {tinggal} dan hobi saya adalah {hobi}.")

