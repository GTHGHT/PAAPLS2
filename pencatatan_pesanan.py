import numpy as np
import pandas as pd

class PencatatanPesanan:

    def __init__(self):
        csv_path = "data/pesanan.csv"
        try:
            self.pesanan_df = pd.read_csv(csv_path)
        except FileNotFoundError:
            with open(csv_path, "w") as pesanan_csv:
                pesanan_csv.write("ID Pesanan,Tanggal Pesan,Tanggal Terima,Status\n")
            self.pesanan_df = pd.read_csv(csv_path)

        try:
            df_by_id = self.pesanan_df.groupby("ID Pesanan")
            barang_pesanan_list = (pd.read_csv(f"data/{id_}.csv" for id_, _ in df_by_id))
            self.barang_pesanan_df = pd.concat(barang_pesanan_list, ignore_index=True)
        except FileNotFoundError:
            raise FileNotFoundError

