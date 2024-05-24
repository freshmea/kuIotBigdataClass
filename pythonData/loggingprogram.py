import csv
import logging
import logging.config


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/"
    logging.config.fileConfig(folder + 'logging.conf')
    logger = logging.getLogger()
    
    logger.info(f"Open file TEST")

if __name__ == '__main__':
    main()
