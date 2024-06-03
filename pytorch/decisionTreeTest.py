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
    

    # # X, y 만들고 train, test로 나누기
    # X = dataset.iloc[:, :-1].values
    # y = dataset.iloc[:, 4].values
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    # # 정규화
    # scaler = StandardScaler()
    # X_train = scaler.fit_transform(X_train)
    # X_test = scaler.fit_transform(X_test)

    # # ML model 만들기 및 학습
    # knn = KNeighborsClassifier(n_neighbors=5)
    # knn.fit(X_train, y_train)

    # # 예측, 정확도 출력
    # y_pred = knn.predict(X_test)
    # print(accuracy_score(y_test, y_pred))

    # # knn의 k값에 따른 정확도 출력 검증
    # k = 10
    # acc_array = np.zeros(k)
    # for k in np.arange(1, k+1):
    #     knn = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    #     y_pred = knn.predict(X_test)
    #     acc_array[k-1] = accuracy_score(y_test, y_pred)
    # print(list(acc_array))


if __name__ == "__main__":
    main()
