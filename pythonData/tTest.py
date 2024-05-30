import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    session_times : pd.DataFrame = pd.read_csv(folder + "web_page_data.csv")
    session_times["Time"] = session_times["Time"] * 100
    print(session_times.head())
    print(session_times.info())
    print(mean_a := session_times[session_times.Page == "Page A"].Time.mean())
    print(mean_b := session_times[session_times.Page == "Page B"].Time.mean())
    print(mean_b - mean_a)
    
    res = stats.ttest_ind(session_times[session_times.Page == "Page A"].Time,
                          session_times[session_times.Page == "Page B"].Time,
                          equal_var=False)
    print(f"p-value single sided test: {res.pvalue/ 2:.3f}") #type: ignore

if __name__ == "__main__":
    main()
