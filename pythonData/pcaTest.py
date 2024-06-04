import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


def abline(slope, intercept, ax):
    x_vals = np.array(ax.get_xlim())
    return(x_vals, intercept + slope * x_vals)

def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_px : pd.DataFrame = pd.read_csv(folder + "sp500_data.csv", index_col=0)
    oil_px = sp500_px[['XOM', 'CVX']]
    print(oil_px.head())
    print(oil_px.info())
    
    pcs = PCA(n_components=2)
    pcs.fit(oil_px)
    loadings = pd.DataFrame(pcs.components_, columns=oil_px.columns)
    print(loadings.head())
    print(loadings.info())
    ax = oil_px.plot.scatter(x='XOM', y='CVX', alpha= 0.3)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.plot(*abline(loadings.loc[0, 'CVX'] / loadings.loc[0, 'XOM'], 0, ax), '--', color='C1') # type: ignore
    ax.plot(*abline(loadings.loc[1, 'CVX'] / loadings.loc[1, 'XOM'], 0, ax), '--', color='blue') # type: ignore
    plt.show()

if __name__ == '__main__':
    main()
