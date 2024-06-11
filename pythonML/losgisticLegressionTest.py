import pandas as pd


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonML/"
    # data_url = "http://www-stat.wharton.upenn.edu/~waterman/DataSets/uva.txt"
    # df = pd.read_table(data_url)
    # df.to_csv(folder + "uva.csv", index=False)
    df = pd.read_csv(folder + "uva.csv")
    print(df.head())
    print(df.info())

if __name__ == '__main__':
    main()
