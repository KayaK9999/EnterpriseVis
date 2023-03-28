import json
import csv


def axis(k):
    data_kind = []
    data_copp = []
    vertical = {}
    axis = {}
    f = open('D:/File/毕业论文/DATA/数据处理/result_kind.csv', 'r')
    reader = csv.reader(f)
    for line in reader:
        data_kind.append(line)
    f.close()
    f = open('D:/File/毕业论文/DATA/数据处理/result_detail.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        data_copp.append(line)
    f.close()

    for i in range(4, 32):
        if i == 13 or i == 11:
            continue
        axis[str(i)] = []
        for j in range(k):
            vertical[str(i)+'_'+str(j)] = [[], 0]

    length = len(data_kind)
    for i in range(length):
        for j in data_kind[i][1:]:
            pos = int(j[:j.rfind('_')])
            vertical[j][0].append(float(data_copp[i][pos]))
            vertical[j][1] += 1
    for i in vertical:
        temp = [min(vertical[i][0])-1, max(vertical[i][0])+1]
        vertical[i][0] = temp
        vertical[i][1] = vertical[i][1]/length
    for i in vertical:
        pos = i[:i.rfind('_')]
        axis[pos].append({i: vertical[i]})

    f = open('D:/File/毕业论文/DATA/数据处理/axis.json', 'w')
    json.dump(axis, f, ensure_ascii=False, indent=2)
    f.close()


if __name__ == "__main__":
    axis(5)
