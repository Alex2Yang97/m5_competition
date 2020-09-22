"""
@Time: 2020/9/22 10:41
@Author: Zhirui(Alex) Yang
@E-mail: 1076830028@qq.com
@Program: 
"""
import os
import logging
from datetime import datetime
from utils.config import LOG_LEVEL, DATA_DIR

logger = logging.getLogger("TAROT LOG")
level = logging.getLevelName(LOG_LEVEL)
logger.setLevel(level)
fmt = "TAROT LOG: %(asctime)s [%(levelname)s] %(message)s"
date_fmt = "%Y-%m-%d %H:%M:%S"
logger_path = os.path.join(DATA_DIR, 'log')

# create dir if needed
if not os.path.exists(logger_path):
    os.mkdir(logger_path)
# create logger file with timestamp
cur_datetime = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
logger_file = os.path.join(logger_path, f"{cur_datetime}.log")

logging.basicConfig(format=fmt, datefmt=date_fmt,
                    filename=logger_file)


if __name__ == '__main__':
    logger.info("Log configured successfully!")