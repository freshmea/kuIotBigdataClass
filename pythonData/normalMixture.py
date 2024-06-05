import matplotlib.pyplot as plt
import pandas as pd
from sklearn.mixture import GaussianMixture


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_px = pd.read_csv(folder + "sp500_data.csv", index_col=0)
    df = sp500_px.loc[sp500_px.index >= '2011-01-01', ['XOM', 'CVX']]

    results = []
    covariance_types = ['full', 'tied', 'diag', 'spherical']
    for n_components in range(1, 9):
        for covariance_type in covariance_types:
            mclust = GaussianMixture(n_components=n_components, covariance_type=covariance_type).fit(df)
            results.append({
                'bic' : mclust.bic(df),
                'n_components' : n_components,
                'covariance_type' : covariance_type,
            })
    results = pd.DataFrame(results)

    colors = ['red', 'blue', 'green', 'purple']
    styles = ['-', '--', '-.', ':']

    # graph
    fig, ax = plt.subplots()
    for i, covariance_type in enumerate(covariance_types):
        subset = results.loc[results['covariance_type'] == covariance_type]
        subset.plot(x='n_components', y='bic', ax=ax, label=covariance_type, kind='line', color=colors[i], style=styles[i])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
