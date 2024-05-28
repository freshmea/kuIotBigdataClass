import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles
from matplotlib.patches import Shadow


def main():
    fig, ax = plt.subplots(2, 2)
    X1 = np.linspace(-10, 10, 1000)
    Y1 = np.sin(X1)
    Y2 = np.cos(X1)
    Y3 = np.tan(X1)
    Y4 = np.exp(X1)
    ax[0, 0].plot(X1, Y1, color='red', linestyle='dashed')
    ax[0, 1].plot(X1, Y2, c="c", linestyle='dotted')
    ax[1, 0].plot(X1, Y3, color='#FF00FF', linestyle=(0, (1, 1)))
    ax[1, 1].plot(X1, Y4, color=(0.1, 0.2, 0.5), linestyle=(0, (3, 10, 1, 10, 1, 10)))
    ax[0, 0].set_title("Sine")
    ax[0, 1].set_title("Cosine")
    ax[1, 0].set_title("Tangent")
    ax[1, 1].set_title("Exponential")
    # fig.legend(ax, labels=['Sine', 'Cosine', 'Tangent', 'Exponential'], loc='upper right', shadow=True, fancybox=False, edgecolor='black', fontsize='small', title='Legend')
    fig.legend(ax, labels=['Sine', 'Cosine', 'Tangent', 'Exponential'], shadow=True, loc='upper right', fancybox=False, edgecolor='black', fontsize='small', title='Legend')

    plt.show()


if __name__ == "__main__":
    main()
