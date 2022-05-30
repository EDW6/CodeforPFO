import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from pyvenn.venn import get_labels,venn5
from Statistics.Findlocation import find_location_of_object


def plot_venn5(labels):
    # 画图 会保存得到五个venn图，
    plt.figure()  # 控制图尺寸的同时，使图高分辨率（高清）显示
    feature_name = ['Pulse', 'Pulse+Peak', 'Peak', 'Fluorescence', 'Sound']
    g = venn5(labels, names=list(feature_name))
    # plt.show()
    plt.savefig(str(str(i) + '.png'), dpi=600)
    plt.clf()


def norm_tabel(base_root0, namelist):
    os.chdir(base_root0)
    data_df_norm = pd.DataFrame(np.arange(31*len(namelist)).reshape((31, len(namelist))),
                                columns=namelist)

    for i in range(len(namelist)):
        encode_id1 = np.load(r'./a' + str(i) + '.npy')
        encode_id2 = np.load(r'./b' + str(i) + '.npy')
        encode_id3 = np.load(r'./c' + str(i) + '.npy')
        encode_id4 = np.load(r'./d' + str(i) + '.npy')
        encode_id5 = np.load(r'./e' + str(i) + '.npy')

        my_dpi = 150
        labels = get_labels([encode_id1, encode_id2, encode_id3,
                             encode_id4, encode_id5], fill=["number"])

        # 用pds把labels（dict）保存下来
        # 用总和归一化
        label_num = labels.values()
        data_df = [int(x) for x in label_num]
        data_df_sum = sum(data_df)
        list2df = pd.DataFrame(np.divide(data_df, data_df_sum))
        data_df_norm[namelist[i]] = list2df

    # 保存
    os.chdir(base_root0)
    name_norm_csv = 'normed' + '.csv'
    data_df_norm.to_csv(name_norm_csv, index = False)
    print('done for the norm table')


base_root0 = r'////data/whjdata/520-测试/'
namelist = ['离心1min', '离心2min', '离心3min', '离心4min', '离心5min']
os.chdir(base_root0)
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




# 先放10 um 和 5 um
# 滤膜用于解释是哪些成分。

base_root1 = r'/data/whjdata/523成分实验/'
os.chdir(base_root1)
namelist1 = ['0.45微米滤膜', '10微米滤膜', '纤细裸藻-对照']
find_location_of_object(base_root0, namelist, 150, 1000, 3000) # 调参

norm_tabel(base_root1, namelist1)

norm_data = pd.read_csv('normed.csv')
# print(norm_data)
# 画出子图subplot 32个， 4*8
plt.figure(figsize=(20, 10))
for i in range(31):
    plt.subplot(4, 8, i+1)
    # print(norm_data.iloc[i,0:])
    one_row = norm_data.iloc[i, 0:]
    plt.bar(range(len(one_row)), one_row)
plt.savefig('norm_data_bar.png', dpi=500)
# plt.tick_params(top='off', bottom='off', left='off')
plt.tick_params(labelsize=1)
plt.clf()



