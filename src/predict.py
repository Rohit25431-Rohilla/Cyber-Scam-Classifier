import pickle
import pandas as pd

df = pd.read_csv("data/processed/cleaned_sms.csv")

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df["clean_message"])

y = df["label"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(X_train, y_train)
with open("models/spam_classifier.pkl", "wb") as file:
    pickle.dump(model, file)

with open("models/vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

message = input("Enter a message: ")

message_features = vectorizer.transform([message])
prediction = model.predict(message_features)

print("Prediction:", prediction[0])
