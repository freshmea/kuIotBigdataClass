import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonML/"
    df = pd.read_csv(folder + "boston.csv")
    print(df.info())
    print(df.keys())
    data = df.drop(columns=["MEDV"])
    target = df["MEDV"]
    x_data = data.to_numpy()
    y_data = target.to_numpy().reshape(-1, 1)
    print(y_data.shape)

if __name__ == '__main__':
    main()

