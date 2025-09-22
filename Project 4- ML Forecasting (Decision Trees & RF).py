# ======================================================
# Project 4: ML Forecasting (Decision Trees & RF)
# ======================================================

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Download data
spy = yf.download("SPY", start="2020-01-01")["Close"]
returns = np.log(spy).diff().dropna()

# 2. Features
df = pd.DataFrame(index=returns.index)
df["ret"] = returns
df["ma5"] = returns.rolling(5).mean()
df["ma20"] = returns.rolling(20).mean()
df["vol"] = returns.rolling(20).std()
df["momentum"] = returns.rolling(5).sum()
df["target"] = (returns.shift(-1) > 0).astype(int)
df = df.dropna()

X = df[["ma5","ma20","vol","momentum"]]
y = df["target"]

split = int(len(df)*0.7)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# 3. Models
dt = DecisionTreeClassifier(max_depth=5).fit(X_train, y_train)
rf = RandomForestClassifier(n_estimators=100, max_depth=5).fit(X_train, y_train)

# 4. Accuracy
y_pred_dt = dt.predict(X_test)
y_pred_rf = rf.predict(X_test)

print("Decision Tree accuracy:", accuracy_score(y_test, y_pred_dt))
print("Random Forest accuracy:", accuracy_score(y_test, y_pred_rf))