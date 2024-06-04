import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import prince
from adjustText import adjust_text
from sklearn.decomposition import PCA


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    housetasks : pd.DataFrame = pd.read_csv(folder + "housetasks.csv", index_col=0)
    
    ca = prince.CA(n_components=2)
    
    ca = ca.fit(housetasks)
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ca.row_coordinates(housetasks).plot.scatter(x=0, y=1, ax=ax)
    ca.column_coordinates(housetasks).plot.scatter(x=0, y=1, ax=ax, c='C1')
    texts= []
    for idx, row in ca.row_coordinates(housetasks).iterrows():
        texts.append(plt.text(row[0], row[1], idx)) # type: ignore
    for idx, row in ca.column_coordinates(housetasks).iterrows():
        texts.append(plt.text(row[0], row[1], idx, color='C1')) # type: ignore
    adjust_text(texts, only_move={'points':'y', 'texts':'y'})
    plt.tight_layout()
    plt.show()
    
    # sp_pca = PCA()
    # sp_pca.fit(top_sp)

    # explained_variance = pd.DataFrame(sp_pca.explained_variance_)
    # # ax = explained_variance.head(10).plot.bar(legend=False)
    # # ax.set_xlabel('Component')
    # # plt.show()

    # loadings = pd.DataFrame(sp_pca.components_[0:5, :], columns=top_sp.columns)
    # print(loadings)
    # maxPC = 1.01 * loadings.abs().to_numpy().max()

    # fig = plt.figure()
    # axes = []
    # for i in range(5):
    #     axes.append(fig.add_subplot(5,1,i+1))
    # for i, ax in enumerate(axes):
    #     pc_loadings = loadings.loc[i, :]
    #     colors = ['red' if l < 0 else 'blue' for l in pc_loadings] # type: ignore
    #     ax.axhline(color='#888888')
    #     pc_loadings.plot.bar(ax=ax, color=colors) # type: ignore
    #     ax.set_ylabel(f'PC{i+1}')
    #     ax.set_ylim(-maxPC, maxPC)
    # plt.show()
    
    # # clustering by PCA
    # from sklearn.cluster import KMeans
    # from sklearn.preprocessing import StandardScaler
    # kmeans = KMeans(n_clusters=4)
    # kmeans.fit(top_sp)
    # top_sp['cluster'] = kmeans.labels_
    
    # # plot
    # fig = plt.figure()
    # ax = fig.add_subplot()
    # for cluster, data in top_sp.groupby('cluster'):
    #     ax.scatter(data['AAPL'], data['MSFT'], label=cluster)
    #     ax.legend(title='Cluster')
    # plt.show()



if __name__ == '__main__':
    main()
