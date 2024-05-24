import pickle


class Multiply:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        return number * self.multiplier

def main():
    multiply = Multiply(5)
    multiply2 = Multiply(10)
    print(multiply.multiply(10))
    with open("list.pickle", "wb") as f:
        pickle.dump(multiply, f)
        pickle.dump(multiply2, f)

if __name__ == "__main__":
    main()

