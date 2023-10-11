def tambah_buku(buku, judul, akun_aktif):
    if akun_aktif and akun_aktif['tipe'] == 'admin':
        buku_baru = {'judul': judul, 'dipinjam': False}
        buku.append(buku_baru)
        print(f"Buku '{judul}' telah ditambahkan.")
    else:
        print("Hanya admin yang dapat menambahkan buku.")
    return buku


def pinjam_buku(buku, judul, akun_aktif):
    if akun_aktif and akun_aktif['tipe'] == 'user':
        for buku in buku:
            if buku['judul'] == judul and not buku['dipinjam']:
                buku['dipinjam'] = True
                print(
                    f"Buku '{judul}' telah dipinjam oleh {akun_aktif['nama']}.")
                return
        print("Buku tidak tersedia.")
    else:
        print("Hanya user yang dapat meminjam buku.")


def kembalikan_buku(buku, judul, akun_aktif):
    if akun_aktif and akun_aktif['tipe'] == 'user':
        for buku in buku:
            if buku['judul'] == judul and buku['dipinjam']:
                buku['dipinjam'] = False
                print(
                    f"Buku '{judul}' telah dikembalikan oleh {akun_aktif['nama']}.")
                return
        print("Buku tidak dapat dikembalikan.")
    else:
        print("Hanya user yang dapat mengembalikan buku.")


def tambah_akun(akun, nama, tipe):
    akun_baru = {'nama': nama, 'tipe': tipe}
    akun.append(akun_baru)
    print(f"Akun {tipe} '{nama}' telah ditambahkan.")
    return akun


def login_akun(akun, nama):
    for ak in akun:
        if ak['nama'] == nama:
            print(f"Akun '{nama}' telah login.")
            return ak
    print("Akun tidak ditemukan.")


def keluar_akun():
    print("Akun telah logout.")


buku = []
akun = []
akun_aktif = None

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Pinjam Buku")
    print("3. Kembalikan Buku")
    print("4. Tambah Akun")
    print("5. Login Akun")
    print("6. Keluar Akun")
    print("7. Keluar")

    pilihan = input("\nMasukkan pilihan Anda: ")

    if pilihan == '1':
        judul = input("\nMasukkan judul buku: ")
        buku = tambah_buku(buku, judul, akun_aktif)
    elif pilihan == '2':
        judul = input("\nMasukkan judul buku: ")
        pinjam_buku(buku, judul, akun_aktif)
    elif pilihan == '3':
        judul = input("\nMasukkan judul buku: ")
        kembalikan_buku(buku, judul, akun_aktif)
    elif pilihan == '4':
        nama = input("\nMasukkan nama akun: ")
        tipe = input("Masukkan tipe akun (admin/user): ")
        akun = tambah_akun(akun, nama, tipe)
    elif pilihan == '5':
        nama = input("\nMasukkan nama akun: ")
        akun_aktif = login_akun(akun, nama)
    elif pilihan == '6':
        keluar_akun()
        akun_aktif = None
    elif pilihan == '7':
        break
