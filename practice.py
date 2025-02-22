import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score


np.random.seed(1)#generating synthetic data


n_products = 1000# simulate 1000 products
n_reviews = 100  # each product has 100 customer reviews

# each customer review is randomly positive (1) or negative (0)
X = np.random.randint(0, 2, size=(n_products, n_reviews))

# product success is influenced by majority positive reviews
success = (X.sum(axis=1) > n_reviews // 2).astype(int)  # Majority vote
y = success

# split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# train a random forest  model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
#making prediction
y_pred = rf.predict(X_test)

# Step 5: Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification report:\n", classification_report(y_test, y_pred))

# Feature importance
importance = rf.feature_importances_

scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')
print("Cross-validation scores:", scores)
print("Mean accuracy:", np.mean(scores))


from sklearn.model_selection import GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
print("Best Parameters:", grid_search.best_params_)

# Visualize the importance of each review in predicting product success
plt.figure(figsize=(12, 6))
sns.barplot(x=np.arange(n_reviews), y=importance, hue=np.arange(n_reviews), dodge=False, palette="viridis", legend=False)
plt.title("customer review for product", fontsize=16)
plt.xlabel("review index", fontsize=14)
plt.ylabel("feature importance", fontsize=14)
plt.tight_layout()
plt.show()


