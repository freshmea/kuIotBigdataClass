import matplotlib.pyplot as plt
import numpy as np


def main():
    fig, ax = plt.subplots(2, 2)
    X1 = np.linspace(-10, 10, 1000)
    Y1 = np.sin(X1)
    Y2 = np.cos(X1)
    Y3 = np.tan(X1)
    Y4 = np.exp(X1)
    ax[0, 0].plot(X1, Y1)
    ax[0, 1].plot(X1, Y2)
    ax[1, 0].plot(X1, Y3)
    ax[1, 1].plot(X1, Y4)
    plt.show()


if __name__ == "__main__":
    main()
