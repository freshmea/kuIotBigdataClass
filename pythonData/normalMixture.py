import matplotlib.pyplot as plt
import pandas as pd
from sklearn.mixture import GaussianMixture


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_px = pd.read_csv(folder + "sp500_data.csv", index_col=0)
    df = sp500_px.loc[sp500_px.index >= '2011-01-01', ['XOM', 'CVX']]

    mclust = GaussianMixture(n_components=2).fit(df)
    print(mclust.bic(df))
    
    print(f"Mean {mclust.means_}")
    print(f"Covariances {mclust.covariances_}")
    
    # graph
    fig, ax = plt.subplots()
    colors = [f'C{c}' for c in mclust.predict(df)]
    df.plot.scatter(x='XOM', y='CVX', c=colors, alpha=0.5, ax=ax)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    plt.show()


if __name__ == "__main__":
    main()
