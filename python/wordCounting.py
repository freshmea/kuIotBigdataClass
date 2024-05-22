def main():
    folder = "/home/aa/kuIotBigdataClass/python/"
    with open(folder + "yesterday.txt", "r") as f:
        yesterday_lyric = f.read()
    n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")
    print(f"'Yesterday'의 단어수: {n_of_yesterday}")

if __name__ == "__main__":
    main()
