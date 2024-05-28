import pandas as pd
from matplotlib import axis


def main():
    raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'test_score': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
    }
    df_left = pd.DataFrame(raw_data, columns=['subject_id', 'test_score'])
    raw_data2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
    }
    df_right = pd.DataFrame(raw_data2, columns=['subject_id', 'first_name', 'last_name'])
    print(pd.merge(left=df_left, right=df_right, how='inner', on='subject_id'))
    print(pd.merge(left=df_left, right=df_right, how='outer', on='subject_id'))
    print(pd.merge(left=df_left, right=df_right, how='left', on='subject_id'))
    print(pd.merge(left=df_left, right=df_right, how='right', on='subject_id'))

if __name__ == "__main__":
    main()
