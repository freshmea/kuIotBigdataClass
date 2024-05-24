def main():
    line_counter = 0
    data_header = []
    customer_list = []
    filename= "/home/aa/kuIotBigdataClass/pythonData/customers.csv"
    with open(filename, "r") as f:
        while data := f.readline():
            if line_counter == 0:
                data_header = data.split(",")
            else:
                customer_list.append(data.split(","))
            line_counter += 1
    print(f"Hearder : {data_header}")
    for customer in customer_list:
        print(customer)
    print(f"총 데이터의 수 : {line_counter}")

if __name__ == "__main__":
    main()
