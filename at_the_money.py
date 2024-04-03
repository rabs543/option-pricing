import matplotlib.pyplot as plt

from bernoulli import bernoulli_price
from black_scholes.black_scholes import black_scholes_price

parameters = {
    "strike_price": 40,
    "initial_price": 40,
    "volatility": 0.5,
    "risk_free_rate": 0.035,
    "expiry_time": 3,
}

results = {}
for n in range(1, 100):
    results[n] = bernoulli_price(**parameters, iterations=n)

bs_price = black_scholes_price(**parameters)

plt.plot(results.keys(), results.values())
plt.title("Bernoulli approximation to Black-Scholes with increasing iterations")
plt.axhline(bs_price, color="black")
plt.savefig("output/at_the_money.png")
plt.show()
