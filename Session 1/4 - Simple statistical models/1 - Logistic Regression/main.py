import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

dataset = np.load('../0 - Preprocessing Dataset/Dataset/vector_dataset.npz')
X = dataset['sentence_vectors']
y = dataset['labels']

print("Shape of sentence vectors:", X.shape)
print("Shape of labels:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=100)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)
