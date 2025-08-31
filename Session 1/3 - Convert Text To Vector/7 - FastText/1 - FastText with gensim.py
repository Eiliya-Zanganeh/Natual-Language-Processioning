from gensim.models import FastText

sentences = [
    ['I', 'love', 'natural', 'language', 'processing'],
    ['Word2Vec', 'is', 'a', 'great', 'tool'],
    ['I', 'love', 'machine', 'learning'],
    ['Natural', 'language', 'processing', 'is', 'fun']
]

model = FastText(
    sentences,
    vector_size=50,
    window=3,
    min_count=1,
    epochs=10,
    sg=1,
    min_n=3,
    max_n=6,
    workers=4
)

print(model.wv['language'])

print(model.wv.most_similar('language'))
