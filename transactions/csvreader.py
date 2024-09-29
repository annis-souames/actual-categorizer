import pandas as pd

class CSVReader:
    def __init__(self, path):
        self.path = path

    def read(self):
        return pd.read_csv(self.path)