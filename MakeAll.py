
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fftpack import fft


base_root = r'F:\2022多模态\0322测试\纤细裸藻光语'
ch_name = ['ch2.npy', 'ch3.npy', 'ch4.npy', 'ch5.npy', 'ch1.npy', 'ch8.npy']
ch_name = ['ch8.npy']
# 把数据访问并且叠在一起
sampling_file = os.listdir(base_root)

len_sampling = len(sampling_file)
for ch_index in ch_name:
    print(ch_index)
    data2store = []
    for list_sample in range(len_sampling):
        sample_file_name = sampling_file[list_sample]
        total_path = os.path.join(base_root, sample_file_name, ch_index)
        # 用于把全部采样的通道进行叠加
        data_for_ch = np.load(total_path)
        data2store = np.hstack([data2store, data_for_ch])
        print(len(data2store))
    print('done')
    os.chdir(base_root)
    np.save(file=ch_index, arr=data2store)



