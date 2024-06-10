import pandas as pd
from sklearn.preprocessing import StandardScaler


def main():
    raw_data ={
        'A' : [14.00, 90.20, 90.95, 96.27, 91.21],
        'B' : [103.02, 107.26, 110.35, 114.23, 114.68],
        'C' : ['big', 'small', 'big', 'small', 'small']
    }
    df = pd.DataFrame(raw_data)
    print(df['A'] - df['A'].min())
    print((df['A'] - df['A'].min()) / (df['A'].max() - df['A'].min()))
    print((df['B']-df['B'].mean()) / df['B'].std())

    # std Scaler
    print('-----------')
    scale = StandardScaler()
    df_scale = scale.fit(df[['B']])
    print(df_scale.fit_transform(df[['B']]))

if __name__ == '__main__':
    main()
