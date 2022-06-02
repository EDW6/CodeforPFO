import os
import numpy as np
from scipy import signal
from scipy.fftpack import fft
import struct

class bin2num(object):
    def __init__(self): #self参数是类下面所有方法必须的参数
        pass

    # 光脉冲的提取
    def get_from_bin(filepath_input):
        f = open(filepath_input, 'rb')
        byt = f.read()
        byt_size = int(len(byt) / 2) - 1
        f = open(filepath_input, 'rb')
        lst = []
        for i in range(byt_size):
            val = struct.unpack('H', f.read(2))[0]
            lst.append(val - 32700)
        lst = np.array(lst)
        return lst

    # 声音脉冲的提取
    def gets_from_bin(filepath_input):
        lst = get_from_bin(filepath_input)
        lst = np.array(lst)
        en1 = lst.reshape(lst.size)
        lst_s_temp = signal.medfilt(en1, kernel_size=401)
        lst_s = lst - lst_s_temp
        # lst_s = np.array(lst_s)
        return lst_s


class locextract(object):
    def __init__(self): #self参数是类下面所有方法必须的参数
        pass

    def peaklocation(base_root, npy, height_num, dis_num):
        filepath_ch = os.path.join(base_root, npy)  # f
        dataL_for_ch = np.load(filepath_ch)
        dataL_for_ch = dataL_for_ch - np.mean(dataL_for_ch)  # 去基线
        peakLight_ch, val_ch = signal.find_peaks(dataL_for_ch, height=height_num, distance=dis_num)
        return peakLight_ch, val_ch, dataL_for_ch

    def fun_diff(data):
        data_diff = []
        for i in range(len(data) - 1):
            data_diff.append(data[i + 1] - data[i])
        return data_diff

    def split2PeaksPulse(peakLight_id, P_signal):
        # 对提取到的peakLight_id进行细致的划分，找到所有脉冲、尖峰、荧光
        # 一个id可以对应多个
        NotinationPulse_loc = []
        NotinationPeaks_loc = []
        NotinationPeakandPulse_loc = []
        for i in range(len(peakLight_id)):
            # print(i)
            loc = peakLight_id[i]
            dataclip_P = P_signal[loc - 199:loc + 200]  # 截取片段

            # 均值用来确定是否是足够大的pulse
            meanP_clip = np.mean(dataclip_P)

            data_o_diff = fun_diff(dataclip_P)

            mark_sign = max(data_o_diff)

            if mark_sign > 1500:  # 单次间隔采样点的变化超过2000
                if meanP_clip < 1500:  # 一段信号的平均数
                    NotinationPeaks_loc.append(loc)
                else:
                    NotinationPeakandPulse_loc.append(loc)
            else:
                NotinationPulse_loc.append(loc)
        return NotinationPulse_loc, NotinationPeaks_loc, NotinationPeakandPulse_loc


class featureextract(object):
    def __init__(self): #self参数是类下面所有方法必须的参数
        pass

    def Analyse_OA_feature(Input_optical_location, OA_all_signal):
        peak_bool_set = []
        frequency_set = []
        amplitude_set = []
        len_loc = len(Input_optical_location)
        # print(len_loc)
        for i in range(len_loc):

            loc_num = Input_optical_location[i]
            OA_clip = OA_all_signal[loc_num-199:loc_num+200]
            max_OA = np.max(OA_clip)

            #找这个脉冲片段对应是否存在声音，若存在的话
            if (max_OA > 150):
                # 统计1：fft频谱的情况
                fft_s = abs(fft(OA_clip))
                fft_s[0] = 0
                frequency_mean = np.mean(fft_s[:int(len(fft_s) / 2)])

                # 统计2：高度,振幅情况
                abs_sound = abs(OA_clip)
                abs_sound_mean = np.max(abs_sound)

                # plt.plot(data2sound)
                frequency_set.append(frequency_mean)
                amplitude_set.append(abs_sound_mean)
            else:
                continue

        frequency_set_mean = np.mean(frequency_set)
        amplitude_set_mean = np.mean(amplitude_set)

        return frequency_set_mean,amplitude_set_mean


    def comprison_counts(interest_target, comparision_target):
        sum_num = 0
        for i in range(len(interest_target)):
            Peaks_temp_analyse = interest_target[i]
            number_id_diff = comparision_target - Peaks_temp_analyse
            diff_abs = abs(number_id_diff)
            min_diff = np.min(np.min(diff_abs))

            if min_diff < 400:  # 同时出现的判据：两者出现的位置
                sum_num = sum_num + 1
            else:
                sum_num = sum_num
        return sum_num


    def OrFluor(loc_peak, ch_fluor):
        sum_if_fluor = 0
        mean_fluor_set = []
        for i in range(len(loc_peak)):
            loc_num = loc_peak[i]
            fluor_clip = ch_fluor[loc_num - 199:loc_num + 200]
            mean_fluor = np.mean(fluor_clip)
            if mean_fluor>1000:
                sum_if_fluor = sum_if_fluor + 1
                mean_fluor_set.append(mean_fluor)
        rate_fluor_allpeak = sum_if_fluor/len(loc_peak)
        mean_set = np.mean(mean_fluor_set)
        return rate_fluor_allpeak, mean_set


    def range_encode( peakid):
        # 每500个数为一个编码
        encode_id = []
        for i in range(len(peakid)):
            current_id = peakid[i] // 300
            encode_id.append(current_id)
        return encode_id

