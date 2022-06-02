import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Statistics.venn import venn5, get_labels
plt.rcParams ['font.sans-serif'] = ['SimHei']
plt.rcParams ['axes.unicode_minus'] = False
mpl.use('Agg')

def find_location_of_object(base_root0):

    feature_name = ['Pulse', 'Pulse+Peak', 'Peak', 'Fluorescence', 'Sound']
    os.chdir(base_root0)

    for i in range(5):
        print(i)
        encode_id1 = np.load(r'./a' + str(i) + '.npy')
        encode_id2 = np.load(r'./b' + str(i) + '.npy')
        encode_id3 = np.load(r'./c' + str(i) + '.npy')
        encode_id4 = np.load(r'./d' + str(i) + '.npy')
        encode_id5 = np.load(r'./e' + str(i) + '.npy')

        my_dpi = 150
        labels = get_labels([encode_id1, encode_id2, encode_id3,
                             encode_id4, encode_id5], fill=["number"])

        plt.figure()  # 控制图尺寸的同时，使图高分辨率（高清）显示
        g = venn5(labels, names=list(feature_name))
        # plt.show()
        plt.savefig(str(str(i) + '.png'), dpi=600)
        plt.clf()

        print(1)
