# def func(x, y):
#     return x + y

def main():
    li1 = [1, 2, 3, 4, 5]
    # li2 = map(func, li1)
    li2 = map(lambda x: x * x, li1)
    li3 = filter(lambda x: x % 2 == 0, li1)
    print(*li2)
    print(*li3)
    func_plus = lambda x, y: x + y
    print(func_plus(3, 4))

if __name__ == "__main__":
    main()
