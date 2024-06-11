import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge, SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonML/"
    df = pd.read_csv(folder + "boston.csv")
    print(df.info())
    print(df.keys())
    data = df.drop(columns=["MEDV"])
    target = df["MEDV"]
    x_data = data.to_numpy()
    y_data = target.to_numpy().reshape(-1, 1)

    minmax_scale = MinMaxScaler(feature_range=(0, 5)).fit(x_data)
    x_scaled_data = minmax_scale.transform(x_data)

    X_train, X_test, y_train, y_test = train_test_split(x_scaled_data, y_data, test_size=0.33)

    model = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=6)
    lasso_model = Lasso(alpha=0.01, fit_intercept=True, copy_X=True)
    ridge_model = Ridge(alpha=0.01, fit_intercept=True, copy_X=True)
    sgd_model = SGDRegressor(penalty="l2", alpha=0.01, max_iter=1000, tol=0.001, eta0=0.01)

    model.fit(X_train, y_train)
    lasso_model.fit(X_train, y_train)
    ridge_model.fit(X_train, y_train)
    sgd_model.fit(X_train, y_train)
    print(f"Linear Coefficients:{model.coef_}")
    print(f"Lasso Coefficients:{lasso_model.coef_}")
    print(f"Ridge Coefficients:{ridge_model.coef_}")
    print(f"SGD Coefficients:{sgd_model.coef_}")
    print("-------------------------")
    print(f"Linear Intercept:{model.intercept_}")
    print(f"Lasso Intercept:{lasso_model.intercept_}")
    print(f"Ridge Intercept:{ridge_model.intercept_}")
    print(f"SGD Intercept:{sgd_model.intercept_}")
    

if __name__ == '__main__':
    main()

