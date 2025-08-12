from gensim.models import Word2Vec

sentences = [
    ['I', 'love', 'natural', 'language', 'processing'],
    ['Word2Vec', 'is', 'a', 'great', 'tool'],
    ['I', 'love', 'machine', 'learning'],
    ['Natural', 'language', 'processing', 'is', 'fun']
]

model = Word2Vec(
    sentences,
    vector_size=100, # Vector dimensions
    window=3,        # Context window size
    min_count=1,     # Minimum word frequency
    workers=4,       # Number of processing cores
    sg=1             # Use Skip-Gram
)

print(model.wv['language'])

print(model.wv.most_similar('language'))
