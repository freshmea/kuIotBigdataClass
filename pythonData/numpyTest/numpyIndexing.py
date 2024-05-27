import numpy as np


def main():
    li1 = [[1,2,3],[4,5,6]]
    test_array = np.array(li1, dtype=np.uint8)

    for i in test_array:
        print(i)
    
if __name__ == "__main__":
    main()