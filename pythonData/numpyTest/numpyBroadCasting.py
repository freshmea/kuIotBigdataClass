import numpy as np


def main():
    x = np.arange(1, 10).reshape(3,3)
    print(x)
    print(x + 10)
    print(x // 3)
    
    x = np.arange(1, 13).reshape(4,3)
    v = np.arange(10, 40, 10)
    print(x)
    print(v)
    print(x + v)
    
    x= np.arange(1, 6)
    y = np.arange(10, 50, 10).reshape(-1, 1)
    print(x)
    print(y)
    print(x+y)

if __name__ == "__main__":
    main()