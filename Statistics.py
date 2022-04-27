import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import signal

base_root = r'F:\2022多模态\0322测试\裸藻-状态可能不好了-水生所的'
ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy']


def fun_diff(data):
    data_diff = []
    for i in range(len(data) - 1):
        data_diff.append(data[i + 1] - data[i])

    return data_diff


object_all = os.listdir(base_root)
len_datafile = len(object_all)
# len_datafile - 1
for list_num in range(1):
    object_name = object_all[list_num + 1]
    print(object_name)
    data2store = np.zeros(2854399)

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
    filepath = os.path.join(base_root, object_name, 'ch8.npy')
    datas_for_ch = np.load(filepath)


    # 不同OA对应的光的信号的片段提取
    # 找peaks
    peak_id, peak_property = signal.find_peaks(datas_for_ch, height=100, distance=200)

    peak_bool_set = []
    # 找每个位置附近的差分片段
    for i in range(len(peak_id)):
        data2store_ch1 = data2store[1,peak_id[i]-399:peak_id[i]+400]
        data_o_diff = fun_diff(data2store_ch1)
        mark_sign = max(data_o_diff)
        if mark_sign > 1000:
            peak_bool = 1
        else:
            peak_bool = 0
        peak_bool_set.append(peak_bool)















