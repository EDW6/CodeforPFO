import os
import numpy as np
import matplotlib as mpl
from pipeline import analysis_seq
mpl.use('Agg')
import matplotlib.pyplot as plt

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




