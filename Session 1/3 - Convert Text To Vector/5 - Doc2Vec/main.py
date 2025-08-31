from gensim.models.doc2vec import Doc2Vec, TaggedDocument

sentences = [
    ['I', 'love', 'natural', 'language', 'processing'],
    ['Word2Vec', 'is', 'a', 'great', 'tool'],
    ['I', 'love', 'machine', 'learning'],
    ['Natural', 'language', 'processing', 'is', 'fun']
]

tagged_data = [TaggedDocument(words=sent, tags=[str(i)]) for i, sent in enumerate(sentences)]

model = Doc2Vec(
    vector_size=100,
    window=3,
    min_count=1,
    workers=4,
    dm=1
)

model.build_vocab(tagged_data)

model.train(tagged_data, total_examples=model.corpus_count, epochs=40)

print("Vector for document 0:", model.dv['0'])

new_sentence = ["I", "enjoy", "deep", "learning"]
print("Inferred vector for new sentence:", model.infer_vector(new_sentence))

print("Most similar documents to doc 0:", model.dv.most_similar('0'))
