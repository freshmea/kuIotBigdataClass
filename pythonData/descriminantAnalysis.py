import numpy as np
import pandas as pd
import statsmodels as sm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    loan3000 : pd.DataFrame = pd.read_csv(folder + "loan3000.csv")
    
    # convert to categorical
    loan3000['outcome'] = loan3000['outcome'].astype('category')
    
    predictors = ['borrower_score', 'payment_inc_ratio']
    outcome = 'outcome'
    
    X = loan3000[predictors]
    y = loan3000[outcome]
    loan_lda = LinearDiscriminantAnalysis()
    loan_lda.fit(X, y) # 핵심 훈련 코드
    result = pd.DataFrame(loan_lda.scalings_, index=X.columns) # type: ignore
    print(result)
    print(f"Intercept: {loan_lda.intercept_}")
    for name, coef in zip(predictors, loan_lda.coef_[0]):
        print(f"\t{name}: {coef:.3f}")
    pred = pd.DataFrame(loan_lda.predict_proba(loan3000[predictors]), columns=loan_lda.classes_) # type: ignore
    print(pred.head())

if __name__ == "__main__":
    main()
