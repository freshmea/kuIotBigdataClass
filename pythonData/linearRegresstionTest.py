import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/data/"
    lung = pd.read_csv(folder + "LungDisease.csv")
    # lung.plot.scatter(x='Exposure', y='PEFR')
    model = LinearRegression()
    predictors= ['Exposure']
    outcone = 'PEFR'
    model.fit(lung[predictors], lung[outcone])
    print(f"intercept: {model.intercept_:.3f}")
    print(f"Coefficient Exposure: {model.coef_[0]:.3f}")
    
    fitted = model.predict(lung[predictors])
    residuals = lung[outcone] - fitted
    print(f"residuals mean: {residuals.mean():.3f}")
    print(f"residuals std: {residuals.std():.3f}")
    print(f"residuals : {residuals}")
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim(0, 23)
    ax.set_ylim(205, 450)
    ax.set_xlabel("Exposure")
    ax.set_ylabel("PEFR")
    ax.plot((0, 23), model.predict(pd.DataFrame({'Exposure': [0, 23]})))
    ax.text(0.4, model.intercept_, r'$b_0$', size='larger') #type: ignore

    x= pd.DataFrame({'Exposure': [7.5, 17.5]})
    y = model.predict(x)
    ax.plot((7.5, 7.5, 17.5), (y[0], y[0], y[1]), '--')
    ax.text(5, np.mean(y), r'$\Delta Y$', size='larger') # type: ignore
    ax.text(12, y[1] - 10, r'$\Delta X$', size='larger') # type: ignore
    ax.text(12, 390, r'$b_1$', size='larger') # type: ignore

    ax.scatter(lung.Exposure, lung.PEFR)
    plt.show()


if __name__ == "__main__":
    main()
