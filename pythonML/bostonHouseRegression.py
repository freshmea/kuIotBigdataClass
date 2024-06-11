import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge, SGDRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
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

    modelnames = ["Linear", "Lasso", "Ridge", "SGD"]
    models = []
    models.append(model)
    models.append(lasso_model)
    models.append(ridge_model)
    models.append(sgd_model)
    
    model.fit(X_train, y_train)
    lasso_model.fit(X_train, y_train)
    ridge_model.fit(X_train, y_train)
    sgd_model.fit(X_train, y_train)
    
    for m, modelName in zip(models, modelnames):
        print(f"{modelName} Coefficients:{m.coef_}")
    print("-------------------------")
    for m, modelName in zip(models, modelnames):
        print(f"{modelName} Intercept:{m.intercept_}")

    print(model.predict(x_data[:5]))
    print(x_data[:5].dot(model.coef_.T) + model.intercept_)

    y_true = y_test.copy()
    y_hats = []
    for m in models:
        y_hats.append(m.predict(X_test))
    for y_hat, modelName in zip(y_hats, modelnames):
        print(f"{modelName} R2 Score:{r2_score(y_true, y_hat)}")
        print(f"{modelName} MSE:{mean_squared_error(y_true, y_hat)}")
        print(f"{modelName} RMSE:{np.sqrt(mean_squared_error(y_true, y_hat))}")
        print(f"{modelName} MAE:{mean_absolute_error(y_true, y_hat)}")

if __name__ == '__main__':
    main()

