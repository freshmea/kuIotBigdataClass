import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold, train_test_split
from sklearn.preprocessing import StandardScaler


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

    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    
if __name__ == "__main__":
    main()
