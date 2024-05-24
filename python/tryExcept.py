class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

def main():
    for i in range(10):
        try:
            print(10/i)
            # raise MyError("내가 일으킨 에러다.")
        except ZeroDivisionError as e:
            print(e)
            print("0으로 나누지 마세요!")
        except MyError as e:
            print(e)
        else:
            print("에러가 발생하지 않았습니다.")
        finally:
            print("무조건 실행")

if __name__ == "__main__":
    main()
