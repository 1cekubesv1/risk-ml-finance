# ======================================================
# Project 3: Portfolio Optimizer (Markowitz)
# ======================================================

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# 1. Download data
assets = ["AAPL", "MSFT", "SPY", "TLT"]
data = yf.download(assets, start="2020-01-01")["Close"].dropna()
returns = np.log(data).diff().dropna()

# 2. Mean & covariance
mean_ret = returns.mean() * 252
cov_matrix = returns.cov() * 252

# 3. Simulate portfolios
N = 5000
results = np.zeros((3,N))

for i in range(N):
    weights = np.random.random(len(assets))
    weights /= np.sum(weights)
    port_return = np.dot(weights, mean_ret)
    port_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe = port_return / port_vol
    results[0,i] = port_return
    results[1,i] = port_vol
    results[2,i] = sharpe

# 4. Plot efficient frontier
plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap="viridis", s=10)
plt.colorbar(label="Sharpe Ratio")
plt.xlabel("Volatility"); plt.ylabel("Return")
plt.title("Efficient Frontier")
plt.savefig("efficient_frontier.png", dpi=150)
plt.close()