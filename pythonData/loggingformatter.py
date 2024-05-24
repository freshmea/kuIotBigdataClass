import logging


def main():
    folder = "/home/aa/kuIotBigdataClass/pythonData/"
    logger = logging.getLogger("myapp")
    hdlr = logging.FileHandler(folder + "myapp.log")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

    logger.error("에러가 발생했습니다.")
    logger.info("시작입니다.")
    logger.info("테스트가 끝났습니다.")

if __name__ == "__main__":
    main()
