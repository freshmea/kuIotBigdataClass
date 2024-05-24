def main():
    with open("test.txt", "w", encoding="utf8") as f:
        for i in range(1, 11):
            f.write(f"{i} 번째 줄 입니다.")

if __name__ == "__main__":
    main()
