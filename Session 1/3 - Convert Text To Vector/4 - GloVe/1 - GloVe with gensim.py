import gensim.downloader as api

model = api.load("glove-wiki-gigaword-100")

vector_king = model['king']

similar_words = model.most_similar('king', topn=5)
print(similar_words)

result = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print(result)
