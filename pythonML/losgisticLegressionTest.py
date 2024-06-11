import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonML/"
    # data_url = "http://www-stat.wharton.upenn.edu/~waterman/DataSets/uva.txt"
    # df = pd.read_table(data_url)
    # df.to_csv(folder + "uva.csv", index=False)
    df = pd.read_csv(folder + "uva.csv")

    df.pop('who')
    df.pop('Country')
    df.pop('Years on Internet')
    cat = df.select_dtypes(include=['object']).columns

    for col in cat:
        df[col] = df[col].astype('category')

    print(df.info())
    # one Hot
    # df_oneHot = pd.get_dummies(df)

    # label encoding
    le = LabelEncoder()
    for col in cat:
        df[col] = le.fit_transform(df[col])
    df_oneHot = df
    print("After label encoding")
    print(df_oneHot.info())
    # fill missing values
    df_oneHot.loc[pd.isnull(df_oneHot['Age']), 'Age'] = df_oneHot['Age'].mean()
    print(df_oneHot.isnull().sum())
    
    # x_data = df_oneHot.iloc[:, 1:].values
    # y_data = df_oneHot.iloc[:, 0].values.reshape(-1, 1) # type: ignore
    # print(x_data.shape, y_data.shape)

    predictors = df_oneHot.drop(columns=['Newbie']).columns
    target = 'Newbie'
    x_data = df_oneHot[predictors]
    y_data = df_oneHot[target]
    
    minmax_scale = MinMaxScaler().fit(x_data)
    x_data = minmax_scale.transform(x_data)
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.33, random_state=42)
    
    model = LogisticRegression(fit_intercept=True)
    model.fit(X_train, y_train)
    LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True, intercept_scaling=1, l1_ratio=None, max_iter=100, multi_class='warn', n_jobs=None, penalty='l2', random_state=None, solver='warn', tol=0.0001, verbose=0, warm_start=False) # type: ignore
    
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)
    print(f"y_pred : {y_pred}")
    print(f"y_pred proba {y_proba}")
    print(f"confusion matrix : \n{confusion_matrix(y_test, y_pred)}")
    print(f"accuracy score : \n{accuracy_score(y_test, y_pred)}")
    print(f"precision score : \n{precision_score(y_test, y_pred)}")
    print(f"recall score : \n{recall_score(y_test, y_pred)}")
    print(f"f1 score : \n{f1_score(y_test, y_pred)}")
    
    
if __name__ == '__main__':
    main()
