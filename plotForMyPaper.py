import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from Statistics.Findlocation import find_location_of_object
from Statistics.plotforpaper import plot_venn5, norm_tabel



# base_root0 = r'////data/whjdata/520-测试/'
# namelist = ['离心1min', '离心2min', '离心3min', '离心4min', '离心5min']
# os.chdir(base_root0)
# 第一张图： 不同样品的模态分布差异，直接对world处理
# find_location_of_object(base_root0, namelist, 150, 1000, 2000) # 调参

# 模态相互作用，venn5，展示一张 venn5，是对单一样品对精细划分，
# 对abcd进行操作
# norm_tabel(base_root0, namelist)

# venn5的部分参数可以表征动态变化
# 提取venn5plot的labels
# 一共有2的5次方32种
# norm_data = pd.read_csv('normed.csv')
# print(norm_data)
# # 画出子图subplot 32个， 4*8
# plt.figure(figsize=(20, 10))
# for i in range(31):
#     plt.subplot(4, 8, i+1)
#     # print(norm_data.iloc[i,0:])
#     plt.plot(norm_data.iloc[i,0:])
# plt.savefig('norm_data.png', dpi=500)
# # plt.tick_params(top='off', bottom='off', left='off')
# plt.tick_params(labelsize=1)
# plt.clf()

# 离心梯度、超声梯度
flag_different_categories = True
if flag_different_categories:
    print('start to analyze centrifuge')
    base_root = r'//data/whjdata/0322测试/'
    os.chdir(base_root)
    namelist = ['纤细裸藻光语', '金粉PS球', '10微米荧光微球', '10微米PS']

    find_location_of_object(base_root, namelist, 100, 1000, 2000)  # 调参

    norm_tabel(base_root, namelist)

    norm_data_categories = pd.read_csv('normed.csv')
    # print(norm_data)
    # 画出子图subplot 32个， 4*8
    plt.figure(figsize=(40, 15))
    for i in range(31):
        plt.subplot(4, 8, i + 1)
        one_row = norm_data_categories.iloc[i, 0:]
        plt.bar(range(len(one_row)), one_row)
    plt.savefig('norm_data_bar.png', dpi=500)
    plt.tick_params(labelsize=1)
    plt.clf()
else:
    print('do not analyze categories')




# 离心梯度、超声梯度
flag_centrifuge = False
if flag_centrifuge:
    print('start to analyze centrifuge')
    base_root0 = r'///data/whjdata/520-测试/'
    os.chdir(base_root0)
    namelist0 = ['离心1min', '离心2min', '离心3min', '离心4min', '离心5min']

    find_location_of_object(base_root0, namelist0, 100, 1000, 2000)  # 调参

    norm_tabel(base_root0, namelist0)

    norm_data_centri = pd.read_csv('normed.csv')
    # print(norm_data)
    # 画出子图subplot 32个， 4*8
    plt.figure(figsize=(40, 15))
    for i in range(31):
        plt.subplot(4, 8, i + 1)
        one_row = norm_data_centri.iloc[i, 0:]
        plt.bar(range(len(one_row)), one_row)
    plt.savefig('norm_data_bar.png', dpi=500)
    plt.tick_params(labelsize=1)
    plt.clf()
else:
    print('do not analyze centrifuge')


# 离心梯度、超声梯度
flag_sonication = False
if flag_sonication:
    print('start to analyze sonication')
    base_root2 = r'//data/whjdata/524超声/'
    os.chdir(base_root2)
    namelist2 = ['对照-裸藻', '超声5min', '超声10min']

    find_location_of_object(base_root2, namelist2, 120, 1000, 2500)  # 调参

    norm_tabel(base_root2, namelist2)

    norm_data_sonic = pd.read_csv('normed.csv')
    # print(norm_data)
    # 画出子图subplot 32个， 4*8
    plt.figure(figsize=(40, 15))
    for i in range(31):
        plt.subplot(4, 8, i + 1)
        one_row = norm_data_sonic.iloc[i, 0:]
        plt.bar(range(len(one_row)), one_row)
    plt.savefig('norm_data_bar.png', dpi=500)
    plt.tick_params(labelsize=1)
    plt.clf()
else:
    print('do not analyze sonica')


# 先放10 um 和 5 um
# 滤膜用于解释是哪些成分。
flag_components = False
if flag_components:
    base_root1 = r'/data/whjdata/523成分实验/'
    os.chdir(base_root1)
    namelist1 = ['0.45微米滤膜', '10微米滤膜', '纤细裸藻-对照']
    find_location_of_object(base_root1, namelist1, 150, 1000, 3000) # 调参

    norm_tabel(base_root1, namelist1)

    norm_data = pd.read_csv('normed.csv')
    # print(norm_data)
    # 画出子图subplot 32个， 4*8
    plt.figure(figsize=(40, 15))
    for i in range(31):
        plt.subplot(4, 8, i+1)
        # print(norm_data.iloc[i,0:])
        one_row = norm_data.iloc[i, 0:]
        plt.bar(range(len(one_row)), one_row)
    plt.savefig('norm_data_bar.png', dpi=500)
    # plt.tick_params(top='off', bottom='off', left='off')
    plt.tick_params(labelsize=1)
    plt.clf()
else:
    print('do not analyze components')




