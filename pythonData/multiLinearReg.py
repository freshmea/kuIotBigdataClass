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
    outcome = 'AdjSalePrice'
    predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
    house_lm = LinearRegression()
    house_lm.fit(house[predictors], house[outcome]) # 핵심 훈련 코드
    print(f"intercept: {house_lm.intercept_:.3f}")
    print(f"Coefficients: ")
    for name, coef in zip(predictors, house_lm.coef_):
        print(f"\t{name}: {coef:.3f}")
    regidue = house[outcome] - house_lm.predict(house[predictors]) # 예측 코드
    print(f"residuals mean: {regidue.mean():.3f}")
    print(f"residuals std: {regidue.std():.3f}")
    print(f"residuals : {regidue}")
    
    test_data = pd.Series([2500, 5000, 3, 4, 7], index=predictors)
    print(house_lm.predict([test_data])) #type: ignore
    
    #RMSE
    print(f"RMSE: {np.sqrt(np.mean(regidue**2)):.3f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(house[outcome],house_lm.predict(house[predictors]))):.3f}")
    r2 = r2_score(house[outcome], house_lm.predict(house[predictors]))
    print(f"R2: {r2:.3f}")
    model = sm.OLS(house[outcome], house[predictors])
    results = model.fit()
    print(results.summary())
    # RSE
    print(f"RSE: {np.sqrt(results.mse_resid):.3f}")
    # MAE (Mean Absolute Error)
    print(f"MAE: {np.mean(np.abs(regidue)):.3f}")
    # MAPE (Mean Absolute Percentage Error)
    print(f"MAPE: {np.mean(np.abs(regidue/house[outcome])):.3f}")

if __name__ == "__main__":
    main()
