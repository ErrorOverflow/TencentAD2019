import pandas as pd
import numpy as np

# data\\totalExposureLog.out
# data\\user_data
# data\\ad_operation.dat
# data\\test_sample.dat
# data\\ad_static_feature.out
totalExposure = pd.DataFrame(
    columns=['AD_id', 'time', 'AD_loc_id', 'user_id', 'expo_id', 'expo_size', 'expo_bid', 'expo_pctr',
             'expo_quality_ecpm',
             'expo_total_ecpm'])

ad_static_feature = pd.DataFrame(
    columns=['AD_id', 'time', 'account_id', 'product_id', 'product_class', 'industry_id', 'size'])

user = pd.DataFrame(
    columns=['user_id', 'age', 'gender', 'area', 'status', 'education', 'consumption_ability', 'device', 'work',
             'connect_type',
             'behavior'])

ADExposure = pd.DataFrame(columns=['num'])


def preTotalExposure():
    with open('data\\totalExposure', 'r', encoding='utf-8') as f:
        new = open('data\\ad_static_feature.csv', 'w')
        i = 0
        for line in f:
            if i % 1000000 == 0:
                print(i, line)
            if i == 0:
                new.write(
                    'AD_id,time,AD_loc_id,user_id,expo_id,expo_size,expo_bid,expo_pctr,expo_quality_ecpm,'
                    'expo_total_ecpm\n')
                lineContent = line.split('m')
                print(lineContent[len(lineContent) - 1])
                new.write(lineContent[len(lineContent) - 1])
            else:
                new.write(line)
            i += 1


def preADStatic():
    with open('data\\ad_static_feature.out', 'r', encoding='utf-8') as f:
        new = open('data\\ad_static_feature.csv', 'w')
        new.write('AD_id,time,account_id,product_id,product_class,industry_id,size,is_multi_size\n')
        for line in f:
            line = line.replace('\n', '')
            lineContent = line.split('\t')
            if len(lineContent) == 7 and lineContent[6] == '':
                for i in range(3):
                    new.write(lineContent[i] + ',')
                new.write('0,')
                new.write(lineContent[3] + ',')
                new.write(lineContent[4] + ',')
                if ',' in lineContent[5]:
                    size = 0
                    size_tmp = lineContent[5].split(',')
                    for _ in size_tmp:
                        size += int(_)
                    size /= len(size_tmp)
                    new.write(str(size) + ',1\n')
                else:
                    new.write(lineContent[5] + ',0\n')
            elif len(lineContent) == 7:
                for i in range(6):
                    new.write(lineContent[i] + ',')
                if ',' in lineContent[6]:
                    size = 0
                    size_tmp = lineContent[6].split(',')
                    for _ in size_tmp:
                        size += int(_)
                    size /= len(size_tmp)
                    new.write(str(size) + ',1\n')
                else:
                    new.write(lineContent[6] + ',0\n')
            else:
                print('ERROR: ', line)


'''
'''


def preUser():
    with open('data\\user_data', 'r', encoding='utf-8') as f:
        new = open('data\\user_data.csv', 'w')
        i = 0
        for line in f:
            if i == 0:
                new.write(
                    'user_id,age,gender,area,status,education,consumption_ability,device,work,connect_type,behavior\n')
            line = line.replace('\t', ',')
            new.write(line)
            if i % 100000 == 0:
                print(i, line)
            i += 1


def countTotalExposure():
    with open('data\\totalExposure.csv', 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            print(line)
            line = line.replace('\n', '')
            lineContent = line.split('\t')
            if i % 100000 == 0:
                print(lineContent[0])
            try:
                ADExposure.loc[lineContent[0]] = ADExposure.loc[lineContent[0]] + 1
            except:
                ADExposure.loc[lineContent[0]] = 0
            i += 1



countTotalExposure()
print(ADExposure.index.is_unique)
