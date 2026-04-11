from src.data_loader import load_data

df = load_data("data/raw/dataset.csv")

# print(df.head(10))
print(df.columns)
# print(df.info())

# print(df.nunique().sort_values(ascending=False))

# print(df.corr(numeric_only=True)['Target'].sort_values())








