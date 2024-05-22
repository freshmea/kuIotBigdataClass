def f(x):
    y = x
    x = 5
    return y * y

def spam(eggs):
    eggs += 1
    # eggs.append(1)
    # eggs = [2, 3]
    eggs = 10


def main():
    x = 3
    print(f(x))
    print(x)
    ham = 0
    spam(ham)
    print(ham)

if __name__ == "__main__":
    main()
