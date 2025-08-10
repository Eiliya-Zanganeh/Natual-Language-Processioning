import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

dataset = pd.read_csv('dataset/dataset.csv')
all_sentences = dataset["text"].tolist()
all_text = " ".join(all_sentences)
all_words = all_text.split()
word_freq = Counter(all_words)
print(word_freq.most_common(10))
rare_words = [word for word, count in word_freq.items() if count == 1]
print(rare_words)

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
