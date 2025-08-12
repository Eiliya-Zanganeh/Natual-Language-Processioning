sentence = "I love NLP and I love Python"

vocab = {}
index = 0

words = sentence.split()

for word in words:
    if word not in vocab:
        vocab[word] = index
        index += 1

print("Vocabulary:", vocab)

indexed_sentence = [vocab[word] for word in words]

print("Indexed sentence:", indexed_sentence)
