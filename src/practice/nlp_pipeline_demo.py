from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

message = "Congratulations! You have won a FREE prize now"

# Tokenization
tokens = message.split()

# Stopwords
stop_words = stopwords.words("english")

filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

# Lemmatization
lemmatizer = WordNetLemmatizer()

clean_words = []

for word in filtered_words:
    clean_words.append(
        lemmatizer.lemmatize(word.lower())
    )

print("Original:", message)
print("Tokens:", tokens)
print("After Stopwords:", filtered_words)
print("Final Clean Text:", clean_words)