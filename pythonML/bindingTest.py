import pandas as pd


def main():
    raw_data ={
        'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]
    }
    df = pd.DataFrame(raw_data)
    print(df)

    bins = [ i for i in range(0, 101, 25)]
    group_names = ['Low', 'Okay', 'Good', 'Great']
    cat = pd.cut(df['postTestScore'], bins, labels=group_names)
    print(cat)

if __name__ == '__main__':
    main()
