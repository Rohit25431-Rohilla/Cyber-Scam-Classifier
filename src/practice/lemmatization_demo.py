from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = [
    "studies",
    "studying",
    "running",
    "cars",
    "winning"
]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))