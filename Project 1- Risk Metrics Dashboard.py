# ======================================================
# Project 1: Risk Metrics Dashboard
# ======================================================

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Download MSFT & S&P500 data
msft = yf.download("MSFT", start="2020-01-01")[["Close"]]
sp500 = yf.download("^GSPC", start="2020-01-01")[["Close"]]
data = pd.concat([msft, sp500], axis=1).dropna()
data.columns = ["MSFT", "SP500"]

# 2. Compute daily log returns
ret_msft = np.log(data["MSFT"]).diff().dropna()
ret_sp500 = np.log(data["SP500"]).diff().dropna()

# 3. Volatility & Sharpe ratio
vol_msft = ret_msft.std() * np.sqrt(252)
mean_msft = ret_msft.mean() * 252
sharpe_msft = mean_msft / vol_msft

# 4. Information ratio
active = ret_msft - ret_sp500
te = active.std() * np.sqrt(252)
ir = (active.mean() * 252) / te

# 5. Max Drawdown
cum_max = data["MSFT"].cummax()
drawdown = data["MSFT"] / cum_max - 1
max_dd = drawdown.min()

# 6. VaR & CVaR
alpha = 0.05
VaR = np.percentile(ret_msft, 100*alpha)
CVaR = ret_msft[ret_msft <= VaR].mean()

print("Volatility:", vol_msft)
print("Sharpe:", sharpe_msft)
print("Information Ratio:", ir)
print("Max Drawdown:", max_dd)
print("VaR (5%):", VaR)
print("CVaR (5%):", CVaR)

# Plots
(1+ret_msft).cumprod().plot(title="Equity Curve MSFT")
plt.savefig("equity_curve.png", dpi=150)
plt.close()

drawdown.plot(title="Drawdown MSFT")
plt.savefig("drawdown.png", dpi=150)
plt.close()

ret_msft.hist(bins=50)
plt.title("Histogram of MSFT returns")
plt.savefig("histogram.png", dpi=150)
plt.close()