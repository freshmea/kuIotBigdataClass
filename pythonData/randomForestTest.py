import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    loan3000 = pd.read_csv(folder + "loan3000.csv")
    print(loan3000.head())
    print(loan3000.info())
    
    predictors = ['borrower_score', 'payment_inc_ratio']
    outcome = 'outcome'
    # 정규화
    loan3000[predictors] = StandardScaler().fit_transform(loan3000[predictors])
    # X, y 만들고 train, test로 나누기
    X_train, X_test, y_train, y_test = train_test_split(loan3000[predictors], loan3000[outcome], test_size=0.2, random_state=0)

    # X = loan3000[predictors]
    # y = loan3000[outcome]

    # rf = RandomForestClassifier(n_estimators=100, random_state=1, oob_score=True)
    # rf.fit(X, y)
    # print(f"rf oob dicisino function : {rf.oob_decision_function_}")
    # print(len(rf.oob_decision_function_))

    # # hyperparameter tuning
    # n_estimator = list(range(20, 510, 5))
    # oobScores = []
    # for n in n_estimator:
    #     rf = RandomForestClassifier(n_estimators=n, criterion='entropy', oob_score=True)
    #     rf.fit(X_train, y_train)
    #     oobScores.append(rf.oob_score_)
    # print(oobScores)
    # fig = plt.figure()
    # ax = fig.add_subplot()
    # ax.plot(n_estimator, oobScores)
    # plt.show()
    
    rf = RandomForestClassifier(n_estimators=100, criterion='entropy', oob_score=True)
    
    # accuracy score
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    
if __name__ == "__main__":
    main()
