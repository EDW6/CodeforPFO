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

TypeWithPeaks_loc = []
TypeOnlyPeaks_loc = []
TypeNoPeak_loc = []

# 对光脉冲做一个细致的划分
for i in range(len(peakLight_id)):
    print(i)
    loc = peakLight_id[i]
    data2store_ch1 = dataL_for_ch[loc - 99:loc + 100]  # 截取片段
    mean_clip = np.mean(data2store_ch1)
    data_o_diff = fun_diff(data2store_ch1)
    # plt.plot(data2store_ch1)

    mark_sign = max(data_o_diff)

    if mark_sign < 5000:
        if mean_clip > 4000:
            TypeWithPeaks_loc.append(loc)
        else:
            TypeOnlyPeaks_loc.append(loc)
    else:
        TypeNoPeak_loc.append(loc)
print('WithPeaks:%d\nOnlyPeaks:%d\nNoPeaks:%d\n' % (len(TypeWithPeaks_loc), len(TypeOnlyPeaks_loc), len(TypeNoPeak_loc)))

