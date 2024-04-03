# Option pricing
## 1. Black Scholes formula
We assume that the logarithm of the stock price follows a Brownian motion, i.e. if $S_t$ is the stock price at time $t$, then
$$
\log \left( \frac{S_t}{S_0} \right) \sim N(\mu t, \sigma^2 t)
$$
where $\sigma$ is the _volatility_ of the stock, and $\mu = \rho - \frac{\sigma^2}{2}$ where $\rho$ is the risk-free rate. Recall the Black-Scholes formula for the price of an option,
$$
\text{price} = S_0\Phi\left(\frac{\log(S_0/c) + (\rho + \sigma^2/2)t_0}{\sigma \sqrt{t_0}}\right)
-
ce^{-\rho t_0}\Phi\left(\frac{\log(S_0/c) + (\rho - \sigma^2/2)t_0}{\sigma \sqrt{t_0}}\right)
$$
where $c$ is the strike price and $t_0$ is the expiry time. For example, here are some prices which were generated in `generate_example_prices.py`.
| $c$ | $S_0$ | $\sigma$ | $\rho$ | $t_0$ | Price |
| --- | --- | --- | --- | --- | --- | 
| 40 | 50 | 0.5 | 0.035 | 2 | 19.38 |
| 40 | 50 | 0.5 | 0.035 | 3 | 22.35 |
| 40 | 100 | 0.5 | 0.035 | 2 | 64.24 |
| 40 | 100 | 0.5 | 0.035 | 3 | 66.84 |
