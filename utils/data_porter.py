"""
@Time: 2020/9/22 10:40
@Author: Zhirui(Alex) Yang
@E-mail: 1076830028@qq.com
@Program: 
"""
import os
import pandas as pd


def read_from_csv(filename, dir_path='./', **kwargs):
    file_path = os.path.join(dir_path, filename)
    df = pd.read_csv(file_path, **kwargs)
    return df


def save_to_csv(df, filename, dir_path='./', index=False,
                encoding='utf-8-sig', **kwargs):
    file_path = os.path.join(dir_path, filename)
    kwargs.update({'index': index, 'encoding': encoding})
    df.to_csv(file_path, **kwargs)