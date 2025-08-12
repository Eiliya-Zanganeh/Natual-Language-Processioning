from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "I Love NLP",
    "I Love Python And I Love Django",
    "Hello World"
]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)

print(vectorizer.get_feature_names_out())  # ['and' 'django' 'hello' 'love' 'nlp' 'python' 'world']

print(x.toarray())  # [[0 0 0 1 1 0 0]
                    # [1 1 0 2 0 1 0]
                    # [0 0 1 0 0 0 1]]
