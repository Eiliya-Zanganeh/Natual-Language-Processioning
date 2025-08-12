from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "the sky is blue",
    "the sun is bright",
    "the sun in the blue sky is bright",
    "we can see the shining sun the bright sun"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

print("Vocabulary:", vectorizer.get_feature_names_out())
print("TF-IDF Matrix:\n", X.toarray())
