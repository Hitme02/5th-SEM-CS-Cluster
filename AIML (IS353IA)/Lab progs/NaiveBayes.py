import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load iris dataset
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names


class NaiveBayes:
    def fit(self, X, y):
        self._classes = np.unique(y)
        self._mean = np.array([X[y == c].mean(axis=0) for c in self._classes])
        self._var = np.array([X[y == c].var(axis=0) for c in self._classes])
        self._priors = np.array([X[y == c].shape[0] / len(y) for c in self._classes])

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        posteriors = [np.log(prior) + np.sum(np.log(self._pdf(idx, x)))
                      for idx, prior in enumerate(self._priors)]
        return self._classes[np.argmax(posteriors)]

    def _pdf(self, class_idx, x):
        mean, var = self._mean[class_idx], self._var[class_idx]
        numerator = np.exp(- (x - mean)**2 / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        return numerator / denominator



# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create and train the Naive Bayes model
nb = NaiveBayes()
nb.fit(X_train, y_train)

# Make predictions
y_pred = nb.predict(X_test)
print('Accuracy: %.4f' % np.mean(y_pred == y_test))
# Print class names instead of class numbers
print("Predictions:", iris.target_names[y_pred])



### Optional confusion matrix

from sklearn.metrics import confusion_matrix, classification_report
# Print confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))