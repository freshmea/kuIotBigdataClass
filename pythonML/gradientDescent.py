import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 2

def main():
    x = np.arange(-10, 11 , 1)
    f_x = f(x)
    
    plt.plot(x, f_x)
    plt.show()
    
    x_new = 10
    derivative = []
    y = []
    learning_rate = 2.5
    for i in range(100):
        old_value = x_new
        x_new = old_value - learning_rate * 2 * old_value
        derivative.append(x_new)
        y.append( f(x_new) )
    plt.plot(x, f_x)
    plt.scatter(derivative, y)
    plt.xlim([-10, 10])
    plt.show()

if __name__ == '__main__':
    main()
