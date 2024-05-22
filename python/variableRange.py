def calculate(x,y):
    global a, b
    total = x + y
    print("In Function")
    print(f"a:{a}, b:{b}, total:{total}")
    return total

a = 5
b = 7
total = 0
print("In Program - 1")
print(f"a:{a}, b:{b}, total:{total}")

sum = calculate(a,b)
print("After Calculation")
print(f"a:{a}, b:{b}, total:{total}, sum:{sum}")
# def main():
#     pass

# if __name__ == "__main__":
#     main()
