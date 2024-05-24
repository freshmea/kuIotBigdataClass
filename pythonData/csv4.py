import csv


def main():
    seoung_nam_data = []
    header = []
    rownum = 0
    filename = "/home/aa/kuIotBigdataClass/pythonData/korea_floating_population_data.csv"
    with open(filename, "r", encoding="cp949") as f:
        csv_data= csv.reader(f)
if __name__ == "__main__":
    main()
