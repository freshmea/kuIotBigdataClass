import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles
from matplotlib.patches import Shadow


def main():
    N = 5
    X1 = np.random.rand(512, N)
    Y1 = np.random.rand(512, N)
    A1 = np.random.rand(512, N) * 150
    # colors = np.random.rand(512, N, N)
    # colors = np.random.choice(['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'])
    for i in range(N):
        plt.scatter(X1[:,i], Y1[:,i], s=A1[:,i], c=np.random.choice(['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']), alpha=0.5)
    
    plt.show()


if __name__ == "__main__":
    main()
