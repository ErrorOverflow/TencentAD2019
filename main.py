import pandas as pd

# data\\totalExposureLog.out
# data\\user_data

totalExposure = pd.DataFrame(
    columns=['AD_id', 'time', 'AD_loc_id', 'user_id', 'expo_id', 'expo_size', 'expo_bid', 'expo_pctr',
             'expo_quality_ecpm',
             'expo_total_ecpm'])

with open('data\\totalExposureLog.out', 'r', encoding='utf-8') as f:
    new = open('data\\totalExposure.csv', 'w')
    i = 0
    for line in f:
        if i % 2000 == 0:
            print(i, line)
        lineContent = line.split('\t')
        if len(lineContent) != 10:
            continue
        line = line.replace('\t', ',')
        new.write(line)
        i+=1

