import json
import csv


def eclat(copp, k):
    print('eclat')
    data = []
    vertical = {}
    eclat = {}
    
    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    f_in = '/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/result_kind.csv'

    file = open(f_in, 'r', encoding='gbk')
    reader = csv.reader((line.replace('\0', '') for line in file))
    for line in reader:
        data.append(line)
        if line[0] == copp:
            for i in line[1:]:
                eclat[i] = 0
    file.close()

    for i in range(4, 32):
        if i == 13 or i == 11:
            continue
        for j in range(k):
            vertical[str(i)+'_'+str(j)] = []

    length = len(data)
    for i in range(length):
        for j in data[i][1:]:
            vertical[j].append(i)  # 生成垂直数据集

    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/eclat.json', 'w')
    json.dump(vertical, f, ensure_ascii=False, indent=2)
    f.close()    

    for i in eclat.keys():
        eclat[i] = len(vertical[i])/length
    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/eclat_1.json', 'w')
    json.dump(eclat, f, ensure_ascii=False, indent=2)
    f.close()

    prepare['k'] = k
    prepare['length'] = length
    prepare['loc_set'] = ['', '', '', '', '', '', '', '', '', '']
    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/prepare.json', 'w')
    json.dump(prepare, f, ensure_ascii=False, indent=2)
    f.close()


if __name__ == "__main__":
    eclat('柏楚电子', 5)
