import pandas as pd

dataset = pd.read_csv('dataset/dataset.csv')
# print(dataset.columns)
sentiment_counts = dataset['label'].value_counts()
print(sentiment_counts)

sentiment_balance = sentiment_counts / len(dataset)
print("Sentiment Balance:", sentiment_balance)
