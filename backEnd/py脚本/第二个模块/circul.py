import json


def circul(level):
    if level <= 1:
        return 0

    circul_d = {}
    circul = {}
    ring = []

    f = open('D:/File/毕业论文/DATA/数据处理/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    f = open('D:/File/毕业论文/DATA/数据处理/eclat.json', 'r')
    eclat = json.load(f)
    f.close()

    length = len(eclat[prepare['loc_set'][0]])
    circul_l = length/prepare['length']
    pos = prepare['loc_set'][level-1][:prepare['loc_set'][level-1].rfind('_')]

    for i in range(level - 1):
        if i == 0:
            comm_set = list(eclat[prepare['loc_set'][i]])
        else:
            comm_set = list(set(comm_set) & set(eclat[prepare['loc_set'][i]])) 
            ring.append(len(comm_set)/length)
    ring.append(-1)

    for i in range(prepare['k']):
        circul_d[pos+'_'+str(i)] = [circul_l]  # 左半圆
        temp1 = list(set(eclat[pos+'_'+str(i)]) & set(comm_set))  # XYZ
        temp2 = list(set(eclat[pos+'_'+str(i)]) & set(eclat[prepare['loc_set'][level - 2]]))  # YZ
        if temp2 == []:
            circul_r = 0
        else:
            circul_r = len(temp1)/len(temp2)
        circul_d[pos+'_'+str(i)].append(circul_r)  # 右半圆
        ring[-1] = len(temp1)/length  # 圆环
        circul_d[pos+'_'+str(i)] = circul_d[pos+'_'+str(i)] + ring
    circul[prepare['loc_set'][level-2]] = circul_d

    f = open('D:/File/毕业论文/DATA/数据处理/circul_{}.json'.format(level), 'w')
    json.dump(circul, f, ensure_ascii=False, indent=2)
    f.close()   # 目标散点分布


if __name__ == "__main__":
    circul(2)