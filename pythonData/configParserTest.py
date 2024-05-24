import argparse
import configparser


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/"
    config = configparser.ConfigParser()
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--a_value", dest="a", help="A integers", type=int, default= 10)
    parser.add_argument("-b", "--b_value", dest="b", help="B integers", type=int)
    args = parser.parse_args()
    
    # configparser
    print(config.sections())
    config.read(folder + "example.cfg")
    print(config.sections())
    for key in config["SectionOne"]:
        print(key)
    print(config["SectionOne"]["status"])
    
    # argparse
    print(args)
    print(args.a)
    print(args.b)

if __name__== "__main__":
    main()
