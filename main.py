# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import scipy.signal as signal
import struct
import matplotlib.pyplot as plt
import numpy as np


def get_from_bin(filepath_input):
    f = open(filepath_input, 'rb')
    byt = f.read()
    byt_size = int(len(byt) / 2) - 1
    f = open(filepath_input, 'rb')
    lst = []
    for i in range(byt_size):
        val = struct.unpack('H', f.read(2))[0]
        lst.append(val-32700)
    return lst


def gets_from_bin(filepath_input):
    lst = get_from_bin(filepath_input)
    lst = np.array(lst)
    en1 = lst.reshape(lst.size)
    lst_s_temp = signal.medfilt(en1, kernel_size=401)
    lst_s = lst - lst_s_temp
    return lst_s


def fun_diff(data):
    data_diff = []
    for i in range(len(data) - 1):
        data_diff.append(data[i + 1] - data[i])

    return data_diff


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_root = r'F:\2022多模态\0322测试'
    object_name = '纤细裸藻光语/23-19-27-0度线偏振//'
    ch_name = ['ch2.bin', 'ch3.bin', 'ch4.bin', 'ch5.bin', 'ch1.bin']

    filepath = base_root + '/' + object_name + ch_name[0]
    dataleft1 = get_from_bin(filepath)
    filepath = base_root + '/' + object_name + ch_name[1]
    data0 = get_from_bin(filepath)
    filepath = base_root + '/' + object_name + ch_name[2]
    data90 = get_from_bin(filepath)
    filepath = base_root + '/' + object_name + ch_name[3]
    data45 = get_from_bin(filepath)
    filepath = base_root + '/' + object_name + ch_name[4]
    dataf = get_from_bin(filepath)

    data_optical_all = dataleft1 + data0 + data90 + data45 + dataf

    # fig1 = plt.figure(num='fig111111')
    # plt.plot(data_optical_all)
    # plt.show()

    data_o_diff = fun_diff(data_optical_all)

    fig2 = plt.figure(num='fig121111')
    plt.plot(data_o_diff)
    plt.show()

    filepath_s = base_root + '/' + object_name + 'ch8.bin'
    datas = gets_from_bin(filepath_s)

    # 找peaks
    peak_id, peak_property = signal.find_peaks(datas, height=200, distance=20)



