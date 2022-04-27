import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal
from scipy.fftpack import fft,ifft
import random

base_root = r'F:\2022多模态\0322测试\纤细裸藻光语'
ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy']


def fun_diff(data):
    data_diff = []
    for i in range(len(data) - 1):
        data_diff.append(data[i + 1] - data[i])

    return data_diff


object_all = os.listdir(base_root)
len_datafile = len(object_all)
# len_datafile - 1
for list_num in range(0, 15):
    object_name = object_all[list_num + 1]
    print(object_name)

    # 算个长度
    filepath = os.path.join(base_root, object_name, 'ch2.npy')
    data_for_ch = np.load(filepath)
    data2store = np.zeros(len(data_for_ch))

    for ch_num in ch_name:
        filepath = os.path.join(base_root, object_name, str(ch_num))
        data_for_ch = np.load(filepath)
        data2store = np.vstack([data2store, data_for_ch])

        print(data_for_ch.size)
        #
        # fig1 = plt.figure(num=str(list_num))
        # plt.plot(data_for_ch,label=ch_num[:3])
        # plt.legend()
        # plt.show()
    # OA通道
    filepath = os.path.join(base_root, object_name, 'ch8.npy')
    datas_for_ch = np.load(filepath)

    # 不同OA对应的光的信号的片段提取
    # 找peaks,记录声音的位置
    peak_id, peak_property = signal.find_peaks(datas_for_ch, height=200, distance=500)

    peak_bool_set = []
    frequency_mean_set = []
    # 找每个位置附近的差分片段
    for i in range(len(peak_id)):
        # 这个声音的片段的特征提取
        data2sound = datas_for_ch[peak_id[i] - 299:peak_id[i] + 300]
        # 统计1：fft频谱的情况
        fft_s = abs(fft(data2sound))
        fft_s[0] = 0
        frequency_mean = np.mean(fft_s[:int(len(fft_s)/2)])
        frequency_mean_set.append(frequency_mean)
        # 统计2：长度；高度（待做）

        # 这里是对应的peak是否是尖峰的标记
        data2store_ch1 = data2store[1, peak_id[i] - 299:peak_id[i] + 300]
        # plt.plot(data2store_ch1)
        # plt.show()
        data_o_diff = fun_diff(data2store_ch1)
        mark_sign = max(data_o_diff)

        if mark_sign > 2000:
            peak_bool = 1
        else:
            peak_bool = 0
        peak_bool_set.append(peak_bool)

    new_peak_bool_set = [i + 0.3*np.random.rand() for i in peak_bool_set] # 列表生成式
    plt.scatter(frequency_mean_set, new_peak_bool_set)
    plt.show()














