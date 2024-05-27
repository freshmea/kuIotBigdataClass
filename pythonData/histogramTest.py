import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels import robust


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    state = pd.read_csv(folder + "state.csv")
    
    binnedPopulation = pd.cut(state["Population"], 10)
    binnedPopulation.value_counts()
    print(binnedPopulation)
    print(binnedPopulation.value_counts())
    
    # plt.hist(state["Population"], bins=10)
    # plt.show()
    # state["Population"].plot.hist(bins=10)
    # ax1 = state["Population"].plot.hist(bins=10)
    # plt.show()
    
    ax = state["Murder.Rate"].plot.hist(density=True, xlim=[0, 12], bins=range(1,12)) #type: ignore
    state["Murder.Rate"].plot.density(ax = ax)
    ax.set_xlabel('Murder Rate (per 100,000)')
    plt.show()
    
    
    


if __name__ == "__main__":
    main()
