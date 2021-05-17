import os


global manajemen_barang
global pencatatan_pesanan


def menu_pesanan():
    print("Menu Pencatatan Pesanan")
    print("1. Tambah Pesanan")
    print("2. Edit Pesanan")
    print("3. Cancel Pesanan")
    print("4. Terima Pesanan")
    print("5. Exit")
    menu_pesanan_in = input("Pilih Aksi : ")


def menu_barang():
    print("Menu Manajemen Barang")
    print("1. Edit Stok")
    print("2. Cari Barang")
    print("3. Exit")
    menu_barang_in = input("Pilih Aksi : ")


if __name__ == '__main__':
    manage_barang = manajemen_barang()
    catat_pesanan = pencatatan_pesanan()
    while True:
        print("Aplikasi Manajemen Gudang Supermarket")
        print("1. Pencatatan Pesanan")
        print("2. Manajemen Barang")
        print("3. Exit")
        main_in = input("Pilih Aksi : ")
        os.system("cls" if os.name == "nt" else "clear")
        if main_in == "1":
            menu_pesanan()
        elif main_in == "2":
            menu_barang()
        elif main_in == "3":
            exit(0)
        else:
            print("Input Invalid")
