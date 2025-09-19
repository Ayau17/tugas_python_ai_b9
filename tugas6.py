"""
NO 1
"""
#Import & Setup 
import numpy as np
import pandas as pd
import os   # opsional

if __name__ == "__main__":
    print("=== DEMO IMPORT & SETUP ===")

    # Cek current working directory (opsional, pakai os)
    print("Current working directory:", os.getcwd())

    # Buat array random dengan numpy
    arr = np.random.randint(1, 100, size=10)
    print("Array random:", arr)

    # Buat DataFrame sederhana dengan pandas
    data = {
        "Nama": ["Budi", "Ani", "Citra", "Dewi"],
        "Nilai": [80, 90, 75, 88]
    }
    df = pd.DataFrame(data)
    print("\nDataFrame:\n", df)

"""
NO 2
"""
import numpy as np
# Set seed agar data random konsisten (opsional)
np.random.seed(42)

# Buat array nilai ujian (10 data acak antara 50–100)
nilai_ujian = np.random.randint(50, 101, size=10)
print("Data nilai ujian:", nilai_ujian)

# Hitung statistik dasar
rata2 = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

# Tampilkan hasil
print("\n=== STATISTIK NILAI ===")
print(f"Rata-rata     : {rata2:.2f}")
print(f"Median        : {median}")
print(f"Standar Deviasi: {std_dev:.2f}")
print(f"Nilai Minimum : {nilai_min}")
print(f"Nilai Maksimum: {nilai_max}")

"""
NO 3
"""
import numpy as np
import pandas as pd

# Set seed biar konsisten
np.random.seed(42)

# Buat data nilai (acak antara 50–100 untuk 5 mahasiswa)
nilai = np.random.randint(50, 101, size=5)

# Buat DataFrame
data = {
    "nama": ["Budi", "Ani", "Citra", "Dewi", "Eko"],
    "nim": ["A001", "A002", "A003", "A004", "A005"],
    "nilai": nilai
}
df = pd.DataFrame(data)

# Tambahkan kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

# Tampilkan 5 baris pertama
print(df.head())

"""
NO 4
"""
import numpy as np
import pandas as pd

#Data & Statistik NumPy
np.random.seed(42)
nilai_ujian = np.random.randint(50, 101, size=10)

rata2 = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

#DataFrame Pandas
data = {
    "nama": ["Budi", "Ani", "Citra", "Dewi", "Eko"],
    "nim": ["A001", "A002", "A003", "A004", "A005"],
    "nilai": nilai_ujian[:5]   # ambil 5 nilai pertama
}
df = pd.DataFrame(data)
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

# Ringkasan DataFrame
jumlah_baris = len(df)
jumlah_lulus = (df["status"] == "LULUS").sum()
jumlah_tidak = (df["status"] == "TIDAK LULUS").sum()

#Tulis ke file .txt
with open("ringkasan_tugas6.txt", "w") as f:
    f.write("=== RINGKASAN STATISTIK NILAI ===\n")
    f.write(f"Rata-rata      : {rata2:.2f}\n")
    f.write(f"Median         : {median}\n")
    f.write(f"Standar Deviasi: {std_dev:.2f}\n")
    f.write(f"Nilai Minimum  : {nilai_min}\n")
    f.write(f"Nilai Maksimum : {nilai_max}\n\n")

    f.write("=== RINGKASAN DATAFRAME ===\n")
    f.write(f"Jumlah baris data : {jumlah_baris}\n")
    f.write(f"Jumlah LULUS       : {jumlah_lulus}\n")
    f.write(f"Jumlah TIDAK LULUS : {jumlah_tidak}\n")

print("Ringkasan berhasil ditulis ke ringkasan_tugas6.txt")

"""
NO 5
"""
# gradebook_demo.py
import numpy as np
import pandas as pd

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        """Menghitung rata-rata kolom nilai"""
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase mahasiswa yang lulus"""
        total = len(self.df)
        if total == 0:
            return 0.0
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100

    def save_summary(self, path: str):
        """Menyimpan ringkasan ke file teks"""
        total = len(self.df)
        avg = self.average()
        lulus = (self.df["nilai"] >= 70).sum()
        tidak = total - lulus
        pass_rate = self.pass_rate()

        with open(path, "a") as f:  # pakai append biar bisa gabung ke file sebelumnya
            f.write("\n=== RINGKASAN GRADEBOOK ===\n")
            f.write(f"Jumlah data       : {total}\n")
            f.write(f"Rata-rata nilai   : {avg:.2f}\n")
            f.write(f"Jumlah LULUS      : {lulus}\n")
            f.write(f"Jumlah TIDAK LULUS: {tidak}\n")
            f.write(f"Persentase LULUS  : {pass_rate:.2f}%\n")

    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average():.2f})"


# DEMO
if __name__ == "__main__":
    np.random.seed(42)
    nilai = np.random.randint(50, 101, size=5)

    data = {
        "nama": ["Budi", "Ani", "Citra", "Dewi", "Eko"],
        "nim": ["A001", "A002", "A003", "A004", "A005"],
        "nilai": nilai
    }
    df = pd.DataFrame(data)
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

    # Buat objek GradeBook
    gb = GradeBook(df)

    print("=== DEMO GRADEBOOK ===")
    print(df)
    print(gb)
    print("Rata-rata nilai :", gb.average())
    print("Persentase lulus:", gb.pass_rate(), "%")

    # Simpan ringkasan ke file
    gb.save_summary("ringkasan_tugas6.txt")
    print("Ringkasan GradeBook ditambahkan ke ringkasan_tugas6.txt")

"""
NO 6
"""
import numpy as np
import pandas as pd


# CLASS GRADEBOOK
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        """Menghitung rata-rata kolom nilai"""
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        """Menghitung persentase mahasiswa yang lulus"""
        total = len(self.df)
        if total == 0:
            return 0.0
        lulus = (self.df["nilai"] >= threshold).sum()
        return (lulus / total) * 100

    def save_summary(self, path: str):
        """Menyimpan ringkasan ke file teks"""
        total = len(self.df)
        avg = self.average()
        lulus = (self.df["nilai"] >= 70).sum()
        tidak = total - lulus
        pass_rate = self.pass_rate()

        with open(path, "a") as f:  # append mode
            f.write("\n=== RINGKASAN GRADEBOOK ===\n")
            f.write(f"Jumlah data       : {total}\n")
            f.write(f"Rata-rata nilai   : {avg:.2f}\n")
            f.write(f"Jumlah LULUS      : {lulus}\n")
            f.write(f"Jumlah TIDAK LULUS: {tidak}\n")
            f.write(f"Persentase LULUS  : {pass_rate:.2f}%\n")

    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average():.2f})"

# DEMO
if __name__ == "__main__":
    np.random.seed(42)

    # NUMPY
    print("=== NUMPY ===")
    nilai_array = np.random.randint(50, 101, size=10)  # 10 nilai ujian
    print("Data nilai:", nilai_array)
    print("Rata-rata :", np.mean(nilai_array))
    print("Median    :", np.median(nilai_array))
    print("Std Dev   :", np.std(nilai_array))
    print("Nilai min :", np.min(nilai_array))
    print("Nilai max :", np.max(nilai_array))

    # PANDAS
    print("\n=== PANDAS ===")
    data = {
        "nama": ["Budi", "Ani", "Citra", "Dewi", "Eko"],
        "nim": ["A001", "A002", "A003", "A004", "A005"],
        "nilai": nilai_array[:5]  # ambil 5 nilai pertama
    }
    df = pd.DataFrame(data)
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")
    print(df.head())

    # OOP: GRADEBOOK
    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print("Rata-rata nilai :", gb.average())
    print("Persentase lulus:", gb.pass_rate(), "%")

    gb.save_summary("ringkasan_tugas6.txt")
    print("Ringkasan disimpan ke ringkasan_tugas6.txt")


