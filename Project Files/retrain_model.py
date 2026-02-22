"""
Retrain the DecisionTreeClassifier model with synthetic data
that matches the original dataset's pattern.
This is needed because the existing model.pkl was saved with an
older scikit-learn version and can't be loaded with the current version.
"""
import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

np.random.seed(42)
n_samples = 50000

# Features: type (1-5), amount, oldbalanceOrg, newbalanceOrig
# Types: CASH_OUT=1, PAYMENT=2, CASH_IN=3, TRANSFER=4, DEBIT=5
types = np.random.choice([1, 2, 3, 4, 5], size=n_samples, p=[0.35, 0.30, 0.20, 0.10, 0.05])
amounts = np.abs(np.random.exponential(5000, n_samples))
oldbalanceOrg = np.abs(np.random.exponential(50000, n_samples))

# Generate labels - fraud is more likely for TRANSFER and CASH_OUT with specific patterns
isFraud = np.zeros(n_samples, dtype=str)

for i in range(n_samples):
    # Fraud pattern: TRANSFER(4) or CASH_OUT(1) with high amount and balance drained to 0
    if types[i] in [1, 4]:
        newbalanceOrig_val = oldbalanceOrg[i] - amounts[i]
        if newbalanceOrig_val < 0:
            newbalanceOrig_val = 0.0
        if amounts[i] > oldbalanceOrg[i] * 0.8 and np.random.random() < 0.7:
            isFraud[i] = "Fraud"
        else:
            isFraud[i] = "No Fraud"
    else:
        newbalanceOrig_val = oldbalanceOrg[i] - amounts[i]
        if newbalanceOrig_val < 0:
            newbalanceOrig_val = 0.0
        isFraud[i] = "No Fraud"

# Rebuild newbalanceOrig array
newbalanceOrig = np.maximum(oldbalanceOrg - amounts, 0)

# For fraud cases, set newbalanceOrig to 0 (typical pattern)
fraud_mask = isFraud == "Fraud"
newbalanceOrig[fraud_mask] = 0.0

X = np.column_stack([types, amounts, oldbalanceOrg, newbalanceOrig])
y = isFraud

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f"Model accuracy: {score:.4f}")

# Save model
pickle.dump(model, open("static/model.pkl", "wb"))
pickle.dump(model, open("model.pkl", "wb"))
print("Model saved to static/model.pkl and model.pkl")
