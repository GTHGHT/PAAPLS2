import datetime
import os

import numpy as np
import pandas as pd


class PencatatanPesanan:

    def __init__(self):
        self.PESANAN_COLUMN = ["ID_Pesanan", "Tanggal_Pesan", "Tanggal_Terima", "Status"]
        self.BARANG_PESANAN_COLUMN = ["ID_Pesanan", "Barcode", "Nama_Barang", "Jumlah_Barang", "Expired"]

        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('expand_frame_repr', False)
        self.load_csv()
        self.pesanan_df.columns = self.pesanan_df.columns.str.strip()
        self.barang_pesanan_df.columns = self.barang_pesanan_df.columns.str.strip()

    def load_csv(self):
        csv_path = "data/pesanan.csv"
        try:
            self.pesanan_df = pd.read_csv(csv_path)
        except FileNotFoundError:
            with open(csv_path, "w") as pesanan_csv:
                pesanan_csv.write("ID_Pesanan,Tanggal_Pesan,Tanggal_Terima,Status\n")
            self.pesanan_df = pd.read_csv(csv_path, index_col="ID_Pesanan")

        self.char_increment = "A"
        self.num_increment = 0

        try:
            df_by_id = self.pesanan_df.groupby("ID_Pesanan")
            if len(self.pesanan_df) > 0:
                barang_pesanan_list = list()
                for id_, _ in df_by_id:
                    barang_pesanan_list.append(pd.read_csv(f"data/pesanan/{id_}.csv", index_col=[0,1]))
                    if id_[0] > self.char_increment:
                        self.char_increment = id_[0]
                    if int(id_[1:]) > self.num_increment:
                        self.num_increment = int(id_[1:])
                    self.barang_pesanan_df = pd.concat(barang_pesanan_list)
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
        barang_df = pd.DataFrame(list_barang, columns=self.BARANG_PESANAN_COLUMN[1:])
        id_pesanan = self.get_id()
        barang_df.insert(0,"ID_Pesanan", id_pesanan)
        barang_df.set_index("ID_Pesanan")
        barang_df.to_csv(f"data/pesanan/{id_pesanan}.csv", index=False)
        new_pesanan_df = pd.DataFrame(
            [[id_pesanan, str(datetime.date.today()), "", "Belum Diterima"]],
            columns=self.PESANAN_COLUMN)
        self.pesanan_df = self.pesanan_df.append(new_pesanan_df, ignore_index=True)
        self.pesanan_df.to_csv("data/pesanan.csv", index=False)
        self.load_csv()
        return id_pesanan

    def delete_pesanan(self, id_pesanan):
        if id_pesanan in self.pesanan_df["ID_Pesanan"].values:
            self.pesanan_df = self.pesanan_df[self.pesanan_df.ID_Pesanan != id_pesanan]
            self.pesanan_df.to_csv("data/pesanan.csv",index=False)
            self.barang_pesanan_df = self.barang_pesanan_df.drop(index=id_pesanan, level=0)
            os.remove(f"data/pesanan/{id_pesanan}.csv")
            self.load_csv()
            return True
        else:
            return False

    def edit_pesanan(self, id_pesanan):
        pass

    def print_pesanan(self):
        print(self.barang_pesanan_df)
