import csv


def main():
    filename = "/home/aa/kuIotBigdataClass/pythonData/customers.csv"
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for c in reader:
            print(c)
    

if __name__ == "__main__":
    main()
