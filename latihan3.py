def hitung_nilai_akhir(nilai):
    return (nilai['UTS'] + nilai['UAS']) / 2

def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        data_nilai_akhir[nama] = hitung_nilai_akhir(nilai)
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print(f"Nama: {nama}\tNilai Akhir: {nilai_akhir:.2f}")

def main():
    data_mahasiswa = {
        'Budi': {'UTS': 85, 'UAS': 95},
        'Ani': {'UTS': 80, 'UAS': 80},
        'Siti': {'UTS': 90, 'UAS': 90}
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
