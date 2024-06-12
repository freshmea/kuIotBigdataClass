import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def main():
    folder = "/home/aa/kuIotBigdataClass/pytorch/data/titanic/"
    data = pd.read_csv(folder + "train.csv")
    data_df = pd.DataFrame(data)
    data_df.drop(columns=["Name", "Ticket", "Cabin"], inplace=True)

    fare_mean = data_df[["Pclass", "Fare"]].groupby("Pclass").mean().reset_index()
    fare_mean.columns = ["Pclass", "Fare_mean"]
    all_df = pd.merge(data_df, fare_mean, how="left", on="Pclass")
    all_df.loc[all_df["Fare"].isnull(), "Fare"] = all_df["Fare_mean"]
    all_df.loc[all_df["Age"].isnull(), "Age"] = all_df["Age"].mean()

    predictors = ["Pclass", "Age", "Fare", "Embarked"]
    outcome = "Survived"

    X = all_df[predictors]
    y = all_df[outcome]
    X_oneHot = pd.get_dummies(X, columns=["Embarked"], drop_first=True)
    X_oneHot = pd.DataFrame(StandardScaler().fit_transform(X_oneHot))
    X_train = X_oneHot.iloc[:891, :]
    y_train = y.iloc[:891]
    # print(X_train.to_numpy())    

    clf1 = LogisticRegression()
    clf2 = DecisionTreeClassifier(random_state=1, max_depth=4)
    clf3 = GaussianNB()
    eclf = VotingClassifier(estimators=[('lr', clf1), ('dt', clf2), ('gnb', clf3)], voting='hard')
    
    # train
    eclf.fit(X_train, y_train)
    
    # cross_val_score
    import sklearn.model_selection as ms
    print(ms.cross_val_score(eclf, X_train, y_train, cv=5).mean())
    print(ms.cross_val_score(clf1, X_train, y_train, cv=5).mean())
    print(ms.cross_val_score(clf2, X_train, y_train, cv=5).mean())
    print(ms.cross_val_score(clf3, X_train, y_train, cv=5).mean())
    
    
if __name__ == "__main__":
    main()
