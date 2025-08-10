import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
print(stop_words)


def clean(text):
    return " ".join([word for word in text.split() if word not in stop_words])


if __name__ == "__main__":
    print(clean("what is NLP?"))
