# 📚 ELMo (Embeddings from Language Models)

## Introduction

ELMo is an advanced model for extracting **word embeddings** based on **LSTM neural networks**.
Unlike traditional methods such as Word2Vec or GloVe, which assign a fixed vector to each word, ELMo considers the **context** of the word and generates a **dynamic, context-dependent vector** for each word.
This means a word like "bank" will have different embeddings in sentences like "river bank" and "bank account"! 🌊🏦

---

## Features ✨

* Dynamic, context-aware word vectors
* Uses **bi-directional LSTM language models**
* Improves accuracy in various NLP tasks like sentiment analysis, named entity recognition, and more
* Can be used as a pre-trained layer in NLP models

---

## Applications 🛠️

* Sentiment Analysis
* Question Answering
* Text Classification
* Named Entity Recognition
* And anywhere a deeper understanding of language is needed!

---

## Further Resources 📖

* Original Paper: [https://arxiv.org/abs/1802.05365](https://arxiv.org/abs/1802.05365)
* AllenNLP Project: [https://allennlp.org/elmo](https://allennlp.org/elmo)

---