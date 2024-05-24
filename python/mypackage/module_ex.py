# import fah_converter
import random
import time
import urllib.request

from fah_converter import convert_c_to_f as con


def main():
    celsius = float(input("썹씨 온도를 넣으시오! : "))
    fah = con(celsius)
    print(f"섭씨 온도는 {celsius} 입니다.")
    print(f"화씨 온도는 {fah} 입니다.")
    print(random.randint(1, 100))
    print(random.random())
    print(urllib.request.urlopen("http://www.google.com").read())

if __name__ == "__main__":
    main()
