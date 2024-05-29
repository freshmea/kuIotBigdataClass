import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    kc_tax = pd.read_csv(folder + "kc_tax.csv.gz")
    
    kc_tax0 = kc_tax.loc[(kc_tax.TaxAssessedValue < 750000) &
                        (kc_tax.SqFtTotLiving > 100) &
                        (kc_tax.SqFtTotLiving < 3500), :]
    print(kc_tax0.shape)
    print(kc_tax0.head())
    print(kc_tax0.info())
    
    # ax = kc_tax0.plot.hexbin(x='SqFtTotLiving', y='TaxAssessedValue', gridsize=30, sharex=False, figsize=(5, 4))
    # ax.set_xlabel('Finished Square Feet')
    # ax.set_ylabel('Tax Assessed Value')
    # plt.tight_layout()
    # plt.show()
    
    # 등고선 그리기
    # fig, ax = plt.subplots(figsize=(4, 4))
    # kc_tax0.replace([np.inf, -np.inf], np.nan, inplace=True)
    # ax = sns.kdeplot(data=kc_tax0, x='SqFtTotLiving', y='TaxAssessedValue', ax=ax)
    # ax.set_xlabel('Finished Square Feet')
    # ax.set_ylabel('Tax Assessed Value')
    # plt.show()


if __name__ == "__main__":
    main()