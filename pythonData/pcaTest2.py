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
    syms =sorted(['AAPL', 'MSFT', 'CSCO', 'INTC', 'CVX', 'XOM', 'SLB', 'COP', 'JPM', 'WFC', 'USB', 'AXP', 'WMT', 'TGT', 'HD', 'COST'])
    top_sp = sp500_px.loc[sp500_px.index >= '2011-01-01', syms]
    print(top_sp.info())
    sp_pca = PCA()
    sp_pca.fit(top_sp)

    explained_variance = pd.DataFrame(sp_pca.explained_variance_)
    # ax = explained_variance.head(10).plot.bar(legend=False)
    # ax.set_xlabel('Component')
    # plt.show()

    loadings = pd.DataFrame(sp_pca.components_[0:5, :], columns=top_sp.columns)
    print(loadings)
    maxPC = 1.01 * loadings.abs().to_numpy().max()

    fig = plt.figure()
    axes = []
    for i in range(5):
        axes.append(fig.add_subplot(5,1,i+1))
    for i, ax in enumerate(axes):
        pc_loadings = loadings.loc[i, :]
        colors = ['red' if l < 0 else 'blue' for l in pc_loadings] # type: ignore
        ax.axhline(color='#888888')
        pc_loadings.plot.bar(ax=ax, color=colors) # type: ignore
        ax.set_ylabel(f'PC{i+1}')
        ax.set_ylim(-maxPC, maxPC)
    plt.show()
    
    # clustering by PCA
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(top_sp)
    top_sp['cluster'] = kmeans.labels_
    
    # plot
    fig = plt.figure()
    ax = fig.add_subplot()
    for cluster, data in top_sp.groupby('cluster'):
        ax.scatter(data['AAPL'], data['MSFT'], label=cluster)
        ax.legend(title='Cluster')
    plt.show()



if __name__ == '__main__':
    main()
