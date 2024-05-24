import datetime
import os
import random


def main():
    if not os.path.isdir("log"):
        os.mkdir("log")
    # 현재 워킹디렉토리 확인
    print(os.getcwd())
    # 워킹 디렉토리 변경
    os.chdir("log")
    print(os.getcwd())

    if not os.path.exists("count_log.txt"):
        with open("count_log.txt", "w", encoding="utf8") as f:
            f.write("기록이 시작됩니다.\n")

    with open("count_log.txt", "a", encoding="utf8") as f:
        for i in range(1, 11):
            stamp = str(datetime.datetime.now())
            value = random.random() * 1000000
            log_line = stamp + "\t" + str(value) + "값이 생성되었습니다.\n"
            f.write(log_line)

if __name__ == "__main__":
    main()
