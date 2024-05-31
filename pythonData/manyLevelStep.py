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
    print(house['ZipCode'].value_counts().transpose())
    
    predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
    outcome = 'AdjSalePrice'
    
    house_lm = LinearRegression()
    house_lm.fit(house[predictors], house[outcome])
    
    zip_group = pd.DataFrame([
        *pd.DataFrame({
            'ZipCode': house['ZipCode'],
            'residue' : house[outcome] - house_lm.predict(house[predictors])
        })
        .groupby('ZipCode')
        .apply(lambda x: {
            'ZipCode': x['ZipCode'].iloc[0],
            'count': len(x),
            'median_residual': x['residue'].median(),
        })
    ]).sort_values('median_residual')
    zip_group['cum_count'] = np.cumsum(zip_group['count'])
    zip_group['ZipGroup'] = pd.qcut(zip_group['cum_count'], 10, labels=False, retbins=False)
    print(zip_group.head())
    print(zip_group.info())
    print(zip_group['ZipGroup'].value_counts())
    
    to_join = zip_group[['ZipCode', 'ZipGroup']].set_index('ZipCode')
    house = house.join(to_join, on='ZipCode')
    house['ZipCode'] = house['ZipGroup'].astype('category')
    predictors.append('ZipGroup')
    model = LinearRegression()
    model.fit(house[predictors], house[outcome])
    print(f"intercept: {model.intercept_:.3f}")
    print(f"Coefficients: ")
    for name, coef in zip(predictors, model.coef_):
        print(f"\t{name}: {coef:.3f}")


if __name__ == "__main__":
    main()
