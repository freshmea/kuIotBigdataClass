import pandas as pd


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonML/"
    df = pd.read_csv(folder + "boston.csv")
    print(df.info())

if __name__ == '__main__':
    main()

