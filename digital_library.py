import pandas as pd

class Library():
    def __init__(self):
        self.data_buku = []
        self.buku_dipinjam = []
    
    def tambah_buku(self, judul, tahun, jumlah):
        self.data_buku.append([judul, tahun, jumlah])
    
    def check_data_buku(self):
        if(len(self.data_buku)==0):
            print('Tidak Ada Buku di Perpustakaan')
        else:
            data = pd.DataFrame((self.data_buku))
            data.columns = ['Judul', 'Tahun Terbit', 'Jumlah Tersedia']
            print(data.to_markdown())
    
    def update_judul(self, judul, judul_baru):
        try:
            self.data_buku[self.return_index(judul)][0] = tahun_baru
            print('Data Judul Berhasil Diperbarui')
        except:
            print('Buku Tidak Ditemukan')

    def update_tahun(self, judul, tahun_baru):
        try:
            self.data_buku[self.return_index(judul)][1] = tahun_baru
            print('Data Tahun Terbit Berhasil Diperbarui')
        except:
            print('Buku Tidak Ditemukan')

    def update_jumlah(self, judul, jumlah_baru):
        try:
            self.data_buku[self.return_index(judul)][2] = jumlah_baru
            print('Data Jumlah Buku Berhasil Diperbarui')
        except:
            print('Buku Tidak Ditemukan')

    def return_index(self, judul):
        for i in range(len(self.data_buku)):
            if self.data_buku[i][0] == judul:
                return i

    def return_index_buku(self, judul, nama_peminjam):
        for i in range(len(self.buku_dipinjam)):
            if self.buku_dipinjam[i][0] == judul and self.buku_dipinjam[i][1] == nama_peminjam:
                return i

    def check_buku_dipinjam(self):
        if(len(self.buku_dipinjam)==0):
            print('Tidak Ada Buku yang sedang dipinjam')
        else:
            data = pd.DataFrame((self.buku_dipinjam))
            data.columns = ['Judul', 'Nama Peminjam']
            print(data.to_markdown())

    def pinjam_buku(self, judul, nama_peminjam):
        try:    
            # mengurangi jumlah buku di data_buku
            self.data_buku[self.return_index(judul)][2] -= 1
            # menambah data di buku_dipinjam
            self.buku_dipinjam.append([judul, nama_peminjam])
        except:
            print('Buku Tidak Ditemukan')

    def kembali_buku(self, judul, nama_peminjam):
        # menghapus data peminjaman di buku_dipinjam
        self.buku_dipinjam.pop(self.return_index_buku(judul, nama_peminjam))
        # menambah data jumlah di data_buku
        self.data_buku[self.return_index(judul)][2] += 1