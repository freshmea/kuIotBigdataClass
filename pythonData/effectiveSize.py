import numpy as np
import pandas as pd
import scipy.stats as statsmodule
import statsmodels.api as sm
import statsmodels.formula.api as smf


def main():
    effect_size = sm.stats.proportion_effectsize(0.0121, 0.011)
    analysis = sm.stats.TTestIndPower()
    result = analysis.solve_power(effect_size=effect_size, alpha=0.05, power=0.8, alternative="larger")
    print(f"Sample size: {result:.2f}")

if __name__ == "__main__":
    main()