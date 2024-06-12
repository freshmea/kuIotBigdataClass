import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import (
    AdaBoostClassifier,
    BaggingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import (
    GridSearchCV,
    KFold,
    cross_val_score,
    train_test_split,
)
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
    # randomForest
    eclf = RandomForestClassifier(n_estimators=500)
    eclf.fit(X_train, y_train)
    
    print(cross_val_score(eclf, X_train, y_train, cv=5).mean())
    
    #Adaboost
    eclf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=2), n_estimators=500)
    eclf.fit(X_train, y_train)
    
    print(cross_val_score(eclf, X_train, y_train, cv=5).mean())
    
    # hyperparameter tuning
    eclf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=2), n_estimators=500)
    params = {
        "base_estimator__criterion": ["gini", "entropy"],
        "base_estimator__max_features": [7, 8],
        "base_estimator__max_depth": [1, 2],
        "n_estimators": [23, 24, 25, 26, 27],
        "learning_rate": [0.4, 0.45, 0.5, 0.55, 0.6],
    }

    grid = GridSearchCV(estimator=eclf, param_grid=params, cv=5)
    grid.fit(X_train, y_train)
    print(grid.best_params_)
    print(grid.best_score_)


if __name__ == "__main__":
    main()
