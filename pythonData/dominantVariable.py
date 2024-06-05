import matplotlib.pyplot as plt
import pandas as pd

# PCA
from sklearn.decomposition import PCA


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_px = pd.read_csv(folder + "sp500_data.csv", index_col=0)
    syms =sorted(['AAPL', 'MSFT', 'CSCO', 'INTC', 'CVX', 'XOM', 'SLB', 'COP', 'JPM', 'WFC', 'USB', 'AXP', 'WMT', 'TGT', 'HD', 'COST'])
    df = sp500_px.loc[sp500_px.index >= '2011-01-01', syms]

    sp_pca = PCA().fit(df)
    
    loadings = pd.DataFrame(sp_pca.components_[0:2, :], columns=df.columns)
    print(f"loadings : {loadings.transpose()}")

    explained_variance = pd.DataFrame(sp_pca.explained_variance_)
    fig, ax = plt.subplots()
    ax = explained_variance.head(10).plot.bar(legend=False, ax=ax)
    ax.set_xlabel('Component')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
