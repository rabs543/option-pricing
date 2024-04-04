from matplotlib import pyplot as plt
import numpy as np

from bernoulli import bernoulli_price
from black_scholes.black_scholes import black_scholes_price

n_0 = 1
r = 2
s = 5

parameters = {
    "strike_price": 40,
    "initial_price": 40,
    "volatility": 0.5,
    "risk_free_rate": 0.035,
    "expiry_time": 2,
}


def approximator(n):
    return bernoulli_price(**parameters, iterations=n)

x_values = [n_0 * r**i for i in range(s)]
y_values = [approximator(x) for x in x_values]
degree = len(x_values)
black_scholes_price=black_scholes_price(**parameters)

# Change of variable: interpolate using a polynomial in x_inv = 1/x
x_inv_values = 1 / np.array(x_values)
coefficients = np.polyfit(x_inv_values, y_values, degree)
polynomial = np.poly1d(coefficients)

# Generate x values for the curve
x_curve_inv = np.linspace(min(x_inv_values) / 5, max(x_inv_values), 100)
x_curve = 1 / x_curve_inv

# Plot the interpolation points
plt.scatter(x_values, y_values, color="red", label="Interpolation points from Bernoulli approximation")

# Plot the polynomial curve
plt.plot(
    x_curve,
    polynomial(x_curve_inv),
    label=f"Interpolated polynomial",
)

plt.axhline(
    y=black_scholes_price,
    color="green",
    linestyle="--",
    label="Black-Scholes price",
)

# Add labels and legend
plt.xlabel("n")
plt.ylabel("Price")
plt.legend()
plt.title("Approximation to option price with r={r} and s={s}".format(r=r, s=s))

plt.grid(True)
plt.savefig("output/extrapolation.png")