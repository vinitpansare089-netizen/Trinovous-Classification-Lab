from src.data_loader import load_data
from src.preprocessing import (
    encode_data,
    feature_engineering,
    split_features,
    split_data,
    scale_data
)
from src.model import train_logistic
from src.evaluate import evaluate_model
def pipeline():

    df = load_data("data/raw/dataset.csv")

    df = encode_data(df)

    df = feature_engineering(df)

    X, y = split_features(df)

    X_train, X_test, y_train, y_test = split_data(X, y)

    X_train, X_test = scale_data(X_train, X_test)

    model = train_logistic(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    return model











