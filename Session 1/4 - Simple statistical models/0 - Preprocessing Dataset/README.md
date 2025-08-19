# Preprocessing Dataset

## Preprocessing steps for train model

### Dataset

#### We Use 5K Data of [IMDB Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

### Data Cleaning

- Apply lowerCase
- Remove special characters & Remove numbers
- Tokenize sentence
- Apply lemmatization

### Word Embedding with FastText

#### Model parameters:

```
vector_size = 100
window = 3
min_count = 1
epochs = 10
sg = 1
min_n = 3
max_n = 6
workers = 4
```

### In the end save numeric vector for train model.