import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    loan_data : pd.DataFrame = pd.read_csv(folder + "loan_data.csv.gz")
    loan_data = loan_data.drop(columns=['Unnamed: 0', 'status'])
    loan_data['outcome'] = pd.Categorical(loan_data['outcome'], categories=['paid off', 'default'], ordered=True)
    
    print(loan_data.head())
    print(loan_data.info())

    predictors = ['dti', 'revol_bal', 'revol_util', 'open_acc', 'delinq_2yrs_zero', 'pub_rec_zero']
    outcome = 'outcome'
    
    X = loan_data[predictors]
    y = loan_data[outcome]
    
    knn = KNeighborsClassifier(n_neighbors=20)
    knn.fit(X, y)

    loan_data['borrower_score'] = knn.predict_proba(X)
    print(loan_data['borrower_score'].describe())


if __name__ == "__main__":
    main()
