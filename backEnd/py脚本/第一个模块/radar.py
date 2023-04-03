import json


def k_means(dic):
    res = {}

    for q in dic:
        cent = []
        cent_temp = []
        clus = []
        # dic[q].sort()
        temp = []
        for p in range(5):
            cent.append(dic[q][p])
            cent_temp.append(0)
        length = len(dic[q])
        for p in range(length):
            clus.append(-1)

        thre = 100
        while thre > 0:
            for i in range(5):
                cent_temp[i] = cent[i]
            # print(cent_temp)
            j = 0
            for i in range(length):
                clus[i] = j
                gap = abs(dic[q][i] - cent[j])
                while j < 4:
                    if abs(dic[q][i] - cent[j+1]) < gap:
                        j += 1
                        gap = abs(dic[q][i] - cent[j])
                        clus[i] = j
                    else:
                        break
            sum = 0
            j = 0
            t = 0
            for i in range(length-1):
                sum += dic[q][i]
                t += 1
                if clus[i+1] != clus[i]:
                    cent[j] = sum/t
                    j += 1
                    sum = 0
                    t = 0
            sum += dic[q][i+1]
            t += 1
            cent[j] = sum/t
            thre = 0
            for i in range(5):
                thre += (cent[i] - cent_temp[i])**2

        res[q] = [[], []]
        temp.append(dic[q][0])
        for i in range(1, length):
            if clus[i] != clus[i-1]:
                res[q][0].append([min(temp), max(temp)+0.01])
                res[q][1].append(round(len(temp)/length, 4))
                temp = [dic[q][i]]
            else:
                temp.append(dic[q][i])
        res[q][0].append([min(temp), max(temp)+0.01])
        res[q][1].append(round(len(temp)/length, 4))
    return res


def radar(copp):
    print('rader')
    radar_temp = {}
    radar_detail = {}
    radar_axis = {
                'ldbl': [],
                'sdbl': [],
                'xjbl': [],
                'zcfzl': [],
                'xyzqybl': [],
                'cqbl': [],
                'ldzczzl': [],
                'ldzclrl': [],
                'gdzczzl': [],
                'gdzclrl': [],
                'zzczzl': [],
                'zzclrl': [],
                'yymll': [],
                'jlrl': [],
                'yylrl': [],
                'cbfylrl': [],
                'zzcbcl': [],
                'zfzbcl': []
                }
    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/radar.json', 'r', encoding='gbk')
    radar = json.load(f)
    f.close()

    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/corr_detail.json', 'r')
    corr_detail = json.load(f)
    f.close()

    ind = corr_detail[copp][2]

    for i in radar:
        if i['INDUSTRY_NAME'] == ind:
            radar_temp[i['SECURITY_NAME_ABBR']] = i
            for j in radar_axis.keys():
                if i[j] != '':
                    radar_axis[j].append(float(i[j]))
                    radar_axis[j].sort()
    for i in corr_detail.keys():
        radar_detail[i] = [float(radar_temp[i]['ldbl']),
                           float(radar_temp[i]['sdbl']),
                           float(radar_temp[i]['xjbl']),
                           float(radar_temp[i]['zcfzl']),
                           float(radar_temp[i]['xyzqybl']),
                           float(radar_temp[i]['cqbl']),
                           float(radar_temp[i]['ldzczzl']),
                           float(radar_temp[i]['ldzclrl']),
                           float(radar_temp[i]['gdzczzl']),
                           float(radar_temp[i]['gdzclrl']),
                           float(radar_temp[i]['zzczzl']),
                           float(radar_temp[i]['zzclrl']),
                           float(radar_temp[i]['yymll']),
                           float(radar_temp[i]['jlrl']),
                           float(radar_temp[i]['yylrl']),
                           float(radar_temp[i]['cbfylrl']),
                           float(radar_temp[i]['zzcbcl']),
                           float(radar_temp[i]['zfzbcl'])
                           ]

    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/radar_axis.json', 'w')
    json.dump(radar_axis, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/radar_detail.json', 'w')
    json.dump(radar_detail, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/GitHub/YbcCompletionProject/backEnd/data/bord.json', 'w')
    json.dump(k_means(radar_axis), f, ensure_ascii=False, indent=2)
    f.close()


if __name__ == "__main__":
    radar('科大讯飞')
