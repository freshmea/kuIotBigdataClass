import pickle

from pickleTest import Multiply


def main():
    with open("list.pickle", "rb") as f:
        test : Multiply = pickle.load(f)
        test2 : Multiply = pickle.load(f)
    print(test)
    print(type(test))
    print(test.multiply(20))
    print(test2.multiply(20))

if __name__ == "__main__":
    main()
