import pandas as pd

class CSVReader:
    def __init__(self, path):
        self.df = pd.read_csv(path)

    def get_transactions(self, columns):
        # Return a list of transaction from one column, if multiple columns specified then concatenate them
        if len(columns) == 1:
            return self.df[columns[0]].tolist()
        elif len(columns) > 1:
            return self.df[columns].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1).tolist()
        else:
            print("No columns specified")
            return []
        