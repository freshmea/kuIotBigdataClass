import numpy as np


def main():
    # reshape() 메소드는 배열의 모양을 변경한다.
    li1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
    test_array = np.array(li1, dtype=np.uint8)
    print(test_array.shape)
    print(test_array)
    test_array2 = test_array.reshape((-1,))
    print(test_array2.shape)
    print(test_array2)
    li2 = [i for i in range(1000)]
    tensor_array = np.array(li2, dtype=np.int64)
    tensor_array = tensor_array.reshape((10,2,5,10))
    print(tensor_array)

    # flatten reshape(-1)과 같은 효과를 가진다.
    print(tensor_array.flatten())

if __name__ == "__main__":
    main()