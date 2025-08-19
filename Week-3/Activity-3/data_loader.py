# Week-3 Activity-3
import pandas as pd
import os
import numpy as np

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.data = pd.DataFrame()

    def check_file(self):
        if os.path.exists(self.filename):
            print(f" File '{self.filename}' found.")
        else:
            print(f" File '{self.filename}' does not exist.")
        return True

    def load_data(self):
        self.data = pd.read_csv(self.filename)
        self.data = self.data.iloc[:, 0]
        print (self.data.head(20))
        print("Data loaded successfully.")

    def max_data(self):
        max_values = self.data.max()
        print("Maximum values for each column:")
        print(max_values)

    def min_data(self):
        min_values = self.data.min()
        print("Minimum values for each column:")
        print(min_values)

    def mean_data(self):
        mean_values = np.mean(self.data, axis=0)
        print("Mean values for each column:", mean_values)

    def absolute_data(self):
        absolute_values = np.abs(self.data)
        print("Absolute values for each column:", absolute_values)

# ---------------- Main Execution ----------------
if __name__ == "__main__":
    path = "data.txt"
    processor = DataLoader(path)
    # processor.check_file()
    processor.load_data()
    processor.max_data()
    processor.min_data()
    processor.mean_data()
    processor.absolute_data()

