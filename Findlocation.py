import os
import numpy as np
from scipy import signal
from Statistics.util import Analyse_OA_feature
from Statistics.util import fun_diff
from Statistics.util import comprison_counts

name_list = ['纤细裸藻光语', '裸藻-状态可能不好了-水生所的', '金粉PS球',
             '10微米荧光微球', '10微米PS']
f1all = []
a1all = []
f2all = []
a2all = []
f3all = []
a3all = []

for name_index in range(len(name_list)):
    base_root = r'/data/whjdata/0322测试/' + name_list[name_index]
    ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy', 'ch8.npy']
    height_threshold = []

    filepath = os.path.join(base_root, 'ch8.npy')
    datas_for_ch = np.load(filepath)

    # 找peaks,记录声音的位置
    Sound_id, peakS_value = signal.find_peaks(datas_for_ch, height=150, distance=600)  # 考虑到声音更短

    filepath = os.path.join(base_root, 'ch2.npy')  # 先通过ch2做一个演示
    dataL_for_ch = np.load(filepath)

    # 光颗粒物的位置，然后分类不同的颗粒物的情况，通过diff
    peakLight_id, peakLight_value = signal.find_peaks(dataL_for_ch, height=1000, distance=400)

    # 通过光信号找声音
    TypeWithPeaks_loc = []
    TypeOnlyPeaks_loc = []
    TypeNoPeak_loc = []
    Peaks_store = []
    # 对光脉冲做一个细致的划分成三大类
    for i in range(len(peakLight_id)):
        # print(i)
        loc = peakLight_id[i]
        data2store_ch1 = dataL_for_ch[loc - 199:loc + 200]  # 截取片段
        mean_clip = np.mean(data2store_ch1)
        data_o_diff = fun_diff(data2store_ch1)
        # plt.plot(data2store_ch1)

        mark_sign = max(data_o_diff)

        if mark_sign > 2000:  # 单次间隔采样点的变化超过2000
            if mean_clip > 1000:  # 一段信号的平均数
                TypeWithPeaks_loc.append(loc)
            else:
                TypeOnlyPeaks_loc.append(loc)
            Peaks_store.append(loc)
        else:
            TypeNoPeak_loc.append(loc)

    # print('WithPeaks:%d\nOnlyPeaks:%d\nNoPeaks:%d\n'
    # % (len(TypeWithPeaks_loc), len(TypeOnlyPeaks_loc), len(TypeNoPeak_loc)))

    # 声音信号与光信号的一个对比
    sum_same1 = comprison_counts(Peaks_store, Sound_id)
    # print('peak信号下的声音信号%d\npeaks的总体长度%d' % (sum_same1, len(Peaks_store)))
    # 通过声音信号的位置检索附近有没有peak呢
    sum_same2 = comprison_counts(Sound_id, Peaks_store)
    # print('sound信号下的光信号%d\nsound的总体长度%d' % (sum_same2, len(Sound_id)))

    # get the features of sound for three categories of optical pulses

    print('===sound_feature_analysing====')
    f1set, a1set = Analyse_OA_feature(TypeWithPeaks_loc, datas_for_ch)
    f2set, a2set = Analyse_OA_feature(TypeOnlyPeaks_loc, datas_for_ch)
    f3set, a3set = Analyse_OA_feature(TypeNoPeak_loc, datas_for_ch)
    # print('===sound_feature_done====')

    # print('脉冲+尖峰：%f, %f\n只有尖峰：%f, %f\n 脉冲：%f, %f'
    #       % (f1set, a1set,
    #          f2set, a2set,
    #          f3set, a3set))

    f1all.append(f1set)
    a1all.append(a1set)
    f2all.append(f2set)
    a2all.append(a2set)
    f3all.append(f3set)
    a3all.append(a3set)
