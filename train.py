import bentoml

from sklearn import svm
from sklearn import datasets

# Load training data set
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train the model
clf = svm.SVC(gamma="scale")
clf.fit(X, y)

# Save model to BentoML local model store
saved_model = bentoml.sklearn.save_model("iris_clf", clf)
print(f"Saved Model: {saved_model}")
