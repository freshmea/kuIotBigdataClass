import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import OLSInfluence


def partialResidualPlot(model, df, outcome, predictor, ax):
    y_pred = model.predict(df)
    copy_df = df.copy()
    for c in copy_df.columns:
        if c == predictor:
            continue
        copy_df[c] = 0.0
    feature_prediction = model.predict(copy_df)
    results = pd.DataFrame({
        'feature': df[predictor],
        'residual': df[outcome] - y_pred,
        'ypartial': feature_prediction - model.params[0]
    })
    results = results.sort_values('feature')
    smoothed = sm.nonparametric.lowess(results['ypartial'], results['feature'], frac=1/3)
    
    ax.scatter(results['feature'], results['ypartial']+ results['residual'])
    ax.plot(smoothed[:,0], smoothed[:,1], 'red')
    ax.plot(results['feature'], results['ypartial'], 'green')
    ax.set_xlabel(predictor)
    ax.set_ylabel(f'Residual + {predictor} contribution')
    return ax

def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    house : pd.DataFrame = pd.read_csv(folder + "house_sales.csv", sep='\t')
    print(house.head())
    print(house.info())
    house_98105 = house.loc[house['ZipCode'] == 98105, :]
    predictors = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
    outcome = 'AdjSalePrice'
    print(house.groupby('ZipCode')['AdjSalePrice'].mean())

    # # polynomial
    # model_poly = smf.ols(formula='AdjSalePrice ~ SqFtTotLiving + np.power(SqFtTotLiving, 2) + SqFtLot + Bathrooms + Bedrooms + BldgGrade', data=house_98105)
    # result_poly = model_poly.fit()
    # print(result_poly.summary())
    # base spline
    formula = 'AdjSalePrice ~ bs(SqFtTotLiving, df=6, degree=3) + SqFtLot + Bathrooms + Bedrooms + BldgGrade'
    model_spline = smf.ols(formula=formula, data=house_98105)
    result_spline = model_spline.fit()
    print(result_spline.summary())
    
    fig = plt.figure()
    ax = fig.add_subplot()
    # partialResidualPlot(result_poly, house_98105, 'AdjSalePrice', 'SqFtTotLiving', ax)
    partialResidualPlot(result_spline, house_98105, 'AdjSalePrice', 'SqFtTotLiving', ax)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
