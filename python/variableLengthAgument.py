def asterisk_test(a, b, *args):
    print(a)
    print(b)
    for i in args:
        print(i)
    return a + b + sum(args)

def main():
    print(asterisk_test(1, 2, 3, 4, 5))

if __name__ == "__main__":
    main()
