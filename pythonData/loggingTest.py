import logging

logging.debug('This is a debug message')
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

logger = logging.getLogger("main")
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

logger.setLevel(logging.WARNING)
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
# 로그 정보 파일로 내보내기
file_handler = logging.FileHandler("my.log")
logger.addHandler(file_handler)
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


