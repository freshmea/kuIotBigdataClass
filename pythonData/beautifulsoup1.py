from bs4 import BeautifulSoup


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/"
    with open(folder + "books.xml", "r", encoding="utf8") as f:
        xml = f.read()
        soup = BeautifulSoup(xml, "lxml")
    
    for book_info in soup.find_all("author"):
        print(book_info)
        print(book_info.get_text())


if __name__ == "__main__":
    main()
