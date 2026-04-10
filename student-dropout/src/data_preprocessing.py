import pandas as pd

def load_data(path):
    try:
        print("data is loaded captain...")
        df = pd.read_csv(path)
        print("Data loaded captain...")
        return df
    except FileNotFoundError as e:
        return f'Invalid file {e}'

