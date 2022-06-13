import os
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from Statistics.venn import get_labels, venn4


def plot_venn4(labels):
    # 画图 会保存得到五个venn图，
    plt.figure()  # 控制图尺寸的同时，使图高分辨率（高清）显示
    feature_name = ['Pulse', 'Peak', 'Fluorescence', 'Sound']
    g = venn4(labels, names=list(feature_name))
    # plt.show()
    plt.savefig('venn.png', dpi=600)
    plt.clf()


def norm_tabel(base_root0, namelist):
    os.chdir(base_root0)
    all_num = 15
    data_df_norm = pd.DataFrame(np.arange(all_num*len(namelist)).reshape((all_num, len(namelist))),
                                columns=namelist)

    for i in range(len(namelist)):
        encode_id1 = np.load(r'./a' + str(i) + '.npy')
        encode_id2 = np.load(r'./b' + str(i) + '.npy')
        encode_id3 = np.load(r'./c' + str(i) + '.npy')
        encode_id4 = np.load(r'./d' + str(i) + '.npy')

        my_dpi = 150
        labels = get_labels([encode_id1, encode_id2, encode_id3, encode_id4], fill=["number"])

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

    return labels

