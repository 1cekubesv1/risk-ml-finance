# ======================================================
# Project 2: Rolling Metrics & Regimes
# ======================================================

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 1. Download SPY
spy = yf.download("SPY", start="2020-01-01")[["Close"]]
returns = np.log(spy["Close"]).diff().dropna()

# 2. Rolling metrics (60-day)
window = 60
ret = returns.values
roll_vol, roll_sharpe, roll_mdd, dates = [], [], [], []

for t in range(window, len(ret)):
    win = ret[t-window:t]
    vol = win.std() * np.sqrt(252)
    mean = win.mean() * 252
    sharpe = mean / vol if vol > 0 else 0
    prices = spy["Close"].iloc[t-window:t].values
    cum_max = np.maximum.accumulate(prices)
    dd = prices / cum_max - 1
    mdd = dd.min()
    roll_vol.append(vol); roll_sharpe.append(sharpe)
    roll_mdd.append(mdd); dates.append(spy.index[t])

# 3. Plot results
plt.plot(dates, roll_vol); plt.title("Rolling Vol (60d)")
plt.savefig("rolling_vol.png", dpi=150); plt.close()

plt.plot(dates, roll_sharpe); plt.title("Rolling Sharpe (60d)")
plt.savefig("rolling_sharpe.png", dpi=150); plt.close()

plt.plot(dates, roll_mdd); plt.title("Rolling Max Drawdown (60d)")
plt.savefig("rolling_mdd.png", dpi=150); plt.close()

# 4. Simple regime classification
threshold = np.median(roll_vol) * 1.5
regimes = ["HighVol" if v > threshold else "LowVol" for v in roll_vol]
print("Regime counts:", Counter(regimes))