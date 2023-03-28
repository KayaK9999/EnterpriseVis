import json


def ring(ind_dt):
    ring = {}

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/prepare.json', 'r')
    prepare = json.load(f)
    k = prepare['k']
    f.close()

    for q in ind_dt:
        cent = []
        cent_temp = []
        clus = []
        ind_dt[q].sort()
        temp = []
        for p in range(k):
            cent.append(ind_dt[q][p])
            cent_temp.append(0)
        length = len(ind_dt[q])
        for p in range(length):
            clus.append(-1)

        thre = 100
        while thre > 1:
            for i in range(k):
                cent_temp[i] = cent[i]
            # print(cent_temp)
            j = 0
            for i in range(length):
                clus[i] = j
                gap = abs(ind_dt[q][i] - cent[j])
                while j < k-1:
                    if abs(ind_dt[q][i] - cent[j+1]) < gap:
                        j += 1
                        gap = abs(ind_dt[q][i] - cent[j])
                        clus[i] = j
                    else:
                        break
            sum = 0
            j = 0
            t = 0
            for i in range(length-1):
                sum += ind_dt[q][i]
                t += 1
                if clus[i+1] != clus[i]:
                    cent[j] = int(sum/t)
                    j += 1
                    sum = 0
                    t = 0
            sum += ind_dt[q][i+1]
            t += 1
            cent[j] = int(sum/t)
            thre = 0
            for i in range(k):
                thre += (cent[i] - cent_temp[i])**2

        ring[q[:q.rfind('_')]] = []
        temp.append(ind_dt[q][0])
        for i in range(1, length):
            if clus[i] != clus[i-1]:
                ring[q[:q.rfind('_')]].append([[min(temp)-1, max(temp)+1], len(temp)])
                temp = [ind_dt[q][i]]
            else:
                temp.append(ind_dt[q][i])
        ring[q[:q.rfind('_')]].append([[min(temp)-1, max(temp)+1], len(temp)])
    return ring


def corr_ind_obj(c_ind, dis):
    print('corr_ind_obj')
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_dt.json', 'r')  # 折线图数据
    ind_dt = json.load(f)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_ratio.json', 'r')  # 折线图数据
    ind_ratio = json.load(f)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_line.json', 'r')  # 折线图标签
    ind_line = json.load(f)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    ind_ratio_obj = {prepare['ind']: ind_ratio[prepare['ind']][-12:], c_ind: ind_ratio[c_ind][dis-12:]}
    ind_line_obj = {prepare['ind']: ind_line[prepare['ind']][-12:], c_ind: ind_line[c_ind][dis-12:]}

    temp1 = {}
    temp2 = {}
    dt = ['2018/3/31', '2018/6/30', '2018/9/30', '2018/12/31',
          '2019/3/31', '2019/6/30', '2019/9/30', '2019/12/31',
          '2020/3/31', '2020/6/30', '2020/9/30', '2020/12/31',
          '2021/3/31', '2021/6/30', '2021/9/30', '2021/12/31']
    for i in ind_dt:
        report_dt = i[:i.rfind('_')]
        ind_name = i[i.rfind('_')+1:]
        if ind_name == prepare['ind'] and report_dt in dt[4:]:
            temp1[i] = ind_dt[i]
        if ind_name == c_ind and report_dt in dt[dis+4:]:
            temp2[i] = ind_dt[i]
    ring_obj = {prepare['ind']: ring(temp1), c_ind: ring(temp2)}

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_ratio_obj.json', 'w')
    json.dump(ind_ratio_obj, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_line_obj.json', 'w')
    json.dump(ind_line_obj, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ring_obj.json', 'w')
    json.dump(ring_obj, f, ensure_ascii=False, indent=2)
    f.close()   # 目标散点分布


if __name__ == "__main__":
    corr_ind_obj('工程建设', -4)
