"""
NO 1
"""
# Membuat list campuran dengan ≥ 6 elemen
data = ["apel", 10, "jeruk", 25, "mangga", 30]

print("List awal:", data)

# Akses elemen pertama & terakhir
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])

# Slicing [start:stop:step]
print("Slicing data[1:5:2]:", data[1:5:2])

# Manipulasi List
# append() -> menambah item di akhir
data.append("semangka")
print("\nSetelah append('semangka'):", data)

# insert() -> menambah item di posisi tertentu
data.insert(2, "pisang")  # disisipkan di index ke-2
print("Setelah insert(2, 'pisang'):", data)

# extend() -> menambah banyak item sekaligus
data.extend(["durian", 100])
print("Setelah extend(['durian', 100]):", data)

# pop() -> menghapus item berdasarkan index
data.pop(3)  # hapus item di index ke-3
print("Setelah pop(3):", data)

# remove() -> menghapus item berdasarkan nilai
data.remove("apel")  # hapus elemen "apel"
print("Setelah remove('apel'):", data)

"""
NO 2
"""
# Membuat tuple dengan ≥ 5 elemen
data_tuple = ("apel", "jeruk", "mangga", "pisang", "anggur", "melon")

print("=== TUPLE AWAL ===")
print(data_tuple)

# Panjang tuple
print("\nPanjang tuple:", len(data_tuple))

# Akses indeks
print("Elemen pertama:", data_tuple[0])
print("Elemen ketiga:", data_tuple[2])
print("Elemen terakhir:", data_tuple[-1])

# Unpacking tuple (dengan *rest)
buah1, buah2, *rest = data_tuple

print("\n=== UNPACKING ===")
print("Buah 1:", buah1)
print("Buah 2:", buah2)
print("Sisa buah:", rest)

"""
NO 3
"""
# Membuat dua set dengan elemen tumpang tindih
set_a = {"apel", "jeruk", "mangga", "pisang", "apel", "anggur"}
set_b = {"mangga", "pisang", "durian", "jeruk", "melon"}

print("=== SET AWAL ===")
print("Set A:", set_a)
print("Set B:", set_b)

# Union (gabungan)
print("\nUnion (A | B):", set_a | set_b)

# Intersection (irisan)
print("Intersection (A & B):", set_a & set_b)

# Difference (selisih)
print("Difference (A - B):", set_a - set_b)
print("Difference (B - A):", set_b - set_a)

# Symmetric Difference (selisih gabungan)
print("Symmetric Difference (A ^ B):", set_a ^ set_b)

"""
NO 4
"""
# Membuat dictionary data mahasiswa
mahasiswa = {
    "nama": "Ayudya",
    "nim": "123456",
    "angkatan": 2023,
    "kota": "Batam"
}

print("=== DICTIONARY AWAL ===")
print(mahasiswa)

# Tambah key baru
mahasiswa["jurusan"] = "Sistem Informasi"
print("\nSetelah tambah key 'jurusan':", mahasiswa)

# Ubah nilai key
mahasiswa["kota"] = "Jakarta"
print("\nSetelah ubah nilai 'kota':", mahasiswa)

# Hapus key
mahasiswa.pop("angkatan")
print("\nSetelah hapus key 'angkatan':", mahasiswa)

# Menampilkan keys(), values(), items()
print("\nKeys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

# Iterasi menampilkan key: value
print("\nIterasi dictionary:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

"""
NO 5
"""
# Membuat list berisi dictionary (daftar buku)
buku_list = [
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun": 2005},
    {"judul": "Pulang", "penulis": "Leila S. Chudori", "tahun": 2012},
]

print("=== DAFTAR BUKU ===")
for buku in buku_list:
    print(buku)

# Cetak semua judul dengan loop
print("\n=== JUDUL BUKU ===")
for buku in buku_list:
    print(buku["judul"])

# Filter buku terbit >= tahun tertentu
tahun_filter = 2000
buku_modern = [buku for buku in buku_list if buku["tahun"] >= tahun_filter]

print(f"\n=== BUKU TERBIT >= {tahun_filter} ===")
for buku in buku_modern:
    print(f"{buku['judul']} ({buku['tahun']})")

"""
NO 6
"""
#List comprehension
angka = list(range(1, 21))

# List angka genap
genap = [x for x in angka if x % 2 == 0]

# List kuadrat
kuadrat = [x**2 for x in angka]

print("=== LIST COMPREHENSION ===")
print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

#Dict comprehension
dict_ganjil_genap = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}

print("\n=== DICT COMPREHENSION ===")
print(dict_ganjil_genap)

#Set comprehension
kalimat = "Belajar Python itu Menyenangkan"
huruf_unik = {ch.lower() for ch in kalimat if ch.isalpha()}

print("\n=== SET COMPREHENSION ===")
print("Huruf unik:", huruf_unik)

"""
NO 7
"""
# Contoh List
buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

# Contoh Set
warna = {"merah", "hijau", "biru", "kuning"}

print("=== CEK KEANGGOTAAN LIST ===")
item = "mangga"
if item in buah:
    posisi = buah.index(item)  # cari posisi item
    print(f"{item} ada di list pada index {posisi}")
else:
    print(f"{item} tidak ditemukan di list")

item2 = "durian"
if item2 in buah:
    print(f"{item2} ada di list")
else:
    print(f"{item2} tidak ada di list")

print("\n=== CEK KEANGGOTAAN SET ===")
cek_warna = "hijau"
if cek_warna in warna:
    print(f"{cek_warna} ada di dalam set")
else:
    print(f"{cek_warna} tidak ada di dalam set")

cek_warna2 = "ungu"
if cek_warna2 in warna:
    print(f"{cek_warna2} ada di dalam set")
else:
    print(f"{cek_warna2} tidak ada di dalam set")


