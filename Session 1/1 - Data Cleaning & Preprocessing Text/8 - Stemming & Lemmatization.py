import nltk
from nltk import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')  # for tokenization
nltk.download('punkt_tab')  # for tokenization
nltk.download('wordnet')  # for Lemmatization
nltk.download('omw-1.4')  # data for Lemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


def clean(text):
    tokens = word_tokenize(text)
    stemmed_text = [stemmer.stem(token) for token in tokens]
    lemmas = [lemmatizer.lemmatize(token, pos='v') for token in tokens]  # pos='v' => Verb
    return stemmed_text, lemmas


if __name__ == "__main__":
    stemmed_text, lemmas = clean("running runner runs easily fairly")
    print(stemmed_text)
    print(lemmas)
