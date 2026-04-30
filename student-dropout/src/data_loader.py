import pandas as pd

def load_data(path):
    try:
        print("data is loading captain...")
        df = pd.read_csv(path)
        print("Data loaded captain...")
        return df
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Invalid File captain{e}")
