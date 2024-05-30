import numpy as np
import scipy.stats as stats


def main():
    aSize = 23739
    bSize = 22588
    aOne = 200
    bOne = 232

    obs_pct_diff = 100 * (bOne / bSize - aOne / aSize)
    print(f"Observed difference: {obs_pct_diff:.4f}%")

    survivors = np.array([[aOne, aSize-aOne],[bOne, bSize-bOne]])
    chi2, p_value, df, _ = stats.chi2_contingency(survivors)
    print(f"p-value for sigle sided test: {p_value/2:.4f}")



if __name__ == "__main__":
    main()
