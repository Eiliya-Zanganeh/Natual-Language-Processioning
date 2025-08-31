import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
import lightgbm as lgb

dataset = np.load('../0 - Preprocessing Dataset/Dataset/vector_dataset.npz')
X = dataset['sentence_vectors']
y = dataset['labels']

print("Shape of sentence vectors:", X.shape)
print("Shape of labels:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

params = {
    'n_estimators': [200, 500],
    'learning_rate': [0.01, 0.05, 0.1],
    'subsample': [0.7, 0.8, 1.0]
}

lgb_model = lgb.LGBMClassifier(objective='binary', random_state=42)

grid = GridSearchCV(
    estimator=lgb_model,
    param_grid=params,
    scoring='accuracy',
    cv=3,
    verbose=1
)
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)

y_pred = grid.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
