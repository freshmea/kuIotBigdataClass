import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def perm_test(df: pd.DataFrame):
    df = df.copy()
    df["Time"] = np.random.permutation(df["Time"].values) # type: ignore
    return df.groupby("Page").std().values[0]

def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    four_session = pd.read_csv(folder + "four_sessions.csv")
    print(four_session.head())
    print(four_session.info())
    # fig = plt.figure()
    # ax = fig.add_subplot()
    # four_session.boxplot(by="Page", column="Time", ax=ax)
    # plt.show()

    observed_variance = four_session.groupby("Page").std().values.ravel()
    observed_mean = four_session.groupby("Page").mean().values.ravel()
    print(f"observed mean: {observed_mean}")
    print(f"observed variance: {observed_variance}")

    perm_variance = [perm_test(four_session) for _ in range(3000)]
    print(f"Pr(Prob) of permuted variance: \
        {np.mean([var > observed_variance for var in perm_variance ])}")
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.hist(perm_variance, bins=11, rwidth=0.9, cumulative=True, density=True)
    for v in observed_variance:
        ax.axvline(x=v, color='black', lw=2)
    ax.text(60, 200, "Observed\nvariance", bbox={'facecolor': 'white'})
    ax.set_xlabel("Session time variance")
    ax.set_ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    main()
