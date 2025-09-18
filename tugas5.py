"""
NO 1
"""
# Fungsi sapaan
def greet(nama: str) -> str:
    return f"Halo, {nama}!"

# Fungsi penjumlahan
def tambah(a: float, b: float = 0.0) -> float:
    return a + b

# Fungsi menghitung rata-rata
def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:  # jika list kosong
        return 0.0
    else:
        return round(sum(angka) / len(angka), 2)  # 2 angka di belakang koma


#CONTOH PEMANGGILAN 
if __name__ == "__main__":
    print(greet("Ayudya"))              # Halo, Ayudya!
    print(tambah(5, 3))                 # 8
    print(tambah(10))                   # 10.0 (karena b default = 0.0)
    print(rata_rata([10, 20, 30, 40]))  # 25.0
    print(rata_rata([]))                # 0.0

"""
NO 2
"""
# Import fungsi rata_rata dari file sebelumnya (atau bisa tulis ulang di sini)
def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    else:
        return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []  # default list kosong

    # Tambah nilai baru
    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    # Hitung rata-rata nilai
    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    # Cek status kelulusan
    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    # Representasi string
    def __str__(self):
        return (f"Student(nama='{self.nama}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")


#CONTOH PEMAKAIAN
if __name__ == "__main__":
    mhs = Student("Budi", "A123")
    mhs.tambah_nilai(80)
    mhs.tambah_nilai(75)
    mhs.tambah_nilai(90)

    print(mhs)  # Student(nama='Budi', nim='A123', rata=81.67, status=LULUS)

    mhs2 = Student("Ani", "B456", [50, 60, 55])
    print(mhs2) # Student(nama='Ani', nim='B456', rata=55.0, status=TIDAK LULUS)

"""
NO 3
"""
#FUNCTIONS 
def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    else:
        return round(sum(angka) / len(angka), 2)


#CLASS STUDENT 
class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self):
        return (f"Student(nama='{self.nama}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")


# ==== DEMO ====
if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Ayudya"))
    print("tambah(5, 7) =", tambah(5, 7))
    print("tambah(10) =", tambah(10))
    print("rata_rata([80, 90, 100]) =", rata_rata([80, 90, 100]))
    print("rata_rata([]) =", rata_rata([]))

    print("\n=== CLASS STUDENT ===")
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(90)
    mhs1.tambah_nilai(100)

    print(mhs1)  # otomatis panggil __str__

    mhs2 = Student("Ani", "B456", [60, 70, 65])
    print(mhs2)

"""
NO 4
"""
def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    else:
        return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self):
        return (f"Student(nama='{self.nama}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")


if __name__ == "__main__":
    # Mahasiswa 1
    mhs1 = Student("Budi", "A123")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(90)
    mhs1.tambah_nilai(100)

    # Mahasiswa 2
    mhs2 = Student("Ani", "B456")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(70)
    mhs2.tambah_nilai(65)

    print("=== DATA MAHASISWA ===")
    print(mhs1)  # otomatis panggil __str__
    print("Rata-rata:", mhs1.rata_nilai())
    print("Status:", mhs1.status())

    print()

    print(mhs2)
    print("Rata-rata:", mhs2.rata_nilai())
    print("Status:", mhs2.status())

