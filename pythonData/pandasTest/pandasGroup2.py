import pandas as pd
from matplotlib import axis


def main():
    ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
                         'Kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals',
                         'Riders'],
                'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
                'Year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
                'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690]}
    df = pd.DataFrame(ipl_data)
    print(df)
    grouped = df.groupby("Team")
    #aggregation
    print(grouped.get_group("Riders"))
    print(grouped.agg(min))
    print(grouped.agg(max))
    #transformation
    score = lambda x: (x - x.mean()) / x.std()
    print(grouped.transform(max))
    print(grouped.transform(score))
    #filter
    print(grouped.filter(lambda x: len(x) >= 3))
    print(grouped.mean())
    print(grouped.filter(lambda x: x["Points"].mean() > 760))
if __name__ == "__main__":
    main()
