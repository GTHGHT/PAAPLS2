import numpy as np
import pandas as pd

class ManajemenBarang:
    def __init__(self):
        csv_path = "data/barang.csv"
        try:
            self.data = pd.read_csv(csv_path)
        except FileNotFoundError:
            with open(csv_path, "w") as barang:
                barang.write("Barcode,Nama Barang,Stok")
            self.data = pd.read_csv(csv_path)

    def print_data(self):
        print(self.data)


if __name__ == '__main__':
    ManajemenBarang().print_data()