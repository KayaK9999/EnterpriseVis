import json
import csv


def point(level):
    if level <= 1:
        return 0

    data_copp = []
    point = {}
    circul = [0, 0, [], []]

    f = open('D:/File/毕业论文/DATA/数据处理/result_detail.csv', 'r')
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        data_copp.append(line)
        # point[line[3]] = [[0, 0], '']
    f.close()

    f = open('D:/File/毕业论文/DATA/数据处理/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    f = open('D:/File/毕业论文/DATA/数据处理/eclat.json', 'r')
    eclat = json.load(f)
    f.close()

    f = open('D:/File/毕业论文/DATA/数据处理/frequent_{}.json'.format(level), 'r')
    fre = json.load(f)
    f.close()

    f = open('D:/File/毕业论文/DATA/数据处理/frequent_2.json', 'r')
    fre2 = json.load(f)
    f.close()

    ind_num = len(data_copp)
    pos1 = int(prepare['loc_set'][level-2][:prepare['loc_set'][level-2].rfind('_')])
    pos2 = int(prepare['loc_set'][level-1][:prepare['loc_set'][level-1].rfind('_')])

    for i in data_copp:
        # point[i[3]] = [[i[pos1], i[pos2]], '-1', 0, -1]  # 坐标位置，颜色，是否变大，是否高亮
        point[i[3]] = [[i[pos1], i[pos2]], -1, -1, 0]  # 坐标位置，颜色，是否高亮，形状            

    for i in fre:
        for j in i[0]:
            point[data_copp[j][3]][1] = int(i[2][-1])

    for i in range(level):
        if i == 0:
            comm_set = list(eclat[prepare['loc_set'][i]])
            loc_len = len(comm_set)
            circul[0] = round(loc_len/ind_num, 4)
        else:
            comm_set = list(set(comm_set) & set(eclat[prepare['loc_set'][i]]))
            circul[2].append(round(len(comm_set)/loc_len, 4))

    temp_set = list(set(eclat[prepare['loc_set'][level-2]]) & set(eclat[prepare['loc_set'][level-1]]))
    if len(temp_set) == 0:
        circul[1] = 0
    else:
        circul[1] = round(len(comm_set)/len(temp_set), 4)

    circul[3] = [prepare['loc_set'][level-2], prepare['loc_set'][level-1]]
    
    # for i in comm_set:
    #     point[data_copp[i][3]][2] = 1
    
    length = len(fre2)
    for i in range(length):
        for j in fre2[i][0]:
            point[data_copp[j][3]][2] = i

    point[prepare['copp']][3] = 1

    f = open('D:/File/毕业论文/DATA/数据处理/point_{}.json'.format(level), 'w')
    json.dump(point, f, ensure_ascii=False, indent=2)
    f.close()   # 全量散点分布

    # f = open('D:/File/毕业论文/DATA/数据处理/circul_{}.json'.format(level), 'w')
    # json.dump(circul, f, ensure_ascii=False, indent=2)
    # f.close()   # 目标散点分布


if __name__ == "__main__":
    point(6)
