from tqdm import tqdm
import numpy as np
import pandas as pd
from gensim.models import FastText
from nltk.tokenize import word_tokenize
from nltk import download

# download("punkt")


class ConvertTextToVector:
    def __call__(self, dataset, vector_size, text_column, label_column):
        self.vector_size = vector_size
        sentences = dataset[text_column].apply(lambda x: word_tokenize(x)).tolist()
        self.max_length = max(len(sentence) for sentence in sentences)
        labels = dataset[label_column].tolist()
        print("Start FastText Learning...")
        model = FastText(
            sentences,
            vector_size=self.vector_size,
            window=3,
            min_count=1,
            epochs=10,
            sg=1,
            min_n=3,
            max_n=6,
            workers=4
        )
        word_vectors_dict = {
            "words": np.array(model.wv.index_to_key),
            "vectors": np.array(model.wv.vectors, dtype=np.float32)
        }
        np.save("Dataset/fasttext_model.npy", word_vectors_dict)
        print("fasttext_model.npy Saved!")

        print("Start Convert Sentences To Vector...")
        vector_batches = []
        label_batches = []

        for idx in tqdm(range(len(sentences))):
            sentence = sentences[idx]
            label = labels[idx]

            sentence_array = np.array(
                [model.wv[word] for word in sentence if word in model.wv],
                dtype=np.float32
            )
            sentence_array = convertor.apply_padding(sentence_array)

            vector_batches.append(sentence_array)
            label_batches.append(label)

        vectors_dict = {
            "sentence_vectors": np.array(vector_batches, dtype=np.float32),
            "labels": np.array(label_batches, dtype=np.float32)
        }
        np.save(f"Dataset/vector_dataset.npy", vectors_dict)
        print(f"vectors_dict_last.npy Saved!")

    def apply_padding(self, sentence):
        if len(sentence) < self.max_length:
            padding_size = self.max_length - len(sentence)
            padding = np.zeros((padding_size, self.vector_size))
            sentence = np.vstack((sentence, padding))
        return sentence


if __name__ == "__main__":
    convertor = ConvertTextToVector()
    df = pd.read_excel("Dataset/IMDB Dataset 5K Cleaned.xlsx")
    convertor(df, 100, text_column="review", label_column="sentiment")
