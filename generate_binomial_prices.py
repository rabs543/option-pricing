import itertools
from binomial import binomial_price

# Some example parameters
parameters = {
    "strike_price": [40],
    "initial_price": [50, 100],
    "volatility": [0.5],
    "risk_free_rate": [0.035],
    "expiry_time": [2, 3],
    "k": [10]
}

# For rendering in GitHub
f = open("output/example_binomial_price_table.txt", "w")
# Render table header
f.write(r"| $c$ | $S_0$ | $\sigma$ | $\rho$ | $t_0$ | Price |")
f.write("\n| --- | --- | --- | --- | --- | --- | \n")

keys = list(parameters)
for values in itertools.product(*map(parameters.get, keys)):
    price = binomial_price(**dict(zip(keys, values)), iterations=27)
    f.write(
        "| {strike_price} | {initial_price} | {volatility} | {risk_free_rate} | {expiry_time} | {price:.2f} |".format(
            **dict(zip(keys, values)), price=price
        )
    )
    f.write("\n")

f.close()
