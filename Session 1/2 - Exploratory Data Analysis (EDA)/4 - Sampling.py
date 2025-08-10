import pandas as pd

dataset = pd.read_csv('dataset/dataset.csv')

sampled_df = dataset.sample(n=5, random_state=42)
for index, row in sampled_df.iterrows():
    print(row['text'], row['label'])
