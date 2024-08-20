# -*- coding: utf-8 -*-
"""Week14_day6_xp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jUs9-Vcz8PPXnMOaau0a-AOlnYOO5bPC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer


# Load Data
df = pd.read_csv('/content/heart_disease_uci.csv')

# Display basic information about the dataset
print(df.info())
print("\nSample of the data:")
print(df.head())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Descriptive statistics for numerical columns
numerical_features = ['age', 'trestbps', 'chol', 'thalch', 'oldpeak', 'ca', 'num']
print("\nDescriptive statistics for numerical columns:")
print(df[numerical_features].describe())

# Distribution of the target variable
plt.figure(figsize=(8, 6))
df['num'].value_counts().sort_index().plot(kind='bar')
plt.title('Distribution of Heart Disease Severity')
plt.xlabel('Severity (0-4)')
plt.ylabel('Count')
plt.show()

# Histograms of numerical features
df[numerical_features].hist(figsize=(15, 10))
plt.tight_layout()
plt.show()

# Preprocessing
# Handle missing values
numeric_imputer = SimpleImputer(strategy='mean')
categorical_imputer = SimpleImputer(strategy='most_frequent')

df[numerical_features] = numeric_imputer.fit_transform(df[numerical_features])
categorical_features = ['sex', 'dataset', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
df[categorical_features] = categorical_imputer.fit_transform(df[categorical_features])

# Encode categorical variables
le = LabelEncoder()
for feature in categorical_features:
    df[feature] = le.fit_transform(df[feature].astype(str))

# Scale the numerical features
scaler = StandardScaler()
df[numerical_features[:-1]] = scaler.fit_transform(df[numerical_features[:-1]])  # Exclude 'num' from scaling

# Correlation matrix of numerical features
plt.figure(figsize=(12, 10))
sns.heatmap(df[numerical_features].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()

print("\nPreprocessed data sample:")
print(df.head())

# Additional visualizations
# Box plot for age by heart disease severity
plt.figure(figsize=(10, 6))
sns.boxplot(x='num', y='age', data=df)
plt.title('Age Distribution by Heart Disease Severity')
plt.xlabel('Heart Disease Severity')
plt.ylabel('Age')
plt.show()

# Bar plot for chest pain type by heart disease severity
plt.figure(figsize=(12, 6))
sns.countplot(x='cp', hue='num', data=df)
plt.title('Chest Pain Type by Heart Disease Severity')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.legend(title='Severity', loc='upper right')
plt.show()

# Save preprocessed data
df.to_csv('preprocessed_heart_disease_data.csv', index=False)
print("\nPreprocessed data saved to 'preprocessed_heart_disease_data.csv'")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np

# Load the preprocessed data
df = pd.read_csv('preprocessed_heart_disease_data.csv')

# Split features and target
X = df.drop('num', axis=1)
y = df['num']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Train logistic regression model
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Analyze feature importance
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': model.coef_[0]})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print(feature_importance)

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('preprocessed_heart_disease_data.csv')
X = df.drop('num', axis=1)
y = df['num']

# Feature engineering
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Feature selection
rfe = RFE(estimator=LogisticRegression(), n_features_to_select=10)
X_selected = rfe.fit_transform(X_poly, y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, stratify=y, random_state=42)

# Define the model with class weights
model = LogisticRegression(multi_class='multinomial', class_weight='balanced', max_iter=1000)

# Hyperparameter tuning
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'penalty': ['l1', 'l2']}
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='f1_macro')
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_

# Cross-validation
cv_scores = cross_val_score(best_model, X_train, y_train, cv=5, scoring='f1_macro')
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV score: {cv_scores.mean()}")

# Final evaluation
y_pred = best_model.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Threshold adjustment (if needed)
y_pred_proba = best_model.predict_proba(X_test)
# Custom thresholds can be applied here

# Feature importance (for interpretability)
feature_importance = pd.DataFrame({'feature': range(X_selected.shape[1]),
                                   'importance': best_model.coef_[0]})
feature_importance = feature_importance.sort_values('importance', ascending=False)
print(feature_importance)

"""**Model Performance Evaluation:**
The model is most effective at identifying individuals without heart disease (class 0.0).
It struggles to differentiate between the various levels of heart disease severity (classes 1.0 to 4.0).
There's a clear class imbalance, with fewer cases of severe and very severe heart disease in the dataset.





"""