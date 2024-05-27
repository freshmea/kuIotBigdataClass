import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels import robust


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_data = pd.read_csv(folder + "sp500_data.csv")
    sp500_px = pd.read_csv(folder + "sp500_sectors.csv")
    


if __name__ == "__main__":
    main()
