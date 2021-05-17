import numpy as np
import pandas as pd

class ManajemenBarang:
    def __init__(self):
        csv_path = "data/barang.csv"
        try:
            self.df = pd.read_csv(csv_path)
        except FileNotFoundError:
            with open(csv_path, "w") as barang_csv:
                barang_csv.write("Barcode,Nama Barang,Stok\n")
            self.df = pd.read_csv(csv_path)

    def print_data(self):
        print(self.df)
        df_by_barcode = self.df.groupby("Barcode")
        for barcode, barcode_df in df_by_barcode:
            filename = f"data/{barcode}.csv"
            print(filename)


if __name__ == '__main__':
    ManajemenBarang().print_data()