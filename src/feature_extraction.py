import pandas as pd

df = pd.read_csv("data/processed/cleaned_sms.csv")

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["clean_message"])

print(vectorizer.get_feature_names_out()[:20])