from digital_library import Library

def main():
    library = Library()
    
    while True:
        print("========== Menu Perpustakaan Digital ==========")
        print("1. Tambah Buku")
        print("2. Cek Data Buku")
        print("3. Update Judul Buku")
        print("4. Update Tahun Terbit Buku")
        print("5. Update Jumlah Buku")
        print("6. Pinjam Buku")
        print("7. Kembalikan Buku")
        print("8. Cek Buku yang Sedang Dipinjam")
        print("9. Keluar")
        print("===============================================")
        
        try:
            menu = int(input("Masukkan nomor menu yang diinginkan: "))
        except:
            print("Input tidak valid. Masukkan nomor menu yang diinginkan (1-9)")
            continue
        
        if menu == 1:
            print("===== Tambah Buku =====")
            judul = input("Judul buku: ")
            tahun = input("Tahun terbit: ")
            jumlah = input("Jumlah tersedia: ")
            library.tambah_buku(judul, tahun, jumlah)
            print("Buku berhasil ditambahkan")
        
        elif menu == 2:
            print("===== Cek Data Buku =====")
            library.check_data_buku()
        
        elif menu == 3:
            print("===== Update Judul Buku =====")
            judul = input("Judul buku yang ingin diperbarui: ")
            judul_baru = input("Judul baru: ")
            library.update_judul(judul, judul_baru)
        
        elif menu == 4:
            print("===== Update Tahun Terbit Buku =====")
            judul = input("Judul buku yang ingin diperbarui: ")
            tahun_baru = input("Tahun terbit baru: ")
            library.update_tahun(judul, tahun_baru)
        
        elif menu == 5:
            print("===== Update Jumlah Buku =====")
            judul = input("Judul buku yang ingin diperbarui: ")
            jumlah_baru = input("Jumlah buku baru: ")
            library.update_jumlah(judul, jumlah_baru)
        
        elif menu == 6:
            print("===== Pinjam Buku =====")
            judul = input("Judul buku yang ingin dipinjam: ")
            nama_peminjam = input("Nama peminjam: ")
            library.pinjam_buku(judul, nama_peminjam)
            print("Buku berhasil dipinjam")
        
        elif menu == 7:
            print("===== Kembalikan Buku =====")
            judul = input("Judul buku yang ingin dikembalikan: ")
            nama_peminjam = input("Nama peminjam: ")
            library.kembali_buku(judul, nama_peminjam)
            print("Buku berhasil dikembalikan")
        
        elif menu == 8:
            print("===== Cek Buku yang Sedang Dipinjam =====")
            library.check_buku_dipinjam()
        
        elif menu == 9:
            print("Keluar dari program")
            break
        
        else:
            print("Input tidak valid. Masukkan nomor menu yang diinginkan (1-9)")

if __name__ == "__main__":
    main()
