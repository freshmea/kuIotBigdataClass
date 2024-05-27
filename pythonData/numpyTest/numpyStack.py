import numpy as np


def main():
    v1 = np.array([1,2,5], dtype=np.uint8)
    v2 = np.array([2,3,4], dtype=np.uint8)
    v3 = np.vstack((v1,v2))
    v4 = np.hstack((v1,v2))
    print(v3)
    print(v4)
    v5 = np.concatenate((v1.reshape(1,3),v2.reshape(1,3)), axis=0)
    print(v5)
    print(v5.shape)
    v6 = np.concatenate((v1.reshape(1,3),v2.reshape(1,3)), axis=0).reshape(-1)
    print(v6)
    
if __name__ == "__main__":
    main()