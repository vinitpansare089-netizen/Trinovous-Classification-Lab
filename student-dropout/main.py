from src.data_loader import load_data

df = load_data("data/raw/dataset.csv")

print(df.head(10))