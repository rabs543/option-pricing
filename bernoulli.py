from math import exp, sqrt


def bernoulli_price(
    initial_price: float,
    strike_price: float,
    volatility: float,
    risk_free_rate: float,
    expiry_time: float,
    iterations: int,
) -> float:

    n = iterations  # number of iterations

    mu = risk_free_rate - 0.5 * volatility**2
    g, p = mean_var_to_bernoulli(
        mean=mu * expiry_time / n, variance=volatility**2 * expiry_time / n
    )

    dp = {
        n: {
            j: max(0, initial_price * exp((2 * j - n) * g) - strike_price)
            for j in range(n + 1)
        }
    }
    for i in range(n - 1, -1, -1):
        dp[i] = {}
        for j in range(i + 1):
            dp[i][j] = (p * dp[i + 1][j + 1] + (1 - p) * dp[i + 1][j]) * exp(
                -risk_free_rate * expiry_time / n
            )

    return dp[0][0]


def mean_var_to_bernoulli(mean, variance):
    """
    Finds parameters g and p of a Bernoulli-like random variable
    (which takes values g, -g w.p. p, 1-p respectively), that has mean and variance given.
    """
    x = mean**2 + variance
    return sqrt(x), (mean * sqrt(x) + x) / (2 * x)
