import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
    sresiduals = influence.resid_studentized_internal
    print(sresiduals.idxmin(), sresiduals.idxmax())

    outlier = house_98105.loc[sresiduals.idxmin(), :]
    print(f"AdjSalePrice: {outlier[outcome]}")
    print(outlier[predictors])
    
if __name__ == "__main__":
    main()
