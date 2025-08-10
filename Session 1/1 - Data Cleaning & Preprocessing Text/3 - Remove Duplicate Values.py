import pandas as pd

data = {
    "text": [
        "I love NLP! 💙",
        "Python is GREAT for Machine Learning.",
        "NLP is fun!!!",
        None,
        "I love NLP! 💙",
        "Deep learning > traditional methods..."
    ],
    "label": ["positive", "neutral", "positive", "positive", "neutral", "neutral"]
}

df = pd.DataFrame(data)

df.drop_duplicates(subset=["text"], inplace=True)
df.reset_index(drop=True, inplace=True)
print(df.head())
