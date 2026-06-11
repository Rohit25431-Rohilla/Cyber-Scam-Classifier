import pandas as pd

df = pd.read_csv(
    "data/raw/sms+spam+collection/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)



from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    
    # Tokenization
    tokens = text.split()

    # Stopword Removal
    filtered_words = []

    for word in tokens:
        if word.lower() not in stop_words:
            filtered_words.append(word)

    # Lemmatization
    clean_words = []

    for word in filtered_words:
        clean_words.append(
            lemmatizer.lemmatize(word.lower())
        )

    return " ".join(clean_words)

df["clean_message"] = df["message"].apply(clean_text)


df.to_csv(
    "data/processed/cleaned_sms.csv",
    index=False
)

print("Processed dataset saved!")