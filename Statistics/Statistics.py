import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft


base_root = r'F:\2022多模态\0322测试\纤细裸藻光语'
ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy']
peak_bool_set = []
frequency_mean_set = []
frequency_peaks = []
frequency_nopeaks = []


def fun_diff(data):
    data_diff = []
    for i in range(len(data) - 1):
        data_diff.append(data[i + 1] - data[i])
    return data_diff


object_all = os.listdir(base_root)
len_datafile = len(object_all)

# len_datafile - 1
# 读入采样的文件夹
for list_num in range(0, 40):
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

    # 找每个位置附近的差分片段
    for i in range(len(peak_id)):
        # 这个声音的片段的特征提取
        data2sound = datas_for_ch[peak_id[i] - 49:peak_id[i] + 100]
        # 统计1：fft频谱的情况
        fft_s = abs(fft(data2sound))
        fft_s[0] = 0
        frequency_mean = np.mean(fft_s[:int(len(fft_s)/2)])

        # 统计2：高度,振幅情况
        abs_sound = abs(data2sound)
        abs_sound_mean = np.mean(abs_sound)
        # plt.plot(data2sound)

        # 这里是对应的peak是否是尖峰的标记
        data2store_ch1 = data2store[1, peak_id[i] - 99:peak_id[i] + 100]
        # plt.plot(data2store_ch1)
        # plt.show()
        data_o_diff = fun_diff(data2store_ch1)
        mark_sign = max(data_o_diff)

        if mark_sign > 200:
            peak_bool = 1
            frequency_peaks.append(abs_sound_mean)
        else:
            peak_bool = 0
            frequency_nopeaks.append(abs_sound_mean)
        peak_bool_set.append(peak_bool)

plt.boxplot([frequency_peaks, frequency_nopeaks])
plt.xlabel("Peaks or not", fontsize=20)
plt.ylabel("Acoustic amplitude", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()
















