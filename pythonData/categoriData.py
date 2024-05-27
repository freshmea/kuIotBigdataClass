import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels import robust


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    dfw = pd.read_csv(folder + "dfw_airline.csv")
    ax = dfw.transpose().plot.bar(figsize=(4,4), legend=False)
    ax.set_xlabel('Cause of delay')
    ax.set_ylabel('Count')
    plt.show()
    
    


if __name__ == "__main__":
    main()
