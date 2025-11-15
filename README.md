

# Praktikum 4 — List & Tuple
**Nama:** Naziha Raiqi Aribino  
**NIM:** 312510232  
**Kelas:** TI.25.A2

---

## 1. Tujuan Praktikum
- Memahami konsep dasar list dan tuple di Python.
- Melakukan operasi dasar list: akses, slicing, update, append, extend, delete, dan gabung.
- Membuat program pengolahan data menggunakan list.
- Menyusun flowchart dan dokumentasi praktikum.

---

## 2. Dasar Teori

### List
List adalah struktur data Python yang bersifat *mutable* (dapat diubah).  
Operasi dasar:
- Akses elemen → `a[2]`
- Slicing → `a[1:4]`
- Ubah elemen → `a[3] = 90`
- Tambah elemen → `append()`, `extend()`
- Gabung list → `a + b`
- Hapus elemen → `del`

### Tuple
Tuple adalah struktur data seperti list tetapi bersifat *immutable* (tidak bisa diubah).

---

## 3. LATIHAN

### Kode Program

```python
A = [10, 20, 30, 40, 50]
print("List A:", A)

print("Elemen ke-3:", A[2])
print("Elemen ke-2 sampai ke-4:", A[1:4])
print("Elemen terakhir:", A[-1])

A[3] = 99
print("Setelah ubah elemen ke-4:", A)

A[3:] = [70, 80]
print("Setelah ubah elemen ke-4 sampai terakhir:", A)

B = A[:2]
print("List B:", B)

B.append("Python")
B.extend([60, 70, 80])
print("List B setelah ditambah:", B)

C = B + A
print("Gabungan list B + A:", C)
````

---

## 4. Tugas Praktikum

### Deskripsi Program

Program meminta user menginput data mahasiswa sebanyak-banyaknya, lalu menghitung nilai akhir:

* Tugas: 30%
* UTS: 35%
* UAS: 35%

User memilih `y` untuk menambah data atau `t` untuk berhenti. Setelah berhenti, program menampilkan semua data mahasiswa dalam format tabel.

---

## 5. Flowchart 

```
+------------------+
|      MULAI       |
+------------------+
         |
         v
+--------------------------+
| Input Data Mahasiswa     |
+--------------------------+
         |
         v
+--------------------------+
| Hitung Nilai Akhir       |
+--------------------------+
         |
         v
+--------------------------+
| Tambah Data? (y/t)       |
+------------+-------------+
             |y
             | 
             v
   (kembali ke Input Data)
             |
             t
             v
+--------------------------+
|   Tampilkan Semua Data   |
+--------------------------+
         |
         v
+------------------+
|      SELESAI     |
+------------------+
```

---

## 6. Kode Program Tugas Praktikum

```python
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
    print(f"{i:<4}{mhs['Nama']:<15}{mhs['NIM']:<10}{mhs['Tugas']:<10}"
          f"{mhs['UTS']:<10}{mhs['UAS']:<10}{mhs['Nilai Akhir']:<10.2f}")

print("=" * 70)
```

---

## 7. Kesimpulan  

Dari Praktikum ini, bisa disimpulkan bahwa:  

* List adalah struktur data fleksibel yang dapat diubah-ubah.
* Program dapat menyimpan banyak data menggunakan list of dictionary.
* Flowchart membantu memahami alur program sebelum coding.
* Penggunaan perulangan dan input sangat penting dalam pengolahan data dinamis.

---

