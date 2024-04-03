import itertools
from black_scholes import black_scholes_price

# Some example parameters
parameters = {
    "strike_price": [40],
    "initial_price": [50, 100],
    "volatility": [0.5],
    "risk_free_rate": [0.035],
    "expiry_time": [2, 3],
}

# For rendering in GitHub
f = open("output/example_black_scholes_price_table.txt", "w")
# Render table header
f.write(r"| $c$ | $S_0$ | $\sigma$ | $\rho$ | $t_0$ | Price |")
f.write("\n| --- | --- | --- | --- | --- | --- | \n")

keys = list(parameters)
for values in itertools.product(*map(parameters.get, keys)):
    price = black_scholes_price(**dict(zip(keys, values)))
    f.write(
        "| {strike_price} | {initial_price} | {volatility} | {risk_free_rate} | {expiry_time} | {price:.2f} |".format(
            **dict(zip(keys, values)), price=price
        )
    )
    f.write("\n")

f.close()
