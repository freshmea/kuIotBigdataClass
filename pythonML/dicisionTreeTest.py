import numpy as np
import pandas as pd


def get_info(df):
    suvived = df.loc[df["Survived"] == 1]
    not_suvived = df.loc[df["Survived"] == 0]
    x = np.array([len(suvived)/len(df), len(not_suvived)/len(df)])
    y = np.log2(x[x != 0])
    info_all = -sum(x[x!=0] * y)
    return info_all

def get_attribute_info(df, attribute_name):
    attribute_values = df[attribute_name].unique()
    get_infos = []
    for value in attribute_values:
        split_df = df.loc[df[attribute_name] == value]
        get_infos.append(len(split_df)/len(df) * get_info(split_df))
    return sum(get_infos)

def main():
    folder = "/home/aa/kuIotBigdataClass/pytorch/data/titanic/"
    df = pd.read_csv(folder + "train.csv")
    print(df["Sex"].head())

    print(get_info(df))
    male = df.loc[df["Sex"] == "male"]
    female = df.loc[df["Sex"] == "female"]
    print(f"male info : {get_info(male)}")
    print(f"female info : {get_info(female)}")

    print(get_attribute_info(df, "Sex"))
    print(get_info(df) - get_attribute_info(df, "Sex"))
    print(get_info(df) - get_attribute_info(df, "Pclass"))

if __name__ == "__main__":
    main()
