texts = [
    "I Love NLP",
    "I Love Python And I Love Django",
    "Hello World"
]

all_text = " ".join(texts)
all_words = all_text.lower().split()
vocabulary = set(all_words)
print(vocabulary)  # {'nlp', 'world', 'love', 'hello', 'django', 'and', 'i', 'python'}


def convert_text(text):
    words: list = text.lower().split()
    vector = [words.count(val) for val in vocabulary]
    return vector


print(convert_text(texts[0]))  # [1, 0, 1, 0, 0, 0, 1, 0]
print(convert_text(texts[1]))  # [0, 0, 2, 0, 1, 1, 2, 1]
print(convert_text(texts[2]))  # [0, 1, 0, 1, 0, 0, 0, 0]