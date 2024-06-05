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
    
    centers = pd.DataFrame(kmeans.cluster_centers_, columns=syms)
    fig, axes = plt.subplots(5, 1, figsize=(5,5), sharex=True)
    for i, ax in enumerate(axes):
        center = centers.loc[i, :]
        maxPC = 1.01 * center.abs().to_numpy().max()
        colors = ['red' if l < 0 else 'blue' for l in center] # type: ignore
        ax.axhline(color='#888888')
        center.plot.bar(ax=ax, color=colors) # type: ignore
        ax.set_ylabel(f'Cluster{i+1}')
        ax.set_ylim(-maxPC, maxPC)
    plt.show()

if __name__ == "__main__":
    main()
