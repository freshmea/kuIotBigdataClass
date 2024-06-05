from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_px = pd.read_csv(folder + "sp500_data.csv", index_col=0)
    syms =sorted(['AAPL', 'MSFT', 'CSCO', 'INTC', 'CVX', 'XOM', 'SLB', 'COP', 'JPM', 'WFC', 'USB', 'AXP', 'WMT', 'TGT', 'HD', 'COST'])
    df = sp500_px.loc[sp500_px.index >= '2011-01-01', syms]
    kmeans = KMeans(n_clusters=5, n_init='auto').fit(df)
    df['cluster'] = kmeans.labels_
    print(df)
    print(df.groupby('cluster').size())
    print(Counter(kmeans.labels_))

    inertia = []
    for n_clusters in range(2, 14):
        kmeans = KMeans(n_clusters=n_clusters, n_init='auto').fit(df)
        inertia.append(kmeans.inertia_ / n_clusters)
    
    inertias = pd.DataFrame({
        'n_clusters' : range(2, 14),
        'inertia' : inertia
    })
    print(inertias)
    ax = inertias.plot(x='n_clusters', y='inertia')
    plt.xlabel('Number of clusters')
    plt.ylabel(('Average Within-Cluster Squared Distances'))
    plt.ylim(0, 1.1 * inertias['inertia'].max())
    plt.show()

if __name__ == "__main__":
    main()
