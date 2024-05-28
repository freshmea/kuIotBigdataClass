import matplotlib.pyplot as plt
import numpy as np


def main():
    X1 = np.linspace(-5, 5, 1000)
    Y1 = np.sin(X1)
    Y2 = np.cos(X1)
    Y3 = np.tan(X1)
    Y4 = np.exp(X1)
    Y5 = np.tanh(X1)
    fig = plt.figure()
    ax1 = fig.add_subplot(321)
    plt.plot(X1, Y1)
    ax2 = fig.add_subplot(322)
    plt.plot(X1, Y2)
    ax3 = fig.add_subplot(312)
    plt.plot(X1, Y3)
    ax4 = fig.add_subplot(325)
    plt.plot(X1, Y4)
    ax5 = fig.add_subplot(326)
    plt.plot(X1, Y5)
    plt.show()


if __name__ == "__main__":
    main()
