# 📚 Word2Vec

## 📌 Introduction

**Word2Vec** is a machine learning model that converts words into numerical vectors in such a way that words with similar meanings have vectors close to each other.
This model was introduced by Tomas Mikolov and the Google team, and it is widely used in many NLP (Natural Language Processing) projects.

---

## 🎯 Applications of Word2Vec

* Finding similarities between words
* Clustering and categorizing words
* Using in advanced NLP models such as machine translation, sentiment analysis, and chatbots
* Creating semantic relationships such as:

  ```
  king - man + woman ≈ queen
  ```

---

## 🏗 Word2Vec Architectures

| Feature                       | **CBOW**                                                     | **Skip-Gram**                                                |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Definition                    | Predict the **target word** from the context words           | Predict the **context words** from the target word           |
| Parameter `sg`                | `0`                                                          | `1`                                                          |
| Training speed                | Faster                                                       | Slightly slower                                              |
| Performance on small datasets | Weaker                                                       | Better                                                       |
| Performance on large datasets | Good performance                                             | Good performance (often preferred for rare word learning)    |
| Performance on rare words     | Weaker                                                       | Better                                                       |
| Example                       | Context: `["I", "love", "Python"]` → Target: `"programming"` | Target: `"Python"` → Context: `["I", "love", "programming"]` |

---

## ⚙️ Key Parameters in Gensim Word2Vec

| Parameter        | Description                                                            |
| ---------------- | ---------------------------------------------------------------------- |
| **sentences**    | Input data in the form of a list of lists of words                     |
| **vector\_size** | Number of dimensions for each word vector (usually 100–300)            |
| **window**       | Number of words before and after the target word considered as context |
| **min\_count**   | Minimum frequency of a word to be included in the vocabulary           |
| **workers**      | Number of CPU cores to use for parallel training                       |
| **sg**           | Model type: `0` = CBOW, `1` = Skip-Gram                                |

---

## 🖥 Example Code

```python
from gensim.models import Word2Vec

# Training data
sentences = [
    ['I', 'love', 'natural', 'language', 'processing'],
    ['Word2Vec', 'is', 'a', 'great', 'tool'],
    ['I', 'love', 'machine', 'learning'],
    ['Natural', 'language', 'processing', 'is', 'fun']
]

# Train the Word2Vec model
model = Word2Vec(
    sentences,
    vector_size=100, # Vector dimensions
    window=3,        # Context window size
    min_count=1,     # Minimum word frequency
    workers=4,       # Number of processing cores
    sg=1             # Use Skip-Gram
)

# Display the vector for the word 'language'
print(model.wv['language'])

# Display words similar to 'language'
print(model.wv.most_similar('language'))
```

---

## 📤 Sample Output

```
[ 0.0031  0.0068  0.0052 ... ]   # Vector for the word 'language'
[('natural', 0.251), ('processing', 0.231), ...]  # Similar words
```

---

## 📎 Important Note

* In this example, the model is trained on a very small dataset, so the results are for demonstration purposes only.
