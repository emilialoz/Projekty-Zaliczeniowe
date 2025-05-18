# dataset_utils.py

import pandas as pd
import random
import sys


class Dataset:
    def __init__(self):
        self.headers = []
        self.data = []
        self.train_set = []
        self.test_set = []
        self.validation_set = []

    def load_data(self, filepath, has_header=True):
        try:
            df = pd.read_csv(filepath)
            if has_header:
                self.headers = df.columns.tolist()
            else:
                self.headers = []
            self.data = df.values.tolist()

            print(f"Loading data successful. Total number of rows is: {len(self.data)}")

        except Exception as e:
            print(f"Error loading CSV data: {e}")

    def print_headers(self):
        if self.headers:
            print("Column labels:", self.headers)
        else:
            print("Column labels not found.")

    def print_data(self, start=None, end=None):
        if not self.data:
            print("No data.")
            return

        subset = self.data[start:end] if start is not None and end is not None else self.data
        for row in subset:
            print(row)

    def split_data(self, train_percent, test_percent, val_percent):
        if not self.data:
            print("No data to split.")
            return

        if (train_percent + test_percent + val_percent) != 100:
            print("The sum of the percentages must be 100.")
            return

        total_len = len(self.data)
        data_copy = self.data[:]
        random.shuffle(data_copy)

        train_size = int(total_len * train_percent / 100)
        test_size = int(total_len * test_percent / 100)

        self.train_set = data_copy[:train_size]
        self.test_set = data_copy[train_size:train_size + test_size]
        self.validation_set = data_copy[train_size + test_size:]

        print("Split completed:")
        print(f"- Training set: {len(self.train_set)}")
        print(f"- Test set: {len(self.test_set)}")
        print(f"- Validation set: {len(self.validation_set)}")

    def class_counts(self, class_index=-1):
        counter = {}
        for row in self.data:
            key = row[class_index]
            counter[key] = counter.get(key, 0) + 1
        print("Class distribution:")
        for k, v in counter.items():
            print(f"{k}: {v}")

    def filter_by_class(self, class_value, class_index=-1):
        filtered = [row for row in self.data if row[class_index] == class_value]
        print(f" Rows with class '{class_value}':")
        for row in filtered:
            print(row)

    def save_to_csv(self, data_subset, filename):
        df = pd.DataFrame(data_subset, columns=self.headers if self.headers else None)
        df.to_csv(filename, index=False)
        print(f"Data saved to file: {filename}")


if __name__ == "__main__":
    ds = Dataset()

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "files/iris_data.csv"

    ds.load_data(filepath, has_header=True)
    ds.print_headers()
    ds.print_data(0, 5)
    ds.split_data(70, 15, 15)
    ds.class_counts(class_index=-1)
    ds.filter_by_class("Iris-setosa", class_index=-1)
    ds.save_to_csv(ds.train_set, "iris_train.csv")
