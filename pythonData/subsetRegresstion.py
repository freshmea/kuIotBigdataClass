import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    house : pd.DataFrame = pd.read_csv(folder + "house_sales.csv", sep='\t')
    print(house.head())
    print(house.info())
    outcome = 'AdjSalePrice'
    predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade', 'PropertyType', 'NbrLivingUnits', 'SqFtFinBasement', 'YrBuilt', 'YrRenovated', 'NewConstruction']

    X = pd.get_dummies(house[predictors], drop_first=True, dtype=int)
    X['NewConstruction'] = [1 if nc else 0 for nc in X['NewConstruction']]

    house_full = sm.OLS(house[outcome], X.assign(const=1))
    results = house_full.fit()
    print(results.summary())
    
if __name__ == "__main__":
    main()
