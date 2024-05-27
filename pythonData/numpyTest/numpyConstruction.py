import numpy as np


def main():
    test_array = np.ones((10,10), dtype=np.int8)
    print(test_array)
    print(test_array.dtype)

    test_array2 = np.zeros((10,10), dtype=np.int8)
    print(test_array2)
    print(test_array2.dtype)

    test_array3 = np.empty((10,10), dtype=np.int8)
    print(test_array3)
    print(test_array3.dtype)

    # ones_like() 메소드는 배열의 모양을 유지하면서 1로 초기화된 배열을 생성한다.
    re_array = np.array(range(60)).reshape(5, 12)
    test_array4 = np.ones_like(re_array, dtype=np.int8)
    print(test_array4)
    print(test_array4.dtype)
    
    # 단위 행렬, eye, diag
    id1 = np.identity(3, dtype=np.int8)
    print(id1)
    eye1 = np.eye(3, 4, k=1, dtype=np.int8)
    print(eye1)
    li1= np.array(range(9)).reshape(3,3)
    diag1 = np.diag(li1)
    print(diag1)
    
    print(np.random.uniform(0, 5, 10).mean())
    print(np.random.normal(0, 2, 10).mean())
    print(np.random.uniform(0, 5, 10).std())
    print(np.random.normal(0, 2, 100000).std())

if __name__ == "__main__":
    main()