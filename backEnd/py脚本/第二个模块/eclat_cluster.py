import json


def colour(loc_i, level):

    frequent = []
    pos = loc_i[:loc_i.rfind('_')]

    f = open('D:/File/毕业论文/DATA/数据处理/eclat.json', 'r')
    eclat = json.load(f)
    f.close()

    f = open('D:/File/毕业论文/DATA/数据处理/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    if level == 1:
        for i in range(prepare['k']):
            frequent.append([list(eclat[pos+'_'+str(i)]), 1, pos+'_'+str(i)])
    else:
        f = open('D:/File/毕业论文/DATA/数据处理/frequent_{}.json'.format(level-1), 'r')
        fre = json.load(f)
        f.close()
        for i in fre:
            for j in range(prepare['k']):
                temp = list(set(i[0]) & set(eclat[pos+'_'+str(j)]))
                sup = len(temp)/(len(i[0])/i[1])
                if sup > 1/prepare['k'] and len(temp) >= 3:
                    frequent.append([temp, sup, i[2]])
    f = open('D:/File/毕业论文/DATA/数据处理/frequent_{}.json'.format(level), 'w')
    json.dump(frequent, f, ensure_ascii=False, indent=2)
    f.close() 


def eclat_cluster(loc_i, level):
    colour(loc_i, level)

    comm_set = []
    eclat = {}

    f = open('D:/File/毕业论文/DATA/数据处理/eclat.json', 'r')
    data = json.load(f)
    f.close()

    f = open('D:/File/毕业论文/DATA/数据处理/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    f = open('D:/File/毕业论文/DATA/数据处理/eclat_{}.json'.format(level), 'r')
    data_obj = json.load(f)
    f.close()

    prepare['loc_set'][level - 1] = loc_i
    f = open('D:/File/毕业论文/DATA/数据处理/prepare.json', 'w')
    json.dump(prepare, f, ensure_ascii=False, indent=2)
    f.close()

    if data_obj[loc_i] < 1/prepare['k']:
        return 0

    # data_obj.pop(loc_i)

    for i in range(level):
        if i == 0:
            comm_set = list(data[prepare['loc_set'][i]])
            length = len(comm_set)
        else:
            comm_set = list(set(comm_set) & set(data[prepare['loc_set'][i]]))

    for i in data_obj.keys():
        temp_set = list(set(comm_set) & set(data[i]))
        eclat[i] = len(temp_set)/length
    for i in range(level):
        eclat[prepare['loc_set'][i]] = -1

    f = open('D:/File/毕业论文/DATA/数据处理/eclat_{}.json'.format(level+1), 'w')
    json.dump(eclat, f, ensure_ascii=False, indent=2)
    f.close()   

    return 1


if __name__ == "__main__":
    print(eclat_cluster('21_1', 3))
