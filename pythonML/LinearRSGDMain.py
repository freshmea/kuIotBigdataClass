# 실패 코드 ..

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# from LinearRSGDTest import LinearRegressionSGD
from sklearn.linear_model import SGDRegressor


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    df = pd.read_csv(folder +"house_sales.csv", sep="\t")
    
    # predictors = ["SqFtLot", "SqFtTotLiving", "YrBuilt"]
    predictors = ["SqFtTotLiving"]
    target = "SalePrice"
    # print(df.head())
    # print(df.info())
    X = df[predictors].values
    y = df[target].values
    print(X.shape, y.shape)
    
    gd_lr = SGDRegressor(eta0=0.001, n_iter_no_change=10000, shuffle=False)
    sgd_lr = SGDRegressor(eta0=0.001, n_iter_no_change=10000, shuffle=True)
    
    gd_lr.fit(X, y) #type : ignore
    sgd_lr.fit(X, y) #type : ignore
    print(gd_lr.loss_functions)
    # plt.plot(range(len(gd_lr.loss_functions)), gd_lr.loss_curve_, label="GD")

if __name__ == "__main__":
    main()

