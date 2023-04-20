import pandas as pd

class Library():
    """
    Program Digital Library

    A program that simulates a digital library with the following functionalities:
        - Add book to library
        - Update book data (title, year, quantity)
        - Check available books
        - Check borrowed books
        - Borrow book
        - Return book

    The program uses a pandas DataFrame to display the book data in a table format.

    Author: dani.herdiana.230885@gmail.com

    Classes:
        Library:
            A class that represents a digital library.

    Methods:
        __init__(self)
            Constructs a new Library object.

        tambah_buku(self, judul, tahun, jumlah)
            Adds a new book to the library.

        check_data_buku(self)
            Displays a table of available books in the library.

        update_judul(self, judul, judul_baru)
            Updates the title of a book in the library.

        update_tahun(self, judul, tahun_baru)
            Updates the year of publication of a book in the library.

        update_jumlah(self, judul, jumlah_baru)
            Updates the quantity of a book in the library.

        return_index(self, judul)
            Returns the index of a book in the data_buku list.

        return_index_buku(self, judul, nama_peminjam)
            Returns the index of a borrowed book in the buku_dipinjam list.

        check_buku_dipinjam(self)
            Displays a table of borrowed books in the library.

        pinjam_buku(self, judul, nama_peminjam)
            Allows a user to borrow a book from the library.

        kembali_buku(self, judul, nama_peminjam)
            Allows a user to return a borrowed book to the library.
    """

    def __init__(self):
        """
        Initialize a Library object with empty data_buku and buku_dipinjam lists.
        """
        self.data_buku = []
        self.buku_dipinjam = []
    
    def tambah_buku(self, judul, tahun, jumlah):
        """
        Add a new book to the library.

        Parameters:
        judul (str): The title of the book.
        tahun (int): The year the book was published.
        jumlah (int): The number of copies available in the library.
        """
        self.data_buku.append([judul, tahun, jumlah])
    
    def check_data_buku(self):
        """
        Display the list of books available in the library.

        If there are no books in the library, print "Tidak Ada Buku di Perpustakaan".
        """
        if(len(self.data_buku)==0):
            print('Tidak Ada Buku di Perpustakaan')
        else:
            data = pd.DataFrame((self.data_buku))
            data.columns = ['Judul', 'Tahun Terbit', 'Jumlah Tersedia']
            print(data.to_markdown())
    
    def update_judul(self, judul, judul_baru):
        """
        Update the title of a book in the library.

        Parameters:
        judul (str): The current title of the book.
        judul_baru (str): The new title of the book.

        If the book cannot be found in the library, print "Buku Tidak Ditemukan".
        """
        try:
            self.data_buku[self.return_index(judul)][0] = tahun_baru
            print('Data Judul Berhasil Diperbarui')
        except:
            print('Buku Tidak Ditemukan')

    def update_tahun(self, judul, tahun_baru):
        """
        Update the publication year of a book in the library.

        Parameters:
        judul (str): The title of the book.
        tahun_baru (int): The new publication year of the book.

        If the book cannot be found in the library, print "Buku Tidak Ditemukan".
        """
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