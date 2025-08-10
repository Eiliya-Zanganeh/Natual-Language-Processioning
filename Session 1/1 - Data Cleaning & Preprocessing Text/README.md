# Data Cleaning & Text Preprocessing 🧹📝✨

## Introduction

Text preprocessing is one of the most important steps in almost every NLP or AI project. During this phase, the main focus is on properly cleaning the text data to prepare it for modeling.
The primary goal is to remove any noise or irrelevant information that might negatively affect the model’s accuracy.

---

## Text Preprocessing Steps

> ⚠️ **Note:** The exact steps may vary depending on the project and your specific requirements.

1. Remove `None` values from the text.
2. Remove empty text entries.
3. Remove duplicate data.
4. Convert all letters to lowercase.
5. Remove punctuation marks and special characters.
6. Remove numbers from the text.
7. Remove stopwords (common, non-informative words).
8. Perform stemming or lemmatization to extract the root/base form of words.

---

### 1. Remove None Values from the Text 🛑

In this step, all records with `None` or null values in the text field are removed from the dataset.

---

### 2. Remove Empty Text Entries 🧼

All records containing empty strings or blank text fields are eliminated.

---

### 3. Remove Duplicate Data 🔍

Duplicate entries in the dataset are identified and removed to avoid redundancy.

---

### 4. Convert All Letters to Lowercase 🔡

All characters in the text are converted to lowercase to maintain consistency and reduce variations.

---

### 5. Remove Punctuation Marks and Special Characters ❌

All punctuation marks, emojis, and special characters that do not contribute meaningful information are removed.

---

### 6. Remove Numbers from the Text 🔢

Any numeric values appearing in the sentences are removed.

---

### 7. Remove Stopwords 🚫

Stopwords are common words that carry little meaningful information for many NLP tasks (e.g., "and", "the", "is"). Removing them can help improve model focus and performance in certain applications.

---

### 8. Perform Stemming or Lemmatization to Get the Root/Base Form of Words 🌿

This step reduces words to their root or base form by removing prefixes, suffixes, or grammatical variations. This helps clarify the core meaning of words.

Two common approaches are:

| Feature  | Stemming                   | Lemmatization               |
| -------- | -------------------------- | --------------------------- |
| Accuracy | Lower                      | Higher                      |
| Speed    | Faster                     | Slightly slower             |
| Method   | Rule-based letter chopping | Dictionary-based (WordNet)  |
| Output   | May produce non-words      | Always produces valid words |

The choice between these depends on whether you prioritize speed or accuracy.
