#!/usr/bin/env/ python3
# 22-05-03
# 采集完成后的第一步
# 用于生成npy文件
import os
import numpy as np
import struct

from scipy import signal


def get_from_bin(filepath_input):
    print(filepath_input)
    f = open(filepath_input,'rb')
    byt = f.read()
    byt_size = int(len(byt) / 2) - 1
    f = open(filepath_input, 'rb')
    lst = []
    for i in range(byt_size):
        val = struct.unpack('H', f.read(2))[0]
        lst.append(val - 32700)
    lst = np.array(lst)
    return lst


def gets_from_bin(filepath_input):
    lst = get_from_bin(filepath_input)
    lst = np.array(lst)

    lst_s_temp = np.convolve(lst, np.ones((400,)) / 400, mode='same')  # signal.medfilt(lst, kernel_size=401)
    lst_s = lst - lst_s_temp
    lst_s[:400] = 0
    lst_s[len(lst_s) - 400:] = 0

    # lst_s = np.array(lst_s)
    return lst_s


class Bin2Num(object):
    def __init__(self,  base_root0, name_list): # self参数是类下面所有方法必须的参数
        self.base_root0 = base_root0
        self.name_list = name_list
        pass

    # 光脉冲的提取

    # 声音脉冲的提取
    def generate_number_from_bin(self):
        for name_index in range(len(self.name_list)):
            print(self.name_list)
            base_root = self.base_root0 + self.name_list[name_index]
            ch_name = ['ch2.bin', 'ch3.bin', 'ch4.bin', 'ch5.bin', 'ch1.bin']


            object_all = os.listdir(base_root)
            len_datafile = len(object_all)-1

            for list_num in range(len_datafile):
                object_name = object_all[list_num+1]
                print(object_name)
                print('processing --> %d/%d' % (list_num, len_datafile))

                os.chdir(os.path.join(base_root, object_name))
                if os.path.exists('ch4.npy'):
                    print('pass')
                else:
                    for ch_num in ch_name:
                        filepath = os.path.join(base_root, object_name, str(ch_num))
                        data_for_ch = get_from_bin(filepath)

                        os.chdir(base_root + '//' + object_name)
                        store_name = ch_num[:3] + '.npy'
                        np.save(file=store_name, arr=data_for_ch)

                    filepath_s = base_root + '/' + object_name + '/ch8.bin'
                    datas = gets_from_bin(filepath_s)
                    np.save(file='ch8.npy', arr=datas)
                    print('done')

            print('全部生成完毕')


    def make_whole_from_separate(self):
        ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy', 'ch8.npy']

        for name_index in range(len(self.name_list)):
            print(self.name_list[name_index])
            base_root = self.base_root0 + self.name_list[name_index]

            os.chdir(base_root)
            if os.path.exists('ch4.npy'):
                pass
            else:
                sampling_file = os.listdir(base_root)

                len_sampling = 11  # len(sampling_file)-2

                os.chdir(base_root)

                for ch_index in ch_name:
                    print(ch_index)
                    data2store = []
                    for list_sample in range(2, len_sampling):
                        sample_file_name = sampling_file[list_sample]
                        total_path = os.path.join(base_root, sample_file_name, ch_index)
                        # 用于把全部采样的通道进行叠加
                        data_for_ch = np.load(total_path)
                        data2store = np.hstack([data2store, data_for_ch])
                        print(len(data2store))
                    print('done')
                    os.chdir(base_root)
                    np.save(file=ch_index, arr=data2store)

        print('Please continue')

