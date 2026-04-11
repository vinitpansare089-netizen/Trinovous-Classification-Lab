import pandas as pd

def preprocess_data(df):

    #convert categorical into binary/boolean
    df = pd.get_dummies(df, drop_first=True)

