import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_px = pd.read_csv(folder + "sp500_data.csv", index_col=0)
    df = sp500_px.loc[sp500_px.index >= '2011-01-01', ['XOM', 'CVX']]
    kmeans = KMeans(n_clusters=4, n_init='auto').fit(df)
    df['cluster'] = kmeans.labels_
    print(df)
    centers = pd.DataFrame(kmeans.cluster_centers_, columns=['XOM', 'CVX'])
    print(centers)
    
    fig, ax = plt.subplots()
    ax = sns.scatterplot(x='XOM', y='CVX', hue='cluster', style='cluster', ax=ax, data=df)
    centers.plot.scatter(x='XOM', y='CVX', ax=ax, s=50, color='black')
    plt.show()

if __name__ == "__main__":
    main()
