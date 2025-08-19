import re

import swifter
import pandas as pd
from nltk import download
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk import WordNetLemmatizer
from nltk import pos_tag

# download('punkt')
# download('stopwords')
# download('wordnet')
# download('omw-1.4')
# download('averaged_perceptron_tagger_eng')


class DataCleaning:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()
        self.tag_dict = {
            "J": wordnet.ADJ,
            "N": wordnet.NOUN,
            "V": wordnet.VERB,
            "R": wordnet.ADV
        }

    def __call__(self, dataset, text_column, label_column):
        dataset.dropna(subset=[text_column], inplace=True)
        dataset = dataset[dataset[text_column].str.strip() != ""]
        dataset.drop_duplicates(subset=[text_column], inplace=True)
        dataset.reset_index(drop=True, inplace=True)
        print("Starting data cleaning...")
        dataset[text_column] = dataset[text_column].swifter.apply(self.clean)
        dataset[label_column].replace({"positive": 1, "negative": 0}, inplace=True)
        return dataset

    def clean(self, text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters & Remove numbers
        words = word_tokenize(text)
        tags = pos_tag(words)
        words = [
            self.lemmatizer.lemmatize(w, self.tag_dict.get(t[0].upper(), wordnet.NOUN))
            for w, t in zip(words, tags)
        ]
        words = [word for word in words if word not in self.stop_words]
        text = ' '.join(words)
        return text

if __name__ == "__main__":
    data_cleaning = DataCleaning()
    df = pd.read_csv('Dataset/IMDB Dataset.csv')

    # Split 5K Data From 0 - Preprocessing Dataset
    positives = df[df['sentiment'] == 'positive']
    negatives = df[df['sentiment'] == 'negative']
    sample_positive = positives.sample(n=2500, random_state=42)
    sample_negative = negatives.sample(n=2500, random_state=42)
    df = pd.concat([sample_positive, sample_negative])

    df = data_cleaning(df, 'review', 'sentiment')
    df.to_excel('Dataset/IMDB Dataset 5K Cleaned.xlsx', index=False)