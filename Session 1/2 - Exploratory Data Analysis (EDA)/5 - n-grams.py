from nltk.util import ngrams
import pandas as pd

dataset = pd.read_csv('dataset/dataset.csv')


def get_ngrams(text, n=2):
    tokens = text.split()
    return list(ngrams(tokens, n))


print(get_ngrams(dataset.loc[0, "text"], 2))
