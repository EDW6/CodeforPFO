import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft


def fun_diff(data):
    data_diff = []
    for i in range(len(data) - 1):
        data_diff.append(data[i + 1] - data[i])
    return data_diff


base_root = r'F:\2022多模态\0322测试\纤细裸藻光语'
ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy', 'ch8.npy']
height_threshold = []

filepath = os.path.join(base_root, 'ch8.npy')
datas_for_ch = np.load(filepath)
# 找peaks,记录声音的位置
peakS_id, peakS_property = signal.find_peaks(datas_for_ch, height=200, distance=500)

filepath = os.path.join(base_root, 'ch2.npy') # 先通过ch2做一个演示
dataL_for_ch = np.load(filepath)

# 光颗粒物的位置，然后分类不同的颗粒物的情况，通过diff
peakLight_id, peakLight_value = signal.find_peaks(dataL_for_ch, height=2000, distance=500)
Type1_loc = []
Type2_loc = []
Type3_loc = []
# 对光脉冲做一个细致的划分
for i in range(len(peakLight_id)):
    loc = peakLight_id[i]
    data2store_ch1 = dataL_for_ch[1, loc[i] - 99:loc[i] + 100] # 截取片段
    data_o_diff = fun_diff(dataL_for_ch)
    mark_sign = max(data_o_diff)

    if mark_sign < 200:
        Type1_loc.append(loc)
    elif mark_sign > 200 & mark_sign < 2000:
        Type2_loc.append(loc)
    elif mark_sign > 2000:
        Type3_loc.append(loc)
