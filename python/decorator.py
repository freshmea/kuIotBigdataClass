import time


def my_decorator(func):
    def wrapper():
        print("함수 시작전 실행할 코드")
        t = time.time()
        func()
        print("함수 실행 시간:", time.time() - t)
        print("함수 실행 후 코드")
    return wrapper

@my_decorator
def print_hello():
    i = 0
    for _ in range(10000000):
        i += 1
    print("Hello"+ str(i))

def main():
    print_hello()

if __name__ == "__main__":
    main()
