# Latihan List
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
