import numpy as np


def main():
    li1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    test_array = np.array(li1, dtype=np.uint8)

    print(test_array[1][1])
    print(test_array[1, 1])
    print(test_array[0:2, 0:2])
    
    x = np.array(range(15), int).reshape(3, -1)
    print(x[:,::2])
    print(x[::2,::3])

if __name__ == "__main__":
    main()