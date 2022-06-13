import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from Statistics.Findlocation import find_location_of_object
from Statistics.out import plot_venn4, norm_tabel
from Preprocessing.GenerateNPY import Bin2Num


def dir2extract(baseroot):
    files = os.listdir(baseroot)
    namelist = []
    for file in files:
        # 得到该文件下所有目录的路径
        m = os.path.join(baseroot, file)
        # 判断该路径下是否是文件夹
        if os.path.isdir(m):
            h = os.path.split(m)
            namelist.append(h[1])
    print(namelist)
    input_num = input("plz input which to extract:")
    print(input_num)
    name_list = [namelist[int(index)] for index in input_num]
    # namelist(int(index))
    print(name_list)
    return name_list


def extract_from_nothing(base_root0, name_list):
    print(1)
    # 从二进制到十进制
    bin2num = Bin2Num(base_root0, name_list)
    bin2num.generate_number_from_bin()
    bin2num.make_whole_from_separate()


def analysis_seq(base_root, namelist, s_th=100, p_th=1000, f_th=2000):
    # 现在的多模态分析，这里针对的是位置和相互依存关系的分析
    all_num = 15
    x_labels = ['S', 'F', 'S+F', 'P', 'S+P', 'F+P', 'S+F+P',
                'PU', 'PU+S', 'PU+F', 'PU+F+S', 'PU+P', 'PU+S+P', 'PU+P+F', 'PU+P+F+S']
    # location of each modality
    find_location_of_object(base_root, namelist, s_th, p_th, f_th)  # 调参

    # genrate a normalized table
    labels_draw = norm_tabel(base_root, namelist)

    # draw the related venn4
    plot_venn4(labels_draw)

    norm_data_categories = pd.read_csv('normed.csv')
    # print(norm_data)
    # 画出子图subplot 32个， 4*8
    plt.figure(figsize=(40, 10))
    for i in range(all_num):
        plt.subplot(2, 8, i + 1)
        one_row = norm_data_categories.iloc[i, 0:]
        plt.bar(range(len(one_row)), one_row)
        plt.xlabel(x_labels[i], fontsize='large')
    plt.savefig('norm_data_bar.png', dpi=200)
    plt.tick_params(labelsize=1)
    plt.clf()


class DataProcess:
    def __init__(self,
                 flag_different_categories=False,
                 flag_centrifuge=False,
                 flag_sonication=False,
                 flag_components=False):

        self.flag_different_categories = flag_different_categories
        self.flag_centrifuge = flag_centrifuge
        self.flag_sonication = flag_sonication
        self.flag_components = flag_components

    def run_specific(self):
        # 不同类别
        if self.flag_different_categories:
            print('start to analyze centrifuge')
            base_root = r'//data/whjdata/0322测试/'
            namelist = ['纤细裸藻光语', '金粉PS球', '10微米荧光微球', '10微米PS']
            os.chdir(base_root)
            analysis_seq(base_root, namelist)
        else:
            print('do not analyze categories')

        # 离心梯度
        if self.flag_centrifuge:
            print('start to analyze centrifuge')
            base_root0 = r'///data/whjdata/520-测试/'
            os.chdir(base_root0)
            namelist0 = ['离心1min', '离心2min', '离心3min', '离心4min', '离心5min']
            analysis_seq(base_root0, namelist0)
        else:
            print('do not analyze centrifuge')

        # 超声梯度
        if self.flag_sonication:
            print('start to analyze sonication')
            base_root2 = r'//data/whjdata/524超声/'
            os.chdir(base_root2)
            namelist2 = ['对照-裸藻', '超声5min', '超声10min']
            analysis_seq(base_root2, namelist2)
        else:
            print('do not analyze sonica')

        # 先放10 um 和 5 um
        # 滤膜用于解释是哪些成分。
        if self.flag_components:
            base_root1 = r'/data/whjdata/523成分实验/'
            os.chdir(base_root1)
            namelist1 = [ '纤细裸藻-对照', '10微米滤膜', '0.45微米滤膜']
            analysis_seq(base_root1, namelist1)
        else:
            print('do not analyze components')




