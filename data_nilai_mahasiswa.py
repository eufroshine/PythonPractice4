# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.35 * uts + 0.35 * uas
    return nilai_akhir

# Inisialisasi list untuk menyimpan data
data_mahasiswa = []

# Perulangan untuk memasukkan data
while True:
    # Meminta input data dari pengguna
    nama = input("Masukkan Nama Mahasiswa: ")
    nim = int(input("Masukan NIM: "))
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))

    # Menghitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    # Menambahkan data ke dalam list
    data_mahasiswa.append({
        'Nama': nama,
        'NIM' : nim,
        'Tugas': tugas,
        'UTS': uts,
        'UAS': uas,
        'Nilai Akhir': nilai_akhir
    })

    # Menanyakan apakah ingin menambahkan data lagi
    tambah_data = input("Tambah data lagi? (y/t): ")
    if tambah_data.lower() != 'y':
        break

# Menampilkan daftar data
print("\nDaftar Nilai Mahasiswa:")
print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<15}".format("Nama", "NIM", "Tugas", "UTS", "UAS", "Nilai Akhir"))
for data in data_mahasiswa:
    print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<15}".format(
        data['Nama'], data['NIM'], data['Tugas'], data['UTS'], data['UAS'], data['Nilai Akhir']
    ))
