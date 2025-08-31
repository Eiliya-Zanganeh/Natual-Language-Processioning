from tqdm import tqdm
import numpy as np
import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from nltk import download


# download("punkt")


class ConvertTextToVector:
    def __call__(self, dataset, vector_size, text_column, label_column):
        sentences = dataset[text_column].apply(lambda x: word_tokenize(x)).tolist()
        labels = dataset[label_column].tolist()
        tagged_data = [TaggedDocument(words=sent, tags=[str(i)]) for i, sent in enumerate(sentences)]
        print("Start Doc2Vec Learning...")
        model = Doc2Vec(
            vector_size=vector_size,
            window=3,
            min_count=1,
            workers=4,
            dm=1
        )
        model.build_vocab(tagged_data)

        model.train(tagged_data, total_examples=model.corpus_count, epochs=40)

        model.save("Dataset/doc2vec_model.model")
        print("doc2vec_model.model Saved!")

        print("Start Convert Sentences To Vector...")
        vector_batches = []
        label_batches = []

        for idx in tqdm(range(len(sentences))):
            sentence = sentences[idx]
            label = labels[idx]

            sentence_vector = model.infer_vector(sentence)

            vector_batches.append(sentence_vector)
            label_batches.append(label)

        vectors_dict = {
            "sentence_vectors": np.array(vector_batches, dtype=np.float32),
            "labels": np.array(label_batches, dtype=np.uint8)
        }
        np.savez(f"Dataset/vector_dataset.npz", **vectors_dict)
        print(f"vector_dataset.np Saved!")


if __name__ == "__main__":
    convertor = ConvertTextToVector()
    df = pd.read_excel("Dataset/IMDB Dataset 5K Cleaned.xlsx")
    convertor(df, 50, text_column="review", label_column="sentiment")
