import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    loan200 : pd.DataFrame = pd.read_csv(folder + "loan200.csv")
    print(loan200.head())
    print(loan200.info())

    predictors = ['payment_inc_ratio', 'dti']
    outcome = 'outcome'

    newloan = loan200.loc[0:0, predictors]
    X = loan200.loc[1:, predictors]
    y = loan200.loc[1:, outcome]

    knn = KNeighborsClassifier(n_neighbors=20)
    knn.fit(X, y)
    result = knn.predict(newloan)
    print(f"result: {result}")

if __name__ == "__main__":
    main()
