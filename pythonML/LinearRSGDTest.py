import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


class LinearRegressionGD(object):
    def __init__(self, fit_intercept=True, copy_X=True,
                 eta0=0.001, epochs=1000, weight_decay=0.999, shuffle=True, batch_size=1):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X
        self._eta0 = eta0
        self._epochs = epochs
        self._weight_decay = weight_decay
        self._is_SGD = shuffle
        self.batch_size = batch_size

        self._cost_history = []
        self._w_history = []

        self._coef = None
        self._intercept = None
        self._new_X = None
        self._theta_hat = None


    def cost(self, h, y):
        return (1 / (2 * len(y))) * np.sum((h-y)**2)

    def hypothesis_function(self, X, theta):
        return X.dot(theta)

    def gradient(self, X, y, theta):
        return ((1 / len(y)) * (self.hypothesis_function(X, theta)-y.transpose()).dot(X))

    def fit(self, X, y):
        self._new_X = X
        if self.fit_intercept == True:
            array_ones = np.ones((len(X),1))
            self._new_X = np.concatenate([array_ones, X], axis = 1)

        theta = np.ones(self._new_X.shape[1])

        for epoch in range(self._epochs):
            X_copy = np.copy(self._new_X)
            
            if self._is_SGD:
                np.random.shuffle(X_copy)

            batch = len(X_copy)//self.batch_size

            for batch_count in range(batch):
                X_batch = np.copy(X_copy[batch_count*self.batch_size:(batch_count+1)*self.batch_size])
                y_batch = np.copy(y[batch_count*self.batch_size:(batch_count+1)*self.batch_size])
                gradient = self.gradient(X_batch, y_batch, theta).flatten()
                theta = theta - self._eta0 * gradient

            if epoch % 100 == 0:
                self._w_history.append(theta)
                cost = self.cost(
                    self.hypothesis_function(X_copy, theta), y)
                print(f"Epoch:{epoch} Cost:{cost}")
                self._cost_history.append(cost)
            self._eta0 = self._eta0 * self._weight_decay

        self._theta_hat = theta
        self._coef = self._theta_hat[1:]
        self._intercept = self._theta_hat[0]
        return self

    def predict(self, X):
        if self.fit_intercept == True:
            array_ones = np.ones((len(X),1))
            X = np.concatenate([array_ones, X], axis = 1)
        return X.dot(self._theta_hat) # type: ignore

    @property
    def coef(self):
        return self._coef

    @property
    def intercept(self):
        return self._intercept

    @property
    def weights_history(self):
        return np.array(self._w_history)

    @property
    def cost_history(self):
        return self._cost_history

def main():

    folder = "/home/aa/kuIotBigdataClass/pythonML/"
    df = pd.read_csv(folder + "boston.csv")
    print(df.info())
    print(df.keys())
    data = df.drop(columns=["MEDV"])
    target = df["MEDV"]
    x_data = data.to_numpy()
    y_data = target.to_numpy().reshape(-1, 1)

    minmax_scale = MinMaxScaler(feature_range=(0, 5)).fit(x_data)
    x_scaled_data = minmax_scale.transform(x_data)
    X = x_scaled_data
    y = y_data
    
    gd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, shuffle=False)
    bgd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, shuffle=False, batch_size=X.shape[0])
    sgd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, shuffle=True )
    msgd_lr = LinearRegressionGD(eta0=0.001, epochs=1000, batch_size=100, shuffle=True)
    print("Fitting the models ...")
    print("Gradient Descent")
    gd_lr.fit(X, y)
    print("Batch Gradient Descent")
    bgd_lr.fit(X, y)
    print("Stochastic Gradient Descent")
    sgd_lr.fit(X, y)
    print("Mini-Batch Stochastic Gradient Descent")
    msgd_lr.fit(X, y)

    import matplotlib.pyplot as plt
    plt.plot(range(len(gd_lr.cost_history)), gd_lr.cost_history, label="GD", c="r")
    plt.plot(range(len(bgd_lr.cost_history)), bgd_lr.cost_history, label="BGD", c="g")
    plt.plot(range(len(sgd_lr.cost_history)), sgd_lr.cost_history, label="SGD", c="b")
    plt.plot(range(len(msgd_lr.cost_history)), msgd_lr.cost_history, label="MSGD", c="y")

    plt.show()
    # print(f"w history gd:{gd_lr.weights_history}")
    # print(f"w history bgd:{bgd_lr.weights_history}")
    # print(f"w history sgd:{sgd_lr.weights_history}")
    # print(f"w history msgd:{msgd_lr.weights_history}")
if __name__ == "__main__":
    main()
