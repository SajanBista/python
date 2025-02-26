"""#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#taking care of missing datas
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean') #inputing mean in empty numeric places
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Encoding the independent variables
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

#encoding the depedent variables
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# splitting the data into training and tets set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)


#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])

print(X_train)
print(X_test)"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Assuming the CSV file is in the same directory
dataset = pd.read_csv('Data.csv')

# Separate features and target variable
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Check for missing value types and choose appropriate imputation strategy
from sklearn.impute import SimpleImputer, KNNImputer  # Consider KNN for skewed data
imputer_strategy = 'mean'  # Adjust based on data analysis
if pd.api.types.is_numeric_dtype(X[:, 1]):  # Check if column 1 is numeric
    imputer_strategy = 'median'  # Use median for skewed numeric data

imputer = SimpleImputer(missing_values=np.nan, strategy=imputer_strategy)
imputer.fit(X[:, 1:])  # Impute for columns 1 and onwards (excluding 0)
X[:, 1:] = imputer.transform(X[:, 1:])

# Identify categorical column indices (assuming more than one)
categorical_cols = [i for i in range(len(X.T)) if pd.api.types.is_categorical_dtype(X.T[i])]

# One-hot encoding for categorical features
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), categorical_cols)], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Label encoding for target variable (consider one-hot encoding if categories are nominal)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# Splitting the data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Feature scaling for all features (adjust if not all need scaling)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_train)
print(X_test)