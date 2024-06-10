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
    df = pd.DataFrame(raw_data)
    # print(df.fillna('aadf'))
    df['preTestScore'].fillna(df['preTestScore'].mean(), inplace=True)
    print(df.groupby('sex')["postTestScore"].transform('mean'))
    df.iloc[1, 3] = 'm'
    df["postTestScore"].fillna(df.groupby('sex')["postTestScore"].transform('mean'), inplace=True)
    print(df)


if __name__ == '__main__':
    main()
