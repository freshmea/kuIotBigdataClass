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
    print(y.head())

    logit_reg = LogisticRegression(penalty='l2', C=1e42, solver='liblinear')
    logit_reg.fit(X, y)

    # y_numnbers = [1 if yi =='default' else 0 for yi in y]
    # print(X.assign(const=1))
    # logit_reg_sm = sm.GLM(y_numnbers, X.assign(const=1), family=sm.families.Binomial())
    # logit_result = logit_reg_sm.fit()
    
    formula = "outcome ~ bs(payment_inc_ratio, df=4) + purpose_" + \
        " + home_ + emp_len_ + bs(borrower_score, df=4)"
    model = smf.glm(formula = formula, data=loan_data, family=sm.families.Binomial())
    result = model.fit()
    print(result.summary())
    


if __name__ == "__main__":
    main()