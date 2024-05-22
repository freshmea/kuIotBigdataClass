def min():
    decimal = 33
    # result = ''
    # while (decimal > 0):
    #     remainder = decimal % 2
    #     decimal = decimal // 2
    #     result = str(remainder) + result
    result = bin(decimal)
    binary = 0b100001
    hexa = 0xff
    print(result)
    print(binary)
    print(hexa)

if __name__ == "__main__":
    min()
