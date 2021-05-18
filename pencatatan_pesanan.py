import datetime

import numpy as np
import pandas as pd


class PencatatanPesanan:

    def __init__(self):
        self.PESANAN_COLUMN = ["ID Pesanan", "Tanggal Pesan", "Tanggal Terima", "Status"]
        self.BARANG_PESANAN_COLUMN = ["Barcode", "Nama Barang", "Jumlah Barang", "Expired"]
        csv_path = "data/pesanan.csv"
        try:
            self.pesanan_df = pd.read_csv(csv_path)
        except FileNotFoundError:
            with open(csv_path, "w") as pesanan_csv:
                pesanan_csv.write("ID Pesanan,Tanggal Pesan,Tanggal Terima,Status\n")
            self.pesanan_df = pd.read_csv(csv_path)

        self.char_increment = "A"
        self.num_increment = 0

        try:
            df_by_id = self.pesanan_df.groupby("ID Pesanan")
            if len(self.pesanan_df)>0:
                barang_pesanan_list = list()
                for id_, _ in df_by_id:
                    barang_pesanan_list.append(pd.read_csv(f"data/pesanan/{id_}.csv"))
                    if id_[0] > self.char_increment:
                        self.char_increment = id_[0]
                    if int(id_[1:]) > self.num_increment:
                        self.num_increment = int(id_[1:])
                self.barang_pesanan_df = pd.concat(barang_pesanan_list, ignore_index=True)
            else:
                self.barang_pesanan_df = pd.DataFrame([], columns=self.BARANG_PESANAN_COLUMN)
        except FileNotFoundError:
            raise FileNotFoundError

    def get_id(self):
        self.num_increment += 1
        if self.num_increment == 10000:
            self.char_increment = chr(ord(self.char_increment) + 1)
            self.num_increment = 1
        return f"{self.char_increment}{self.num_increment:0>4}"

    def add_pesanan(self, list_barang):
        barang_df = pd.DataFrame(list_barang, columns=self.BARANG_PESANAN_COLUMN)
        id_pesanan = self.get_id()
        barang_df.to_csv(f"data/pesanan/{id_pesanan}.csv")
        new_pesanan_df = pd.DataFrame([[id_pesanan, str(datetime.date.today()), "", "Belum Diterima"]],columns=self.PESANAN_COLUMN)
        self.pesanan_df.append(new_pesanan_df, ignore_index=True)
        self.pesanan_df.to_csv("data/pesanan.csv")
        return id_pesanan

    def print_pesanan(self):
        print(self.pesanan_df)
        print(self.barang_pesanan_df)


