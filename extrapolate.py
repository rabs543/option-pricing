from typing import Callable


def extrapolate(n_0: int, r: int, s: int, approximator: Callable[[int], float]) -> float:
    a = {0: {m: approximator(n_0 * r**m) for m in range(s + 1)}}
    for i in range(1, s + 1):
        a[i] = {}
        for m in range(i, s + 1):
            a[i][m] = a[i - 1][m] + (a[i - 1][m] - a[i - 1][m - 1]) / (r**i - 1)

    return a[s][s]
