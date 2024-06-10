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
    
    # # with transform
    # print(df.groupby('sex')["postTestScore"].transform('mean'))
    # df.iloc[1, 3] = 'm'
    # df["postTestScore"].fillna(df.groupby('sex')["postTestScore"].transform('mean'), inplace=True)
    
    # # without transform
    # print(df.groupby('sex')["postTestScore"].mean())
    # sex_group = df.groupby('sex')["postTestScore"].mean()
    # df.iloc[1, 3] = 'm'
    # new_df = df.merge(sex_group, how='left', on='sex')
    # print(new_df.head())
    # new_df["postTestScore_x"].fillna(new_df["postTestScore_y"], inplace=True)
    # new_df.drop(columns="postTestScore_y", inplace=True)
    # new_df.rename(columns={"postTestScore_x": "postTestScore"}, inplace=True)
    # print(new_df)
    
    # without transform2
    for i in range(len(df)):
        if df.iloc[i, 3] == 'm' and pd.isnull(df.iloc[i, 5]):
            df.iloc[i, 5] = df.groupby("sex")["postTestScore"].mean()[0]
        elif df.iloc[i, 3] == 'f' and pd.isnull(df.iloc[i, 5]):
            df.iloc[i, 5] = df.groupby("sex")["postTestScore"].mean()[1]
    print(df)


if __name__ == '__main__':
    main()
