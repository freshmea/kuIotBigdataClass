import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import OLSInfluence


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    house : pd.DataFrame = pd.read_csv(folder + "house_sales.csv", sep='\t')
    print(house.head())
    print(house.info())
    house_98105 = house.loc[house['ZipCode'] == 98105, :]
    predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
    outcome = 'AdjSalePrice'
    print(house.groupby('ZipCode')['AdjSalePrice'].mean())

    house_outlier = sm.OLS(house_98105[outcome], house_98105[predictors].assign(const=1))
    results_98105 = house_outlier.fit()
    influence = OLSInfluence(results_98105)
    fig = plt.figure()
    ax = fig.add_subplot()
    sns.regplot(x = results_98105.fittedvalues, y = np.abs(results_98105.resid),
                scatter_kws={'alpha': 0.5}, line_kws={'color': 'C1'}, lowess=True, ax=ax)
    ax.set_xlabel('predicted')
    ax.set_ylabel('abs(residual)')
    plt.show()

if __name__ == "__main__":
    main()
