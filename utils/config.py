"""
@Time: 2020/9/22 10:42
@Author: Zhirui(Alex) Yang
@E-mail: 1076830028@qq.com
@Program: 
"""
import os

LOG_LEVEL = 'DEBUG'

__proj_dir = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(__proj_dir, 'data')


if __name__ == '__main__':
    print(DATA_DIR)
