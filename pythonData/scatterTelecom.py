import matplotlib.pyplot as plt
import pandas as pd


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    sp500_px = pd.read_csv(folder + "sp500_data.csv", index_col=0)
    sp500_sym = pd.read_csv(folder + "sp500_sectors.csv")

    telecomSymbols = sp500_sym[sp500_sym['sector'] == 'telecommunications_services']['symbol']
    telecom = sp500_px.loc[sp500_px.index > '2012-07-01', telecomSymbols]
    print(telecom.corr())
    print(telecom)
    ax = telecom.plot.scatter(x='T', y='VZ', marker='o', alpha=0.5)
    ax.set_xlabel('AT&T')
    ax.set_ylabel('Verizon (VZ)')
    ax.axhline(0, color='gray', lw=1)
    ax.axvline(0, color='gray', lw=1)
    plt.show()

if __name__ == "__main__":
    main()
