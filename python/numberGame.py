import random
import time


def min():
    random.seed(time.time())
    guess_number = random.randint(1, 100)
    print(guess_number)
    users_input = int(input("숫자를 맞춰보세요: "))
    while users_input is not guess_number:
        print("숫자가 너무 큽니다.") if users_input > guess_number else print("숫자가 너무 작습니다.")
        users_input = int(input("다시 입력해주세요: "))
    print("정답입니다.")

if __name__ == "__main__":
    min()
