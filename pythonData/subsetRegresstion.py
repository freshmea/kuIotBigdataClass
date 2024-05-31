import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from dmba import AIC_score, stepwise_selection
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
    
    y = house[outcome]
    
    def train_model(variables):
        if len(variables) == 0:
            return None
        model = LinearRegression()
        model.fit(X[variables], y)
        return model

    def score_model(model, variables):
        if len(variables) == 0:
            return AIC_score(y, [y.mean()] * len(y), model, df=1)
        return AIC_score(y, model.predict(X[variables]), model)
    
    best_model, best_variables = stepwise_selection(X.columns, train_model, score_model, verbose=True) #type: ignore
    print(f"Intercept: {best_model.intercept_:.3f}")
    print("Coefficients: ")
    for name, coef in zip(best_variables, best_model.coef_):
        print(f"\t{name}: {coef:.3f}")


if __name__ == "__main__":
    main()
