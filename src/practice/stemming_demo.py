from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "play",
    "playing",
    "played",
    "studies",
    "studying",
    "running",
    "runner",
    "happiness",
    "winning"
]

for word in words:
    print(word, "->", stemmer.stem(word))