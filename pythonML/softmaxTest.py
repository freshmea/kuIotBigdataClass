import numpy as np


def softmaxTest(values):
    array_values = np.exp(values)
    return array_values / np.sum(array_values)


def main():
    values = [2, 1, 5, 0.5]
    y = softmaxTest(values)
    print(f"y : {y}")
    print(f"sum y : {np.sum(y)}")

if __name__ == "__main__":
    main()
