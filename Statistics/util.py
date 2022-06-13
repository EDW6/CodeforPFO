import numpy as np
from scipy.fftpack import fft


def analyse_oa_feature(Input_optical_location, oa_all_signal):
    peak_bool_set = []
    frequency_set = []
    amplitude_set = []
    len_loc = len(Input_optical_location)
    # print(len_loc)
    for i in range(len_loc):

        loc_num = Input_optical_location[i]
        OA_clip = oa_all_signal[loc_num-199:loc_num+200]
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



