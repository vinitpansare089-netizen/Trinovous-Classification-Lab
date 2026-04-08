import pandas as pd

def load_data(path):
    print("Data is being loaded...")
    df = pd.read_csv(path)
    print("Data is loaded")

    return df
