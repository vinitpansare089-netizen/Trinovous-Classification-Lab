import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.preprocessing import StandardScaler

def encode_data(df):
    df = pd.get_dummies(df, drop_first=True)
    return df

def feature_engineering(df):

    
    df["high_absence"] = df["absences"].apply(lambda x: 1 if x > 10 else 0)
    df["has_failures"] = df["failures"].apply(lambda x: 1 if x > 0 else 0)

    
    if "schoolsup" in df.columns and "famsup" in df.columns:
        df["total_support"] = df["schoolsup"] + df["famsup"]

    
    if "studytime" in df.columns and "failures" in df.columns:
        df["study_fail_interaction"] = df["studytime"] * df["failures"]

    return df

def split_features(df):
    X = df.drop("target", axis = 1)
    y = df["target"]

    return X, y

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)

def scale_data(X_train, X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    joblib.dump(scaler, "models/scaler.pkl")

    return X_train, X_test



