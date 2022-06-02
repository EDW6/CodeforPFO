import numpy as np
from Statistics.util import peaklocation, split2PeaksPulse, range_encode
import pandas as pd
import os

print(0)


def find_location_of_object(base_root0, namelist, s_th, p_th, f_th):
    f1all = []
    a1all = []
    f2all = []
    a2all = []
    f3all = []
    a3all = []

    df = pd.DataFrame(np.arange(5*len(namelist)).reshape((5, len(namelist))),
                      index=['脉冲', '脉冲+尖峰','尖峰', '荧光', '声音'],
                      columns=namelist)

    for name_index in range(len(namelist)):
        base_root = base_root0 + namelist[name_index]
        ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy', 'ch8.npy']  # ch1---f
        print(name_index)
        # 找peaks,记录声音的位置
        Sound_id, peakS_value, data_s = peaklocation(base_root, 'ch8.npy', s_th, 400)  # 考虑到声音更短

        # 光颗粒物的位置，ch1--f, ch2--p
        peakLight_p, val_p, data_p = peaklocation(base_root, 'ch4.npy', p_th, 400)
        peakLight_f, val_f, data_f = peaklocation(base_root, 'ch1.npy', f_th, 400)


        print(2)
        Pulse_loc, Peaks_loc, co_loc = split2PeaksPulse(peakLight_p, data_p)

        print(3)
        df.iloc[0, name_index] = len(Pulse_loc)
        df.iloc[1, name_index] = len(co_loc)
        df.iloc[2, name_index] = len(Peaks_loc)
        df.iloc[3, name_index] = len(peakLight_f)
        df.iloc[4, name_index] = len(Sound_id)

        print(df)

        encode_id1 = range_encode(Pulse_loc)

        os.chdir(base_root0)
        np.save(str('a' + str(name_index) + '.npy'), encode_id1)
        encode_id2 = range_encode(co_loc)
        np.save(str('b' + str(name_index) + '.npy'), encode_id2)
        encode_id3 = range_encode(Peaks_loc)
        np.save(str('c' + str(name_index) + '.npy'), encode_id3)
        encode_id4 = range_encode(peakLight_f)
        np.save(str('d' + str(name_index) + '.npy'), encode_id4)
        encode_id5 = range_encode(Sound_id)
        np.save(str('e' + str(name_index) + '.npy'), encode_id5)

        # 输出第一个表
    out_path = "./0524-离心1.csv"
    df.to_csv(out_path, encoding="utf_8_sig")
