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

df["text"] = df["text"].str.lower()
print(df.head())
