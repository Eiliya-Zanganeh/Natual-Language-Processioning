import pandas as pd

dataset = pd.read_csv('dataset/dataset.csv')

def word_diversity(text):
    tokens = text.split()
    unique_tokens = set(tokens)
    return len(unique_tokens) / len(tokens) if tokens else 0

print(word_diversity(dataset.loc[0, "text"]))
