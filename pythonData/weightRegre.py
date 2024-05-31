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
    subset= ['AdjSalePrice', 'SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
    predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
    outcome = 'AdjSalePrice'
    house['Year'] = [int(date.split('-')[0]) for date in house['DocumentDate']]
    house['Weight'] = house['Year'] - 2005
    
    house_lm = LinearRegression()
    house_lm.fit(house[predictors], house[outcome], sample_weight=house['Weight']) # 핵심 훈련 코드
    print(f"intercept: {house_lm.intercept_:.3f}")
    print(f"Coefficients: ")
    for name, coef in zip(predictors, house_lm.coef_):
        print(f"\t{name}: {coef:.3f}")


if __name__ == "__main__":
    main()
