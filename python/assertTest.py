def get_binary_number(decimal_number):
    assert isinstance(decimal_number, int)
    return bin(decimal_number)

def main():
    print(get_binary_number(10))
    print(get_binary_number("10"))

if __name__ == "__main__":
    main()
