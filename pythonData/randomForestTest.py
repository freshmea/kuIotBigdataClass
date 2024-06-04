import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    loan3000 = pd.read_csv(folder + "loan3000.csv")
    print(loan3000.head())
    print(loan3000.info())
    
    predictors = ['borrower_score', 'payment_inc_ratio']
    outcome = 'outcome'
    
    X = loan3000[predictors]
    y = loan3000[outcome]
        
    rf = RandomForestClassifier(n_estimators=100, random_state=1, oob_score=True)
    rf.fit(X, y)
    print(f"rf oob dicisino function : {rf.oob_decision_function_}")
    print(len(rf.oob_decision_function_))
    
    n_estimator = list(range(20, 510, 5))
    oobScores = []
    for n in n_estimator:
        rf = RandomForestClassifier(n_estimators=n, criterion='entropy', max_depth=5, random_state=1, oob_score=True)
        rf.fit(X, y)
        oobScores.append(rf.oob_score_)
    print(oobScores)
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(n_estimator, oobScores)
    plt.show()
    
if __name__ == "__main__":
    main()
