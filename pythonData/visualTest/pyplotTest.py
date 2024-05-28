import matplotlib.pyplot as plt
import numpy as np


def main():
    fig = plt.figure()
    fig.set_size_inches(10, 20)
    ax_1 = fig.add_subplot(1,2,1)
    ax_2 = fig.add_subplot(1,2,2)
    X = np.linspace(0, 100, 100)
    Y = np.linspace(0, 100, 100)
    ax_1.plot(X, Y)
    X_1 = np.linspace(0, 30, 1000)
    Y_1 = np.cos(X_1)
    ax_2.plot(X_1, Y_1)
    plt.show()

if __name__ == "__main__":
    main()
