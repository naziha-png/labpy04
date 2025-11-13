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
