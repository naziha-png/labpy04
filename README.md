# Laporan Praktikum 4: List
## Praktikum 4 — Struktur Data List
**Mata Kuliah:** Pengantar Pemrograman<br>
**Nama:** Naziha Raiqi Aribino<br>
**NIM:** 312510232<br>
**Kelas:** TI.25.A2<br>
## 1. Tujuan Praktikum

Memahami konsep dasar list dalam Python.

Mampu melakukan operasi dasar pada list (akses, ubah, tambah, gabung).

Membuat program sederhana menggunakan list untuk manajemen data.

Mengimplementasikan perulangan, input, dan perhitungan nilai pada list.

# 2. Dasar Teori
**List adalah struktur data di Python yang dapat menyimpan banyak nilai sekaligus dalam satu variabel.** <br>
**Ciri-ciri list:<br>**
* Ditulis dengan tanda []<br>
* Mendukung berbagai tipe data (string, integer, float)<br>
* Bersifat mutable (bisa diubah)<br>
* Mendukung operasi slicing, penambahan elemen, penghapusan, dan penggabungan<br>
## Operasi dasar list:
* Akses elemen : list[index]<br>
* Slicing : list[start:end]<br>
* Ubah elemen : list[index] = nilai_baru<br>
* Append : list.append()<br>
* Extend : list.extend()<br>
* Gabung : listA + listB<br>
# 3. Latihan
Kode Program<br>
**1. Buat sebuah list sebanyak 5 elemen** <br>
A = [10, 20, 30, 40, 50]
print("List A:", A)
**2. Akses list** <br>
print("Elemen ke-3:", A[2])
print("Elemen ke-2 sampai ke-4:", A[1:4])
print("Elemen terakhir:", A[-1])
**3. Ubah elemen list** <br>
A[3] = 99  # ubah elemen ke-4
print("Setelah ubah elemen ke-4:", A)

A[3:] = [70, 80]  # ubah elemen ke-4 sampai terakhir
print("Setelah ubah elemen ke-4 sampai terakhir:", A)

**4. Tambah elemen list** <br>
B = A[:2]  # ambil 2 bagian dari list pertama
print("List B (2 elemen dari A):", B)

B.append("Python")  # tambah string
print("Setelah tambah string:", B)

B.extend([60, 70, 80])  # tambah 3 nilai
print("Setelah tambah 3 nilai:", B)

**5. Gabungkan list B dengan list A** <br>
C = B + A
print("Gabungan list B + A:", C)

## 4. TUGAS PRAKTIKUM
**Deskripsi Tugas**

* **Membuat program untuk:**

Input data mahasiswa sebanyak-banyaknya menggunakan perulangan.

Hitung nilai akhir = (Tugas 30%) + (UTS 35%) + (UAS 35%).

Tampilkan daftar data jika user memilih t (tidak menambah data lagi).

Flowchart Program

(Gambar dijelaskan dengan teks, bisa kamu convert ke draw.io nanti)

            ┌───────┐
            │ Mulai │
            └───┬───┘
                │
        ┌───────▼────────┐
        │ Input data mhs │
        └───────┬────────┘
                │
        ┌───────▼─────────┐
        │ Hitung Nilai    │
        └───────┬─────────┘
                │
      ┌─────────▼──────────┐
      │ Tambah ke list?     │
      │ (y/t)               │
      └───────┬────────────┘
          y   │     t
              │
     ┌────────▼───────┐
     │ Kembali input   │
     └─────────────────┘
                │
        ┌───────▼────────┐
        │ Tampilkan data │
        └───────┬────────┘
                │
            ┌───▼───┐
            │ Selesai│
            └────────┘

Kode Program
# Program menambahkan data ke dalam list

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

5. Kesimpulan

Pada praktikum ini, mahasiswa berhasil memahami:

Cara membuat dan mengelola list pada Python

Operasi dasar list termasuk akses, slicing, update, append, extend, dan penggabungan list

Implementasi list untuk manajemen data menggunakan perulangan dan struktur data dictionary

Penerapan perhitungan nilai akhir berdasarkan bobot tertentu

Program dapat digunakan untuk menyimpan banyak data mahasiswa dan menampilkannya dalam bentuk tabel.
