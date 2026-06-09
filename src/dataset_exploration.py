import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/raw/sms+spam+collection/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Basic information
print("Dataset Shape:")
print(df.shape)

print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Class distribution
print("\nLabel Distribution:")
print(df["label"].value_counts())

# Feature Engineering
df["message_length"] = df["message"].apply(len)

print("\nAverage Message Length:")
print(df.groupby("label")["message_length"].mean())