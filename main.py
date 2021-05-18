import os
from manajemen_barang import ManajemenBarang
from pencatatan_pesanan import PencatatanPesanan

manage_barang = ManajemenBarang()
catat_pesanan = PencatatanPesanan()


def menu_pesanan():
    global catat_pesanan
    catat_pesanan.print_pesanan()
    print("Menu Pencatatan Pesanan")
    print("1. Tambah Pesanan")
    print("2. Edit Pesanan")
    print("3. Cancel Pesanan")
    print("4. Terima Pesanan")
    print("5. Exit")
    menu_pesanan_in = input("Pilih Aksi : ")
    if menu_pesanan_in == "1":
        jenis_barang = int(input(f"{'Masukkan Jumlah Jenis Barang': <30} = "))
        if jenis_barang > 0:
            daftar_barang = list()
            for i in range(jenis_barang):
                print()
                print(f"Barang ke-{i + 1}")
                print(f"{'':-<50}")
                barcode = input(f"{'Masukkan Barcode': <30} = ")
                nama = input(f"{'Masukkan Nama Barang': <30} = ")
                jumlah = int(input(f"{'Masukkan Jumlah Barang': <30} = "))
                daftar_barang.append([barcode, nama, jumlah, ""])
            po_id = catat_pesanan.add_pesanan(daftar_barang)
            print("\nPenambahan Preorder Berhasil")
            print(f"ID Preorder = {po_id}")
        else:
            print("\nPenambahan Preorder Gagal")


def menu_barang():
    print("Menu Manajemen Barang")
    print("1. Edit Stok")
    print("2. Cari Barang")
    print("3. Exit")
    menu_barang_in = input("Pilih Aksi : ")


if __name__ == '__main__':
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
