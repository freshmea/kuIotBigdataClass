import numpy as np


def main():
    print(np.arange(1,11,2).sum())
    print(np.arange(1,13).reshape(3,4).shape)
    print(np.arange(1,13).reshape(3,4).sum())
    print(np.arange(1,13).reshape(3,4).sum(axis=0).shape)
    print(np.arange(1,13).reshape(3,4).sum(axis=1).shape)
    
    test_array = np.arange(1,13).reshape(3,4)
    third_order_tensor = np.array([test_array, test_array])
    print(third_order_tensor.shape)
    print(third_order_tensor.sum())
    print(third_order_tensor.sum(axis=0).shape)
    print(third_order_tensor.sum(axis=1).shape)
    print(third_order_tensor.sum(axis=2).shape)
    
if __name__ == "__main__":
    main()