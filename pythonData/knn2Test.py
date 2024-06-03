import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    loan_data : pd.DataFrame = pd.read_csv(folder + "loan_data.csv.gz")
    print(loan_data.head())
    print(loan_data.info())

    predictors = ['payment_inc_ratio', 'dti', 'revol_bal', 'revol_util']
    outcome = 'outcome'

    newloan = loan_data.loc[0:0, predictors]
    X = loan_data.loc[1:, predictors]
    y = loan_data.loc[1:, outcome]

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X, y)
    
    nbrs = knn.kneighbors(newloan)
    print(X.iloc[nbrs[1][0], :])
    print(f"distance : {nbrs[0]}")
    print(f"predict {knn.predict(newloan)}")

    # Normalization of Data
    scaler = StandardScaler()
    scaler.fit(X * 1.0)

    X_std = scaler.transform(X * 1.0)
    newlan_std = scaler.transform(newloan * 1.0)

    knn.fit(X_std, y)

    nbrs = knn.kneighbors(newloan)
    print(X.iloc[nbrs[1][0], :])
    print(f"distance : {nbrs[0]}")
    print(f"predict {knn.predict(newloan)}")

if __name__ == "__main__":
    main()
