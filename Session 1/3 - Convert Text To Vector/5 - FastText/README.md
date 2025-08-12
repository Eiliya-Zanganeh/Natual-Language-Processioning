# FastText 🚀

## Introduction

FastText is a word embedding model developed by the Facebook AI Research team. Similar to Word2Vec, it learns vector representations for words, but it also considers subwords (character n-grams). This feature allows FastText to generate meaningful vectors for new or out-of-vocabulary words and provides better generalization, especially for languages with complex morphology.

## Advantages ✨

* **Subword-level embeddings:** The model breaks words into smaller parts (character n-grams) and represents each word as the sum of its subword vectors.
* **Ability to generalize to new words:** Even if a word was not seen during training, FastText can create a vector for it based on its subwords.
* **Great for morphologically rich languages:** Such as Persian, Turkish, German, and others.
* **High efficiency:** Fast training speed and good performance compared to similar models.

## Use Cases 📚

* Generating numeric word vectors (embeddings) for NLP projects
* Text classification, clustering, and Named Entity Recognition (NER)
* Useful for multiple languages, even with limited data resources
* Enhancing deep learning models by using pre-trained embeddings

## Important FastText Parameters ⚙️

| Parameter     | Description                                        | Default Value (Example)            |
| ------------- | -------------------------------------------------- | ---------------------------------- |
| `vector_size` | Length of the vector representation for each word  | 100                                |
| `window`      | Context window size for learning surrounding words | 5                                  |
| `min_count`   | Minimum frequency count for words to be included   | 5                                  |
| `sg`          | Model type: 0 for CBOW, 1 for Skip-Gram            | 1 (Skip-Gram)                      |
| `epochs`      | Number of training epochs                          | 5                                  |
| `min_n`       | Minimum length of character n-grams                | 3                                  |
| `max_n`       | Maximum length of character n-grams                | 6                                  |
| `workers`     | Number of CPU cores used for parallel training     | Number of CPU cores on your system |

## Final Notes 📝

* The `min_n` and `max_n` parameters specify the minimum and maximum length of the character n-grams. Choosing appropriate values depends on your language and data.
* Increasing `epochs` usually improves model quality but increases training time.
* `sg=1` enables the Skip-Gram model, and `sg=0` enables the CBOW model.
