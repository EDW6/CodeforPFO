
import os
import numpy as np
from Preprocessing.GenerateNPY import generate_number_from_bin
from Preprocessing.MakeAll import make_whole_from_separate
from Statistics.Findlocation import find_location_of_object

base_root0 = r'///data/whjdata/连续测量每天/'
print(base_root0)
namelist = os.listdir(base_root0)
print(namelist)


# generate_number_from_bin(base_root0, namelist)
# make_whole_from_separate(base_root0, namelist)
find_location_of_object(base_root0, namelist)
