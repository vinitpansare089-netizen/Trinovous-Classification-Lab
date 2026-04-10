import pandas as pd

def preprocess_data(df):

    df = pd.get_dummies(df, drop_first=True)

    df = 