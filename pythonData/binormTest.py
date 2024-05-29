import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats


def main():
    print(stats.binom.pmf(2, n=5, p=0.1))
    print(stats.binom.cdf(2, n=5, p=0.1))
    
    print(stats.poisson.rvs(2, size=100))
    print(stats.poisson.rvs(2, size=100).mean())
    print(stats.expon.rvs(scale=1/0.2, size=100).mean())
    print(stats.expon.rvs(scale=5, size=100).mean())

if __name__ == "__main__":
    main()
