# 整合每个采样数据集的数据到一个npy文件中

import os
import numpy as np
import pandas as pd

# 输出第一个表
# 对表进行
out_path = "../"
os.chdir(out_path)
df = pd.read_csv("0524-离心.csv")

base_root0 = r'/data/whjdata/519离心实验/'
ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy', 'ch8.npy']

namelist = ['1min', '离心2min', '离心3min',  '离心4min', '离心5min']

for name_index in range(5):
    print(namelist[name_index])
    base_root = base_root0 + namelist[name_index]
    sampling_file = os.listdir(base_root)

