import random
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def perm_func(x :pd.Series, nA, nB):
    n = nA + nB
    idx_b = set(random.sample(range(n), nB))
    idx_a = set(range(n)) - idx_b
    return x.loc[list(idx_b)].mean() - x.loc[list(idx_a)].mean()

def main():
    aSize = 23739
    bSize = 22588
    aOne = 200
    bOne = 182

    obs_pct_diff = 100 * (bOne / bSize - aOne / aSize)
    random.seed(time.time())
    print(f"Observed difference: {obs_pct_diff:.4f}%")
    conversion = [0] * (aSize + bSize - aOne - bOne)
    conversion.extend([1] * (aOne + bOne))
    conversion = pd.Series(conversion)

    perm_diffs = [100 * perm_func(conversion, aSize, bSize) for _ in range(1000)]

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.hist(perm_diffs, bins=11, rwidth=0.9)
    ax.axvline(x=obs_pct_diff, color='black', lw=2)
    ax.text(0.5, 100, 'Observed\ndifference', bbox={'facecolor': 'white'})
    ax.set_xlabel("Conversion rate (percent)")
    ax.set_ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    main()
