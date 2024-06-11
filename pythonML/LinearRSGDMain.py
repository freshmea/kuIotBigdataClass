import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from LinearRSGDTest import LinearRegressionGD
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
    X = x_scaled_data
    y = y_data
    
    gd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, shuffle=False)
    bgd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, shuffle=False, batch_size=X.shape[0])
    sgd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, shuffle=True )
    msgd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, batch_size=100, shuffle=True)
    print("Fitting the models ...")
    print("Gradient Descent")
    gd_lr.fit(X, y)
    print("Batch Gradient Descent")
    bgd_lr.fit(X, y)
    print("Stochastic Gradient Descent")
    sgd_lr.fit(X, y)
    print("Mini-Batch Stochastic Gradient Descent")
    msgd_lr.fit(X, y)

    import matplotlib.pyplot as plt
    plt.plot(range(len(gd_lr.cost_history)), gd_lr.cost_history, label="GD", c="r")
    plt.plot(range(len(bgd_lr.cost_history)), bgd_lr.cost_history, label="BGD", c="g")
    plt.plot(range(len(sgd_lr.cost_history)), sgd_lr.cost_history, label="SGD", c="b")
    plt.plot(range(len(msgd_lr.cost_history)), msgd_lr.cost_history, label="MSGD", c="y")

    plt.show()
    # print(f"w history gd:{gd_lr.weights_history}")
    # print(f"w history bgd:{bgd_lr.weights_history}")
    # print(f"w history sgd:{sgd_lr.weights_history}")
    # print(f"w history msgd:{msgd_lr.weights_history}")
if __name__ == "__main__":
    main()
