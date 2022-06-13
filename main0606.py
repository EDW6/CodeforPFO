import argparse
from pipeline import extract_from_nothing, dir2extract, analysis_seq, DataProcess

print(111)
parser = argparse.ArgumentParser(description='my_device')
parser.add_argument('--pathFrom', default='',
                    help='directory of original signal')
# parser.add_argument('--filenames', default='',
#                     help='list of filenames')
parser.add_argument('--mode', default='',
                    help='1-existed; 0-not existed; 2-specific optimization')


args = parser.parse_args()
print(args)


filenames = dir2extract(args.pathFrom)

# namelist0 = ['离心1min', '离心2min', '离心3min', '离心4min', '离心5min']
if args.mode == '0':
    print('start to interpret bin data')

    extract_from_nothing(args.pathFrom, filenames)

if args.mode == '1':
    # 跑已有的
    print('start to analyze new data')
    analysis_seq(args.pathFrom, filenames, s_th=100, p_th=1000, f_th=2000)

if args.mode == '2':
    # 跑已有的
    print('start to analyze specific data')
    DataProcess(flag_different_categories=False, flag_centrifuge=False,
                flag_sonication=False, flag_components=False)