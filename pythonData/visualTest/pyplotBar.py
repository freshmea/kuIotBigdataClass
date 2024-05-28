import matplotlib.pyplot as plt
import numpy as np


def main():
    data= [[5., 25., 50., 20.],
           [4., 23., 51., 17.],
           [6., 22., 52., 19.],
           [5., 26., 53., 23.],]

    # # 바 그래프
    # X = np.arange(0,8,2)
    # plt.bar(X + 0.00, data[0], color = 'b', width = 0.50)
    # plt.bar(X + 0.50, data[1], color = 'g', width = 0.50)
    # plt.bar(X + 1.0, data[2], color = 'r', width = 0.50)
    # plt.xticks(X+0.50, ("A","B","C","D"))

    # 누적바 그래프
    data2 = np.array(data)
    color_list = np.random.choice(['b', 'g', 'r', 'y', 'm', 'c', 'k'], data2.shape[0], replace = False)
    data_label = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:data2.shape[0]]
    X = np.arange(data2.shape[1])

    for i in range(data2.shape[0]):
        plt.bar(X, data2[i], bottom = np.sum(data2[:i], axis = 0), color = color_list[i], label = data_label[i])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
