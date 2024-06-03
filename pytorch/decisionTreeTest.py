import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dmba import plotDecisionTree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


def main():
    folder = "/home/aa/kuIotBigdataClass/pytorch/data/"
    dataset : pd.DataFrame= pd.read_csv(folder + "titanic/train.csv", index_col="PassengerId")
    print(dataset.head())
    print(dataset.info())
    df = dataset[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Survived']]
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    print(df.head())
    print(df.info())
    df.dropna(inplace=True)
    print(df.head())
    print(df.info())
    
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accurate = accuracy_score(y_test, y_pred)
    print(f"Accuracy : {accurate}")
    # fig = plt.figure()
    # ax = fig.add_subplot()
    # plotDecisionTree(model, feature_names=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare'], class_names=['Died', 'Survived'])
    # plt.show()


if __name__ == "__main__":
    main()
