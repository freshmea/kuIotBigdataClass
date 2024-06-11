# 실패 코드 ..

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from LinearRSGDTest import LinearRegressionGD

# from sklearn.linear_model import SGDRegressor


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
    
    gd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, shuffle=False)
    sgd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, shuffle=True)
    
    gd_lr.fit(X, y) #type : ignore
    sgd_lr.fit(X, y) #type : ignore
    

if __name__ == "__main__":
    main()

