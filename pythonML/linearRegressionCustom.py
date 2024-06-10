import random

import matplotlib.pyplot as plt
import numpy as np


def gen_data(numPoints, bias, variance, weight=1):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    for i in range(0, numPoints):
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i* weight + bias) + random.uniform(0, 1) * variance
    return x, y

def gradient_descent(x, y, theta, alpha, m, numIterations):
    xTrans = x.transpose()
    theta_list = []
    cost_list = []
    for i in range(0, numIterations):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        gradient = np.dot(xTrans, loss) / m
        theta = theta - alpha * gradient
        if i % 250 == 0:
            theta_list.append(theta)
        cost_list.append(cost)
    return theta, np.array(theta_list), cost_list

def main():
    x, y = gen_data(100, 25, 10)
    # plt.plot(x[:, 1] , y, 'ro')
    # plt.show()
    m, n = np.shape(x)
    numIterations = 5000
    alpha = 0.0005 # learning rate
    theta = np.ones(n)

    theta, theta_list, cost_list = gradient_descent(x, y, theta, alpha, m, numIterations)

    y_predict_step = np.dot(x, theta_list.transpose())
    # plt.plot(x[:, 1], y, 'ro')
    # for i in range(0, 20, 2):
    #     plt.plot(x[:, 1], y_predict_step[:, i], label="Line %d %i")
    # plt.show()

    # y_pred = np.dot(x, theta)
    # plt.plot(x[:, 1], y, 'ro')
    # plt.plot(x[:, 1], y_pred, lw=3)
    # plt.show()

    iterations = range(len(cost_list))
    plt.scatter(iterations, cost_list)
    plt.show()


if __name__ == '__main__':
    main()
