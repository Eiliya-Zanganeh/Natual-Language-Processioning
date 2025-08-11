## Understanding TF, IDF, and TF-IDF with Example Tables 📊✨

We have four simple texts as our example dataset:

```python
texts = [
    "the sky is blue",
    "the sun is bright",
    "the sun in the blue sky is bright",
    "we can see the shining sun the bright sun"
]
```

---

### 1. Term Frequency (TF) 📈

**What is TF?**
Term Frequency measures how frequently a word appears in a single document (text). It is calculated as:

$$
\text{TF} = \frac{\text{Number of times the word appears in the document}}{\text{Total number of words in the document}}
$$

TF gives us insight into the importance of a word within a single text. Words that appear more often in a document get higher TF scores.

---

| Word    | Text 1 | Text 2 | Text 3 | Text 4 |
| ------- | ------ | ------ | ------ | ------ |
| blue    | 0.2500 | 0.0000 | 0.1250 | 0.0000 |
| bright  | 0.0000 | 0.2500 | 0.1250 | 0.1111 |
| can     | 0.0000 | 0.0000 | 0.0000 | 0.1111 |
| in      | 0.0000 | 0.0000 | 0.1250 | 0.0000 |
| is      | 0.2500 | 0.2500 | 0.1250 | 0.0000 |
| see     | 0.0000 | 0.0000 | 0.0000 | 0.1111 |
| shining | 0.0000 | 0.0000 | 0.0000 | 0.1111 |
| sky     | 0.2500 | 0.0000 | 0.1250 | 0.0000 |
| sun     | 0.0000 | 0.2500 | 0.1250 | 0.2222 |
| the     | 0.2500 | 0.2500 | 0.2500 | 0.2222 |
| we      | 0.0000 | 0.0000 | 0.0000 | 0.1111 |

---

### 2. Inverse Document Frequency (IDF) 🔍

**What is IDF?**
Inverse Document Frequency measures how important a word is across the entire collection of documents. It helps downweight very common words (like “the”, “is”) that appear in many documents, because they carry less unique information.

It is calculated as:

$$
\text{IDF}(t) = \log \left( \frac{N}{1 + \text{number of documents containing } t} \right) + 1
$$

where

* $N$ is the total number of documents
* $t$ is the term (word)

The "+1" in the denominator avoids division by zero, and the "+1" after the log ensures positive values.

---

| Word    | IDF Value |
| ------- | --------- |
| blue    | 1.5108    |
| bright  | 1.2231    |
| can     | 1.9163    |
| in      | 1.9163    |
| is      | 1.2231    |
| see     | 1.9163    |
| shining | 1.9163    |
| sky     | 1.5108    |
| sun     | 1.2231    |
| the     | 1.0000    |
| we      | 1.9163    |

---

### 3. TF-IDF (Term Frequency - Inverse Document Frequency) 🎯

**What is TF-IDF?**
TF-IDF is the product of TF and IDF, combining the local importance of a word in a single document (TF) with its global importance across all documents (IDF).

$$
\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \text{IDF}(t)
$$

* Words with **high TF** in a document but **low document frequency** (high IDF) will have higher TF-IDF scores.
* Common words with high document frequency (like “the”) get lower TF-IDF scores despite possibly high TF.
* This helps highlight words that are both frequent in a document and rare across documents, improving keyword extraction, document classification, and search relevance.

---

| Word    | Text 1 | Text 2 | Text 3 | Text 4 |
| ------- | ------ | ------ | ------ | ------ |
| blue    | 0.5686 | 0.0000 | 0.3694 | 0.0000 |
| bright  | 0.0000 | 0.5221 | 0.2991 | 0.2391 |
| can     | 0.0000 | 0.0000 | 0.0000 | 0.3746 |
| in      | 0.0000 | 0.0000 | 0.4686 | 0.0000 |
| is      | 0.4603 | 0.5221 | 0.2991 | 0.0000 |
| see     | 0.0000 | 0.0000 | 0.0000 | 0.3746 |
| shining | 0.0000 | 0.0000 | 0.0000 | 0.3746 |
| sky     | 0.5686 | 0.0000 | 0.3694 | 0.0000 |
| sun     | 0.0000 | 0.4269 | 0.4890 | 0.4782 |
| the     | 0.2500 | 0.2500 | 0.2500 | 0.2222 |
| we      | 0.0000 | 0.0000 | 0.0000 | 0.3746 |

---

### Summary 🌟

* **TF** captures how important a word is *inside a document*.
* **IDF** captures how unique or rare a word is *across documents*.
* **TF-IDF** balances both to find words that are important *inside* a document but *not common* everywhere.

This makes TF-IDF a fundamental technique for text analysis tasks such as **search engines**, **document classification**, **keyword extraction**, and **recommendation systems**.

---