from math import exp, sqrt, comb


def binomial_price(
    initial_price: float,
    strike_price: float,
    volatility: float,
    risk_free_rate: float,
    expiry_time: float,
    iterations: int,
    k: int,
    american: bool = False,
) -> float:

    n = iterations  # number of iterations

    mu = risk_free_rate - 0.5 * volatility**2
    g, p = mean_var_to_binomial(
        mean=mu * expiry_time / n, variance=volatility**2 * expiry_time / n, k=k
    )

    dp = {
        n: {
            j: price_if_exercised(
                time=n,
                increments_up=j,
                initial_price=initial_price,
                g=g,
                strike_price=strike_price,
                k=k,
            )
            for j in range(k * (n + 1))
        }
    }
    for i in range(n - 1, -1, -1):
        dp[i] = {}
        for j in range(i * k + 1):
            dp[i][j] = sum(
                dp[i + 1][j + r] * comb(k, r) * (p**r) * ((1 - p) ** (k - r))
                for r in range(k + 1)
            ) * exp(-risk_free_rate * expiry_time / n)
            if american:
                # Calculate current price to sell
                sell_now = price_if_exercised(
                    time=i,
                    increments_up=j,
                    initial_price=initial_price,
                    g=g,
                    strike_price=strike_price,
                    k=k,
                ) * exp((n - i) * risk_free_rate * expiry_time / n)
                if sell_now > dp[i][j]:
                    dp[i][j] = sell_now

    return dp[0][0]


def price_if_exercised(time, increments_up, initial_price, g, strike_price, k):
    # If there have been r increments up, then there have been ik - r increments down (as the total possible increase is ik).
    # Therefore, the total change is exp((r - (ik - r))g/k) = exp((2r/k - i)g).
    return max(
        0, initial_price * exp((2 * increments_up / k - time) * g) - strike_price
    )


def mean_var_to_binomial(mean, variance, k):
    """
    Finds parameters g and p of a binomial random variable
    (which takes values over g(2X/k - 1)), that has mean and variance given.
    """
    g = sqrt(mean**2 + variance * k)
    return g, (mean + g) / (2 * g)
