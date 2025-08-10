# Exploratory Data Analysis (EDA) 🧹📝✨

## Introduction

In this section, we explore and analyze the dataset from different perspectives to better understand its characteristics and potential issues.

---

## Analysis Steps

1. **Label Count & Sentiment Balance**
2. **Sentence Length**
3. **Most Frequent & Rare Words, and WordCloud**
4. **Sampling**
5. **n-grams**
6. **Word Diversity**

---

### 1. Label Count & Sentiment Balance ⚖️

In this step, all labels in the dataset are examined. We calculate the count and percentage of each label relative to the total to identify any imbalance or potential issues with the labeling.

---

### 2. Sentence Length 📏

Here, we analyze the length of sentences in the dataset. This helps us find appropriate sentence length limits to optimize AI model training.

---

### 3. Most Frequent & Rare Words, and WordCloud ☁️🔍

This part focuses on:

* Identifying the most frequent words in the dataset.
* Finding rare or infrequent words.
* Using WordCloud as a visual tool to represent word frequency and prominence.

---

### 4. Sampling 🎲

In this step, random samples of the dataset are reviewed manually to check for any anomalies or inconsistencies in the overall data.

---

### 5. n-grams 📚

Sentences are split into sequences of *n* consecutive words for various purposes.

#### Applications of n-grams:

* **Language Modeling:**
  Predicting the next word in a sentence based on previous words.

* **Feature Extraction:**
  Transforming text into numeric features for machine learning models. Instead of using only single words (uni-grams), pairs (bi-grams), triplets (tri-grams), etc., are also considered.

* **Writing Style Analysis:**
  Finding frequently repeated phrases or language patterns.

* **Sentence Similarity Detection:**
  Comparing n-grams of two texts to measure their similarity.

* **Reducing Semantic Ambiguity:**
  For example, “New York” as two words together carries a special meaning and is treated as a bi-gram.

---

### 6. Word Diversity 🌈

This section evaluates how many unique or non-repetitive words each sentence contains, indicating lexical richness.
