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
    print(house['PropertyType'].head())
    print(house['PropertyType'].value_counts())
    house_oneHot = pd.get_dummies(house['PropertyType'])
    house['NewConstruction'] = [1 if nc else 0 for nc in house['NewConstruction']]
    house_oneHot['Single Family'] = [1 if pt == 'Single Family' else 0 for pt in house['PropertyType']]
    house_oneHot['Townhouse'] = [1 if pt == 'Townhouse' else 0 for pt in house['PropertyType']]
    house_oneHot['Multiplex'] = [1 if pt == 'Multiplex' else 0 for pt in house['PropertyType']]
    
    print(house_oneHot.head())
    print(house_oneHot.info())
    outcome = 'AdjSalePrice'
    predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade', 'PropertyType', 'NbrLivingUnits', 'SqFtFinBasement', 'YrBuilt', 'YrRenovated', 'NewConstruction']
    # model train
    house = pd.concat([house, house_oneHot], axis=1)
    predictors.append('Single Family')
    predictors.append('Townhouse')
    predictors.append('Multiplex')
    # delete PropertyType
    predictors.remove('PropertyType')
    model = LinearRegression()
    model.fit(house[predictors], house[outcome])
    print(f"intercept: {model.intercept_:.3f}")
    print(f"Coefficients: ")
    for name, coef in zip(predictors, model.coef_):
        print(f"\t{name}: {coef:.3f}")



if __name__ == "__main__":
    main()
