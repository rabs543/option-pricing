import itertools
import matplotlib.pyplot as plt
import numpy as np
from bernoulli import bernoulli_price
from black_scholes.black_scholes import black_scholes_price
from extrapolate import extrapolate
from util import interpolate_and_plot


parameters = {
    "strike_price": [40],
    "initial_price": [40],
    "volatility": [0.8],
    "risk_free_rate": [0.035],
    "expiry_time": [10],
}

extrapolation_parameters = {"n_0": 1, "r": 3, "s": 3}

# For rendering in GitHub
f = open("output/example_extrapolated_price_table.txt", "w")
# Render table header
f.write(r"| $c$ | $S_0$ | $\sigma$ | $\rho$ | $t_0$ | Price |")
f.write("\n| --- | --- | --- | --- | --- | --- | \n")

keys = list(parameters)
for values in itertools.product(*map(parameters.get, keys)):

    def approximator(n):
        return bernoulli_price(**dict(zip(keys, values)), iterations=n)

    price = extrapolate(**extrapolation_parameters, approximator=approximator)
    f.write(
        "| {strike_price} | {initial_price} | {volatility} | {risk_free_rate} | {expiry_time} | {price:.2f} |".format(
            **dict(zip(keys, values)), price=price
        )
    )
    f.write("\n")

f.close()

