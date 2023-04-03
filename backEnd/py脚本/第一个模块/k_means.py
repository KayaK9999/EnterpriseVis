import csv
import json


def k_means_line(data, k, cop_clus, loc_i):
    clus = []
    cent = []
    cent_temp = []
    data_temp = []
    corp = []
    clus = []
    for i in data:
        if float(i[loc_i]) != 0:
            corp.append(i[3])
            data_temp.append(float(i[loc_i]))

    length = len(data_temp)
    if length == 0:
        return
    for i in range(length):
        clus.append(-1)
        min = data_temp[i]
        flag = i
        for j in range(i+1, length):
            if data_temp[j] < min:
                min = data_temp[j]
                flag = j
        data_temp[flag] = data_temp[i]
        data_temp[i] = min
        corp_temp = corp[flag]
        corp[flag] = corp[i]
        corp[i] = corp_temp

    j = int(length/(k+1))
    for i in range(1, k+1):
        cent.append(data_temp[j*i])
        cent_temp.append(0)
    thre = 100
    while thre > 1:
        for i in range(k):
            cent_temp[i] = cent[i]
        # print(cent_temp)
        j = 0
        for i in range(length):
            clus[i] = j
            gap = abs(data_temp[i] - cent[j])
            while j < k-1:
                if abs(data_temp[i] - cent[j+1]) < gap:
                    j += 1
                    gap = abs(data_temp[i] - cent[j])
                    clus[i] = j
                else:
                    break
        sum = 0
        j = 0
        t = 0
        for i in range(length-1):
            sum += data_temp[i]
            t += 1
            if clus[i+1] != clus[i]:
                cent[j] = int(sum/t)
                j += 1
                sum = 0
                t = 0
        sum += data_temp[i+1]
        t += 1
        cent[j] = int(sum/t)
        thre = 0
        for i in range(k):
            thre += (cent[i] - cent_temp[i])**2
    for i in range(length):
        cop_clus['%s' % corp[i]].append(str(loc_i) + '_' + str(clus[i]))


def k_means(copp, k):
    print('k_means')
    data = []
    data_ind = []
    cop_clus = {}
    prepare = {}

    f_in = '/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/cwkb20211231.csv'
    f_out_detail = '/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/result_detail.csv'
    f_out_kind = '/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/result_kind.csv'

    with open(f_in, 'r', encoding='gbk') as file:
        reader = csv.reader(file)
        # lable = next(reader)
        header_row = next(reader)
        for line in reader:
            if line[3] == copp:
                ind = line[2]
            data.append(line)

    for i in data:
        if i[2] == ind:
            cop_clus['%s' % i[3]] = [i[3]]
            data_ind.append(i)

    file = open(f_out_detail, 'w', encoding='gbk', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(header_row)
    for i in data_ind:
        csv_writer.writerow(i)
    file.close()

    for i in range(4, 32):
        if i == 13 or i == 11:
            continue
        k_means_line(data_ind, k, cop_clus, i)

    file = open(f_out_kind, 'w', encoding='gbk', newline='')
    csv_writer = csv.writer(file)
    for i in cop_clus.keys():
        csv_writer.writerow(cop_clus[i])
    file.close()

    prepare['copp'] = copp
    prepare['ind'] = ind
    prepare['k'] = k
    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/prepare.json', 'w')
    json.dump(prepare, f, ensure_ascii=False, indent=2)
    f.close()


if __name__ == "__main__":
    k_means('ST国华', 5)
