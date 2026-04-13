from src.data_loader import load_data
from src.preprocessing import (
    encode_data,
    feature_engineering,
    split_features,
    split_data,
    scale_data
)

def run_pipeline(df):

    df = load_data("data/raw/dataset.csv")

    df = encode_data(df)
    df = feature_engineering(df)

    X, y = split_features(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train, X_test = scale_data(X_train, X_test)

    return X_train, X_test, y_train, y_test








