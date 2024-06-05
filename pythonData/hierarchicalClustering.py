import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, fcluster, linkage


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_px = pd.read_csv(folder + "sp500_data.csv", index_col=0)
    syms =sorted(['AAPL', 'MSFT', 'CSCO', 'INTC', 'CVX', 'XOM', 'SLB', 'COP', 'JPM', 'WFC', 'USB', 'AXP', 'WMT', 'TGT', 'HD', 'COST'])
    df = sp500_px.loc[sp500_px.index >= '2011-01-01', syms].transpose()

    Z = linkage(df, method='ward')
    print(Z)
    print(Z.shape)
    
    
    # cut dendrogram
    memb = fcluster(Z, 4, criterion='maxclust')
    memb = pd.Series(memb, index=df.index)
    for k, idx in memb.groupby(memb):
        print(f'Cluster {k}: {", ".join(idx.index)}')
        
    # dendrogram
    fig, ax = plt.subplots()
    dendrogram(Z, labels=list(df.index), color_threshold=0 ,ax=ax)
    plt.xticks(rotation=90)
    ax.set_ylabel('Distance')
    plt.show()

if __name__ == "__main__":
    main()
