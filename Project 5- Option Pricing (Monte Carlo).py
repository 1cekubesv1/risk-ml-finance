# ======================================================
# Project 5: Option Pricing (Monte Carlo)
# ======================================================

import numpy as np

# Parameters
S0 = 100      # initial price
K = 100       # strike
T = 1         # maturity
r = 0.05      # risk-free rate
sigma = 0.2   # volatility
N = 100000    # number of simulations

# 1. European Call (Black-Scholes MC)
Z = np.random.standard_normal(N)
ST = S0 * np.exp((r - 0.5*sigma**2)*T + sigma*np.sqrt(T)*Z)
payoff = np.maximum(ST-K,0)
price = np.exp(-r*T) * np.mean(payoff)
print("European Call (MC):", price)

# 2. Asian Call (average price)
steps = 50
dt = T/steps
paths = np.zeros((steps+1, N))
paths[0] = S0
for t in range(1, steps+1):
    Z = np.random.standard_normal(N)
    paths[t] = paths[t-1] * np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)
asian_payoff = np.maximum(paths.mean(axis=0)-K,0)
asian_price = np.exp(-r*T) * np.mean(asian_payoff)
print("Asian Call (MC):", asian_price)

# 3. Barrier Option (Down-and-Out)
barrier = 90
knocked_out = (paths.min(axis=0) < barrier)
barrier_payoff = np.where(knocked_out, 0, np.maximum(paths[-1]-K,0))
barrier_price = np.exp(-r*T) * np.mean(barrier_payoff)
print("Down-and-Out Call (MC):", barrier_price)