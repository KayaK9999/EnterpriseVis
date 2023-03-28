import json
import csv


def eclat(copp, k):

    data = []
    vertical = {}
    eclat = {}
    
    f = open('D:/File/毕业论文/DATA/数据处理/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    f_in = 'D:/File/毕业论文/DATA/数据处理/result_kind.csv'

    file = open(f_in, 'r')
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

    f = open('D:/File/毕业论文/DATA/数据处理/eclat.json', 'w')
    json.dump(vertical, f, ensure_ascii=False, indent=2)
    f.close()    

    for i in eclat.keys():
        eclat[i] = len(vertical[i])/length
    f = open('D:/File/毕业论文/DATA/数据处理/eclat_1.json', 'w')
    json.dump(eclat, f, ensure_ascii=False, indent=2)
    f.close()

    prepare['k'] = k
    prepare['length'] = length
    prepare['loc_set'] = ['', '', '', '', '', '', '', '', '', '']
    f = open('D:/File/毕业论文/DATA/数据处理/prepare.json', 'w')
    json.dump(prepare, f, ensure_ascii=False, indent=2)
    f.close()


if __name__ == "__main__":
    eclat('柏楚电子', 5)
