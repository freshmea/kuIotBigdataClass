from unittest import result

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    loan_data : pd.DataFrame = pd.read_csv(folder + "loan_data.csv.gz")
    print(loan_data.head())
    print(loan_data.info())

    predictors = ['payment_inc_ratio', 'purpose_', 'home_', 'emp_len_', 'borrower_score']
    outcome = 'outcome'
    X = pd.get_dummies(loan_data[predictors], prefix='', prefix_sep='', drop_first=True)
    y = loan_data[outcome]
    print(X.head())
    print(X.T.head(20))
    print(y.head())

    logit_reg = LogisticRegression(penalty='l2', C=1e42, solver='liblinear')
    logit_reg.fit(X, y)

    pred = logit_reg.predict(X)
    pred_y = pred == 'default'
    true_y = y == 'default'
    true_pos = true_y & pred_y
    true_neg = ~true_y & ~pred_y
    false_pos = ~true_y & pred_y
    false_neg = true_y & ~pred_y
    
    con_mat = pd.DataFrame([[np.sum(true_pos), np.sum(false_neg)],
                            [np.sum(false_pos), np.sum(true_neg)]],
                           index=['Y=default', 'Y=Paid off'],
                           columns=['Yhat = default', 'Yhat = Paid off'])
    print(con_mat)
    print(f"Accuracy(정확도): {(np.sum(true_pos) + np.sum(true_neg)) / len(y)}")
    print(f"Precision(정밀도): {np.sum(true_pos) / (np.sum(true_pos) + np.sum(false_pos))}")
    print(f"Recall(재현율): {np.sum(true_pos) / (np.sum(true_pos) + np.sum(false_neg))}")
    
    


if __name__ == "__main__":
    main()