
# 🧩 Praktikum 4 – List (Bahasa Pemrograman)

## 📘 Deskripsi
Modul ini membahas tentang penggunaan **List** pada Python — mulai dari membuat, mengakses, mengubah, menambah, menggabungkan list, hingga membuat program untuk menambahkan data mahasiswa menggunakan list dan perulangan.

---

## 💻 Kode Program Lengkap
```python
# =============================
# LATIHAN LIST
# =============================

# 1. Buat sebuah list sebanyak 5 elemen
A = [10, 20, 30, 40, 50]
print("List A:", A)

# 2. Akses list
print("Elemen ke-3:", A[2])
print("Elemen ke-2 sampai ke-4:", A[1:4])
print("Elemen terakhir:", A[-1])

# 3. Ubah elemen list
A[3] = 99  # ubah elemen ke-4
print("Setelah ubah elemen ke-4:", A)

A[3:] = [70, 80]  # ubah elemen ke-4 sampai terakhir
print("Setelah ubah elemen ke-4 sampai terakhir:", A)

# 4. Tambah elemen list
B = A[:2]  # ambil 2 bagian dari list pertama
print("List B (2 elemen dari A):", B)

B.append("Python")  # tambah string
print("Setelah tambah string:", B)

B.extend([60, 70, 80])  # tambah 3 nilai
print("Setelah tambah 3 nilai:", B)

# 5. Gabungkan list B dengan list A
C = B + A
print("Gabungan list B + A:", C)


# =============================
# TUGAS PRAKTIKUM
# =============================

data_mahasiswa = []

while True:
    print("\nMasukkan data mahasiswa")
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa.append({
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Nilai Akhir": akhir
    })

    lanjut = input("Tambah data lagi? (y/t): ")
    if lanjut.lower() == 't':
        break

print("\nDaftar Data Mahasiswa")
print("=" * 70)
print(f"{'No':<4}{'Nama':<15}{'NIM':<10}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Akhir':<10}")
print("=" * 70)

for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"{i:<4}{mhs['Nama']:<15}{mhs['NIM']:<10}{mhs['Tugas']:<10}{mhs['UTS']:<10}{mhs['UAS']:<10}{mhs['Nilai Akhir']:<10.2f}")

print("=" * 70)
````

---

## 🧮 Contoh Output Program

```
List A: [10, 20, 30, 40, 50]
Elemen ke-3: 30
Elemen ke-2 sampai ke-4: [20, 30, 40]
Elemen terakhir: 50
Setelah ubah elemen ke-4: [10, 20, 30, 99, 50]
Setelah ubah elemen ke-4 sampai terakhir: [10, 20, 30, 70, 80]
List B (2 elemen dari A): [10, 20]
Setelah tambah string: [10, 20, 'Python']
Setelah tambah 3 nilai: [10, 20, 'Python', 60, 70, 80]
Gabungan list B + A: [10, 20, 'Python', 60, 70, 80, 10, 20, 30, 70, 80]

Masukkan data mahasiswa
Nama: Budi
NIM: 123
Nilai Tugas: 80
Nilai UTS: 85
Nilai UAS: 90
Tambah data lagi? (y/t): t

Daftar Data Mahasiswa
======================================================================
No  Nama           NIM       Tugas     UTS       UAS       Akhir     
======================================================================
1   Budi           123       80.0      85.0      90.0      85.75     
======================================================================
```

---

## 🧭 Flowchart Program

```
┌────────────────────────────┐
│ Mulai                     │
└────────────┬───────────────┘
             │
             ▼
   ┌───────────────────┐
   │ Inisialisasi list │
   │ data_mahasiswa=[] │
   └─────────┬─────────┘
             │
             ▼
 ┌────────────────────────────┐
 │ Input data: Nama, NIM,     │
 │ Tugas, UTS, UAS            │
 └───────────┬────────────────┘
             │
             ▼
 ┌────────────────────────────┐
 │ Hitung nilai akhir:        │
 │ (tugas*0.3)+(uts*0.35)+(uas*0.35) │
 └───────────┬────────────────┘
             │
             ▼
 ┌────────────────────────────┐
 │ Simpan data ke list        │
 └───────────┬────────────────┘
             │
             ▼
 ┌────────────────────────────┐
 │ Tambah data lagi (y/t)?    │
 └───────┬────────────┬───────┘
         │y            │t
         ▼             ▼
    Kembali ke input   Tampilkan seluruh data
                       │
                       ▼
                ┌──────────────┐
                │ Selesai       │
                └──────────────┘
```

---

