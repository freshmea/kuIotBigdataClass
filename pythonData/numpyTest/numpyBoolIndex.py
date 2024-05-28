import numpy as np


def main():
    x_1 =np.random.randint(1, 100, 10)
    x_2 =np.random.randint(1, 100, 10)
    print(f"x_1 : {x_1}")
    print(f"x_2 : {x_2}")
    print(f"x_1 > x_2 : {x_1 > x_2}")
    # all any
    print(f"(x_1 > x_2).all() : {(x_1 > x_2).all()}")
    print(f"(x_1 > 100).all() : {(x_1 > 100).all()}")
    print(f"(x_1 > x_2).any() : {(x_1 > x_2).any()}")
    print(f"(x_1 > 0) : {(x_1 > 0)}")
    print(f"(x_1 > 0).any() : {(x_1 > 0).any()}")
    # where
    x = np.array([4, 6, 7, 3, 2])
    print(f"x > 5 : {x > 5}")
    print(f"np.where(x > 5) : {np.where(x > 5)}")
    for i in np.where(x > 5):
        print(f"x[i] : {x[i]}")
    # argsort, argmax, argmin
    print(f"np.argsort(x) : {np.argsort(x)}")
    for i in np.argsort(x):
        print(f"x[{i}] : {x[i]}")
    print(f"np.argmax(x) : {np.argmax(x)}, {x[np.argmax(x)]}")
    print(f"np.argmin(x) : {np.argmin(x)}, {x[np.argmin(x)]}")
    

if __name__ == "__main__":
    main()
