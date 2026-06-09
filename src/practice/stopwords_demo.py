from nltk.corpus import stopwords

stop_words = stopwords.words("english")

message = "You have won a free prize"

tokens = message.split()

filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print("Original:", tokens)
print("After Stopword Removal:", filtered_words)