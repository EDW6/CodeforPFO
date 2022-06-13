import numpy as np
import pandas as pd
import os

from scipy import signal

print(0)


def range_encode(peak_id):
    # 每500个数为一个编码
    encode_id = []
    for i in range(len(peak_id)):
        current_id = peak_id[i] // 300
        encode_id.append(current_id)
    return encode_id


def fun_diff(data):
    data_diff = []
    for i in range(len(data) - 1):
        data_diff.append(data[i + 1] - data[i])
    return data_diff


def peak_location(base_root, npy, height_num, dis_num):
    filepath_ch = os.path.join(base_root, npy)  # f
    dataL_for_ch = np.load(filepath_ch)
    dataL_for_ch = dataL_for_ch - np.mean(dataL_for_ch)  # 去基线
    peakLight_ch, val_ch = signal.find_peaks(dataL_for_ch, height=height_num, distance=dis_num)
    return peakLight_ch, val_ch, dataL_for_ch


def split2(peakLight_id, P_signal):
    # 对提取到的peakLight_id进行细致的划分，找到所有脉冲、尖峰、荧光
    # 一个id可以对应多个
    NotinationPeaks_loc = []

    for i in range(len(peakLight_id)):
        # print(i)
        loc = peakLight_id[i]
        dataclip_P = P_signal[loc - 199:loc + 200]  # 截取片段

        # 均值用来确定是否是足够大的pulse
        # meanP_clip = np.mean(dataclip_P)
        data_o_diff = fun_diff(dataclip_P)
        mark_sign = max(data_o_diff)

        if mark_sign > 1500:  # 单次间隔采样点的变化超过2000
            NotinationPeaks_loc.append(loc)
        else:
            pass
    return NotinationPeaks_loc


def find_location_of_object(base_root0, namelist, s_th, p_th, f_th):
    df = pd.DataFrame(np.arange(4*len(namelist)).reshape((4, len(namelist))),
                      index=['脉冲', '尖峰', '荧光', '声音'],
                      columns=namelist)

    for name_index in range(len(namelist)):
        base_root = base_root0 + namelist[name_index]
        ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy', 'ch8.npy']  # ch1---f
        print(name_index)
        # 找peaks,记录声音的位置
        Sound_id, peakS_value, data_s = peak_location(base_root, 'ch8.npy', s_th, 400)  # 考虑到声音更短

        # 光颗粒物的位置，ch1--f, ch2--p
        peakLight_p, val_p, data_p = peak_location(base_root, 'ch4.npy', p_th, 400)
        peakLight_f, val_f, data_f = peak_location(base_root, 'ch1.npy', f_th, 400)

        print(2)
        Peaks_loc = split2(peakLight_p, data_p)

        print(3)
        df.iloc[0, name_index] = len(peakLight_p)
        df.iloc[1, name_index] = len(Peaks_loc)
        df.iloc[2, name_index] = len(peakLight_f)
        df.iloc[3, name_index] = len(Sound_id)

        print(df)
        os.chdir(base_root0)

        encode_id1 = range_encode(peakLight_p)
        np.save(str('a' + str(name_index) + '.npy'), encode_id1)
        encode_id2 = range_encode(Peaks_loc)
        np.save(str('b' + str(name_index) + '.npy'), encode_id2)
        encode_id3 = range_encode(peakLight_f)
        np.save(str('c' + str(name_index) + '.npy'), encode_id3)
        encode_id4 = range_encode(Sound_id)
        np.save(str('d' + str(name_index) + '.npy'), encode_id4)

        # 输出第一个表
    out_path = "./tem_file.csv"
    df.to_csv(out_path, encoding="utf_8_sig")
