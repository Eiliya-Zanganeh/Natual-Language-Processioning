# Bag of Words (BoW) 🧺📚

## What is Bag of Words? 🤔

**Bag of Words (BoW)** is one of the simplest and most widely used techniques in Natural Language Processing (NLP) for representing text data. It converts text into numerical feature vectors based on the **frequency of words** in the text, **ignoring grammar and word order**.

---

## How does BoW work? 🛠️

1. **Build a Vocabulary**:
   Collect all unique words from the whole dataset of documents (texts).

2. **Convert Texts to Vectors**:
   For each document, count how many times each word from the vocabulary appears in that document.
   This count forms a vector (list of numbers), where each position corresponds to a word in the vocabulary.

3. **Ignore Word Order**:
   BoW treats the document simply as a "bag" of words. The order and context are not considered, only the counts.

---

## Example 📖

Consider these three example texts:

```python
texts = [
    "I Love NLP",
    "I Love Python And I Love Django",
    "Hello World"
]
```

### Step 1: Create Vocabulary

We combine all texts and get unique words:

```python
all_text = " ".join(texts)
all_words = all_text.lower().split()
vocabulary = set(all_words)
print(vocabulary)  # {'nlp', 'world', 'love', 'hello', 'django', 'and', 'i', 'python'}
```

Vocabulary is the set of unique words:

`{'nlp', 'world', 'love', 'hello', 'django', 'and', 'i', 'python'}`

---

### Step 2: Convert Each Text to a Vector

We write a function that counts the occurrences of each vocabulary word in the given text:

```python
def convert_text(text):
    words = text.lower().split()
    vector = [words.count(word) for word in vocabulary]
    return vector
```

---

### Step 3: Output Vectors for Each Text

```python
print(convert_text(texts[0]))  # [1, 0, 1, 0, 0, 0, 1, 0]
print(convert_text(texts[1]))  # [0, 0, 2, 0, 1, 1, 2, 1]
print(convert_text(texts[2]))  # [0, 1, 0, 1, 0, 0, 0, 0]
```

Here, each list represents the frequency counts of words from the vocabulary in the order they appear in the vocabulary set. For example, the first vector `[1, 0, 1, 0, 0, 0, 1, 0]` means:

* "nlp": 1
* "world": 0
* "love": 1
* "hello": 0
* "django": 0
* "and": 0
* "i": 1
* "python": 0

---

## Summary ✨

* **Bag of Words** is a simple vectorization technique that transforms text into a frequency vector of words.
* It **ignores word order and grammar**, focusing only on the presence and count of words.
* It's often the **first step in text classification, sentiment analysis, and other NLP tasks**.
* Although simple, it can be very effective, especially combined with other techniques.