import os


global manajemen_barang
global pencatatan_pesanan


def menu_pesanan():
    pass


def menu_barang():
    pass

if __name__ == '__main__':
    while True:
        print("Aplikasi Manajemen Gudang Supermarket")
        print("1. Pencatatan Pesanan")
        print("2. Manajemen Barang")
        print("3. Exit")
        main_in = input("Pilih Aksi : ")
        if main_in == "1":
            pass
        elif main_in == "2":
            pass
        elif main_in == "3":
            exit(0)
        else:
            print("Input Invalid")
            os.system("cls" if os.name == "nt" else "clear")