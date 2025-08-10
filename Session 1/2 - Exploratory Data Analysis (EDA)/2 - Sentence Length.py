import pandas as pd
import matplotlib.pyplot as plt


def count_word(text):
    return len(text.split())


dataset = pd.read_csv('dataset/dataset.csv')

dataset['text_length'] = dataset['text'].apply(count_word)

print(dataset['text_length'].describe())

plt.hist(dataset["text_length"], bins=5, color="skyblue", edgecolor="black")
plt.xlabel("Sentence Length (words)")
plt.ylabel("Frequency")
plt.title("Sentence Length Distribution")
plt.show()
