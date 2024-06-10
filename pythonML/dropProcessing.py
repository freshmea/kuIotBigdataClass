import numpy as np
import pandas as pd


def main():
    raw_data = {
        'first_name' : ['Jason', np.nan, 'Tina', "Jake", "Amy"],
        'last_name' : ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
        'age' : [42, np.nan, 36, 24, 73],
        'sex' : ['m', np.nan, 'f', 'm', 'f'],
        'preTestScore' : [4, np.nan, np.nan, 2, 3],
        'postTestScore' : [25, np.nan, np.nan, 62, 70]
    }

    # df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])
    df = pd.DataFrame(raw_data)
    print(df)
    print(df.isnull().sum()/len(df))
    print(df.info())

    # drop
    df_nan_drop = df.dropna()
    print(df.dropna())
    print(df)
    print(df_nan_drop)

    # drop all
    df_nan_drop_all = df.dropna(how='all')
    print('drop all')
    print(df_nan_drop_all)
    df_nan_drop_row = df_nan_drop_all.dropna(axis=1)
    print(df_nan_drop_row)

    # drop threshold
    print('drop threshold')
    print(df.dropna(thresh=3))
    print(df.dropna(axis=0, thresh=5))

    # drop inplace
    print(df.dropna(inplace=True))


if __name__ == '__main__':
    main()
