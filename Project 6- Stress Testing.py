# ======================================================
# Project 6: Stress Testing
# ======================================================

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# 1. Download SP500
sp500 = yf.download("^GSPC", start="2020-01-01")["Close"]
returns = np.log(sp500).diff().dropna()

# 2. Metrics baseline
vol = returns.std()*np.sqrt(252)
mean = returns.mean()*252
sharpe = mean/vol

print("Baseline Vol:", vol)
print("Baseline Sharpe:", sharpe)

# 3. Apply shock (-20%)
shock = returns - 0.20
vol_shock = shock.std()*np.sqrt(252)
mean_shock = shock.mean()*252
sharpe_shock = mean_shock/vol_shock

print("Shocked Vol:", vol_shock)
print("Shocked Sharpe:", sharpe_shock)

# 4. Plot cumulative returns
(1+returns).cumprod().plot(label="Baseline")
(1+shock).cumprod().plot(label="Stress -20%")
plt.legend()
plt.title("Stress Testing Scenario")
plt.savefig("stress_test.png", dpi=150)
plt.close()