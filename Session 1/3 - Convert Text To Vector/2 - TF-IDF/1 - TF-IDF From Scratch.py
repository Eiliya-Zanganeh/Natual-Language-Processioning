import math

texts = [
    "the sky is blue",
    "the sun is bright",
    "the sun in the blue sky is bright",
    "we can see the shining sun the bright sun"
]

tokenized_texts = list(map(lambda x: x.lower().split(), texts))

all_words = sorted(list(set(word for text in tokenized_texts for word in text)))


def compute_tf(text):
    tf_dict = {}
    total_terms = len(text)
    for word in all_words:
        tf_dict[word] = text.count(word) / total_terms
    return tf_dict


def compute_idf():
    idf_dict = {}
    N = len(tokenized_texts)
    for word in all_words:
        containing_docs = sum(1 for text in tokenized_texts if word in text)
        idf_dict[word] = math.log((1 + N) / (1 + containing_docs)) + 1
    return idf_dict


def l2_normalize(vec):
    norm = math.sqrt(sum(v ** 2 for v in vec))
    return [v / norm for v in vec] if norm != 0 else vec


idf_all = compute_idf()

tfidf_all = []
for doc in tokenized_texts:
    tf = compute_tf(doc)
    tfidf = [tf[word] * idf_all[word] for word in all_words]
    tfidf_normalized = l2_normalize(tfidf)
    tfidf_all.append(tfidf_normalized)

for tfidf in tfidf_all:
    print(tfidf)
