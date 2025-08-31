# 📄 Doc2Vec: Vector Representation of Text Documents

## 📌 Introduction

**Doc2Vec** (also known as Paragraph Vector) is a distributed representation model from the **Word2Vec** family, introduced by [Le and Mikolov (2014)](https://arxiv.org/abs/1405.4053).
Unlike Word2Vec, which only converts words into numeric vectors, Doc2Vec can map an entire **sentence**, **paragraph**, or **document** into a **dense, fixed-length vector**.

This capability makes Doc2Vec useful in applications such as:

* 🔍 Semantic document search
* 💬 Sentiment analysis
* 📑 Text classification and clustering
* 🤖 Question answering systems (Q\&A)
* 🧠 Information retrieval

---

## ⚙️ How It Works

Doc2Vec has two main architectures:

1. **Distributed Memory (DM)**

   * Similar to Continuous Bag of Words (CBOW) in Word2Vec.
   * A document vector is combined with context word vectors to predict the target word.

2. **Distributed Bag of Words (DBOW)**

   * Similar to Skip-Gram.
   * The document vector is used to predict randomly sampled words from the same document.

Both methods can be trained separately or in combination.

---

## 📊 Applications of Doc2Vec

* **Sentiment Analysis**: Classifying reviews as positive or negative.
* **Topic Detection**: Automatically labeling articles or news.
* **Recommendation Systems**: Finding similar documents or articles.
* **Semantic Search**: Retrieving documents based on meaning rather than just keywords.

---