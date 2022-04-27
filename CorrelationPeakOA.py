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



