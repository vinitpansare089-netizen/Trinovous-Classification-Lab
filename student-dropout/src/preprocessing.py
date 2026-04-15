import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.preprocessing import StandardScaler

def encode_data(df):
    df = pd.get_dummies(df, drop_first=True)
    return df

def feature_engineering(df):

    # ===============================
    # 🎯 1. Academic Performance Ratio
    # ===============================

    df["sem1_pass_ratio"] = df["Curricular units 1st sem (approved)"] / (
        df["Curricular units 1st sem (enrolled)"] + 1
    )

    df["sem2_pass_ratio"] = df["Curricular units 2nd sem (approved)"] / (
        df["Curricular units 2nd sem (enrolled)"] + 1
    )

    # ===============================
    # 📊 2. Average Grades
    # ===============================

    df["avg_grade"] = (
        df["Curricular units 1st sem (grade)"] +
        df["Curricular units 2nd sem (grade)"]
    ) / 2

    # ===============================
    # ⚡ 3. Engagement Score
    # ===============================

    df["engagement"] = (
        df["Curricular units 1st sem (evaluations)"] +
        df["Curricular units 2nd sem (evaluations)"]
    )

    # ===============================
    # ⚠️ 4. Risk Flags
    # ===============================

    df["high_debt"] = df["Debtor"].apply(lambda x: 1 if x == 1 else 0)

    df["fees_issue"] = df["Tuition fees up to date"].apply(
        lambda x: 0 if x == 1 else 1
    )

    # ===============================
    # 📉 5. Low Performance Flag
    # ===============================

    df["low_performance"] = df["avg_grade"].apply(
        lambda x: 1 if x < 10 else 0
    )

    # ===============================
    # 🔗 6. Combined Risk Score
    # ===============================

    df["risk_score"] = (
        df["high_debt"] +
        df["fees_issue"] +
        df["low_performance"]
    )

    # ===============================
    # 👨‍👩‍👧 7. Parent Education Level
    # ===============================

    df["parent_edu_avg"] = (
        df["Mother's qualification"] +
        df["Father's qualification"]
    ) / 2

    # ===============================
    # 📊 8. Total Approved Units
    # ===============================

    df["total_approved"] = (
        df["Curricular units 1st sem (approved)"] +
        df["Curricular units 2nd sem (approved)"]
    )

    return df

def split_features(df):
    X = df.drop("Target", axis = 1)
    y = df["Target"]

    return X, y

def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)

def scale_data(X_train, X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    joblib.dump(scaler, "models/scaler.pkl")

    return X_train, X_test



