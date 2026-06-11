import pickle

with open("models/spam_classifier.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

message = input("Enter a message: ")

message_features = vectorizer.transform([message])

prediction = model.predict(message_features)

print("Prediction:", prediction[0])