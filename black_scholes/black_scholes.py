from scipy.stats import norm
from math import sqrt, log, exp


def black_scholes_price(
    initial_price: float,
    strike_price: float,
    volatility: float,
    risk_free_rate: float,
    expiry_time: float,
) -> float:
    x0 = 1 / (volatility * sqrt(expiry_time))

    x1 = (
        log(initial_price / strike_price)
        + (risk_free_rate + 0.5 * volatility**2) * expiry_time
    ) * x0

    x2 = (
        log(initial_price / strike_price)
        + (risk_free_rate - 0.5 * volatility**2) * expiry_time
    ) * x0

    return initial_price * norm.cdf(x1) - strike_price * exp(
        -risk_free_rate * expiry_time
    ) * norm.cdf(x2)
