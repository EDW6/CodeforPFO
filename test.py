import os
import numpy as np
import struct
import time
from scipy import signal
import matplotlib.pyplot as plt




start = time.time()
filepath = r'C:/Users/WANGHONGJIAN/Desktop/ch8.bin'

end = time.time()
print(end-start)

lst = np.array(lst)
end = time.time()
print(end-start)

# en1 = lst.reshape(lst.size)
lst_s_temp = np.convolve(lst, np.ones((400,))/400, mode='same')# signal.medfilt(lst, kernel_size=401)
lst_s = lst - lst_s_temp
lst_s[:400] = 0
lst_s[len(lst_s)-400:]=0
end = time.time()
print(end-start)
print('done')