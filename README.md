# risk-ml-finance

# Risk & Machine Learning in Finance

This repository showcases several projects I developed to practice and demonstrate key skills in **risk management, quantitative finance, and applied machine learning**.

The projects are written in Python, using `pandas`, `numpy`, `matplotlib`, and `yfinance`.  
They are designed to be clear, reproducible, and relevant for **interviews in risk management / quant roles**.

---
## Projects

### [Project 1: Risk Metrics Dashboard](Project1_RiskMetricsDashboard)
- Computes key risk metrics: **Volatility, Sharpe ratio, Information Ratio, Max Drawdown, VaR, CVaR**
- Assets: Microsoft (MSFT) vs S&P500 (^GSPC)
- Includes visualizations: equity curve, drawdown, histogram of returns

### [Project 2: Rolling Metrics & Regimes](Project2_RollingMetricsRegimes)
- 60-day rolling **volatility, Sharpe, Max Drawdown**
- Simple regime classification (high/low volatility)
- Multi-asset comparison: SPY (equities) vs TLT (bonds)

### [Project 3: Portfolio Optimizer (Markowitz)](Project3_PortfolioOptimizer)
- Efficient frontier with multiple assets
- Minimum-variance portfolio construction
- Visualization of risk-return tradeoff

### [Project 4: ML Forecasting](Project4_MLForecasting)
- Predicts asset return direction with **Decision Trees & Random Forests**
- Features: moving averages, rolling volatility, momentum
- Evaluation with accuracy & confusion matrix

### [Project 5: Option Pricing (Monte Carlo)](Project5_OptionPricingMonteCarlo)
- Prices **European call and put options** using **Monte Carlo simulation**
- Simulates stock price paths under **Geometric Brownian Motion (GBM)**
- Estimates the **expected discounted payoff**
- Compares simulation results against the **Black–Scholes closed-form solution**

### [Project 6: Stress Testing](Project6_StressTesting)
- Models portfolio behavior under **extreme market scenarios**
- Applies shocks to **returns, volatility, and correlations**
- Measures impact on **portfolio value and risk metrics**
- Provides insights into **downside risk under stress conditions**

---

## Installation & Run

Clone the repository:
```bash
git clone https://github.com/1cekubesv1/risk-ml-finance.git
cd risk-ml-finance
