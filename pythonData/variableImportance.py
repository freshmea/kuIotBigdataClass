from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    loan_data = pd.read_csv(folder + "loan_data.csv.gz")
    print(loan_data.head())
    print(loan_data.info())
    
    predictors = ["loan_amnt", "term", "annual_inc", "dti", "payment_inc_ratio", "revol_bal", "revol_util", "purpose", "delinq_2yrs_zero", "pub_rec_zero", "open_acc", "grade", "emp_length", "purpose_", "home_", "emp_len_", "borrower_score"]
    outcome = 'outcome'
    
    X = pd.get_dummies(loan_data[predictors], drop_first=True, dtype=int)
    y = loan_data[outcome]
    
    rf_all = RandomForestClassifier(n_estimators=500, random_state=1)
    rf_all.fit(X, y)

    
    rf_all_entropy = RandomForestClassifier(n_estimators=500, criterion='entropy')
    rf_all_entropy.fit(X, y)

    
    scores = defaultdict(list)
    
    # 교차 검증
    for _ in range(3):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
        rf_all.fit(X_train, y_train)
        acc = accuracy_score(y_test, rf_all.predict(X_test))
        for column in X.columns:
            X_t = X_test.copy()
            X_t[column] = np.random.permutation(X_t[column].values)
            shuff_acc = accuracy_score(y_test, rf_all.predict(X_t))
            scores[column].append((acc-shuff_acc)/acc)
    # # 정규화
    # loan3000[predictors] = StandardScaler().fit_transform(loan3000[predictors])
    # # X, y 만들고 train, test로 나누기
    # X_train, X_test, y_train, y_test = train_test_split(loan3000[predictors], loan3000[outcome], test_size=0.2, random_state=0)

if __name__ == "__main__":
    main()
