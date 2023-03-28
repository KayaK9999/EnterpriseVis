import json
import csv


def rose():
    print('rose')
    data = {}
    rose = {}
    copp = {}
    quata = {}
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/zcfzb.csv', 'r', encoding='gbk')
    reader = csv.reader(f)
    next(reader)
    next(reader)
    for line in reader:
        if line[5][5:10] == '12/31':
            data[line[5][:4]+line[4]] = line
    f.close()

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/corr_detail.json', 'r')
    corr_detail = json.load(f)
    f.close()

    rose['4'] = []
    for j in range(2012, 2022):
        copp[str(j)] = []
        for i in corr_detail.keys():
            if data.get(str(j)+i, -1) != -1:
                quata = {}
                quata['主指标'] = float(data[str(j)+i][6])
                quata['固定资产'] = float(data[str(j)+i][8])
                quata['流动资产'] = float(data[str(j)+i][9])+float(data[str(j)+i][11])+float(data[str(j)+i][13])
            else:
                quata = {}
                quata['主指标'] = 0
                quata['固定资产'] = 0
                quata['流动资产'] = 0
            copp[str(j)].append({i: quata})
        rose['4'].append({str(j): copp[str(j)]})

    rose['9'] = []
    for j in range(2012, 2022):
        copp[str(j)] = []
        for i in corr_detail.keys():
            if data.get(str(j)+i, -1) != -1:
                quata = {}
                quata['主指标'] = float(data[str(j)+i][15])
                quata['应付账款'] = float(data[str(j)+i][17])
                quata['预收账款'] = float(data[str(j)+i][19])
            else:
                quata = {}
                quata['主指标'] = 0
                quata['应付账款'] = 0
                quata['预收账款'] = 0
            copp[str(j)].append({i: quata})
        rose['9'].append({str(j): copp[str(j)]})

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/lrb.csv', 'r', encoding='gbk')
    reader = csv.reader(f)
    next(reader)
    next(reader)
    for line in reader:
        if line[5][5:10] == '12/31':
            data[line[5][:4]+line[4]] = line
    f.close()

    rose['21'] = []
    for j in range(2012, 2022):
        copp[str(j)] = []
        for i in corr_detail.keys():
            if data.get(str(j)+i, -1) != -1:
                quata = {}
                quata['主指标'] = float(data[str(j)+i][17])
                quata['营业支出'] = float(data[str(j)+i][12])
                quata['各项费用'] = float(data[str(j)+i][14])+float(data[str(j)+i][15])+float(data[str(j)+i][16])
            else:
                quata = {}
                quata['主指标'] = 0
                quata['营业支出'] = 0
                quata['各项费用'] = 0
            copp[str(j)].append({i: quata})
        rose['21'].append({str(j): copp[str(j)]})

    rose['16'] = []
    for j in range(2012, 2022):
        copp[str(j)] = []
        for i in corr_detail.keys():
            if data.get(str(j)+i, -1) != -1:
                quata = {}
                quata['主指标'] = float(data[str(j)+i][10])
                quata['营业利润'] = float(data[str(j)+i][19])
                quata['净利润'] = float(data[str(j)+i][6])
            else:
                quata = {}
                quata['主指标'] = 0
                quata['营业利润'] = 0
                quata['净利润'] = 0
            copp[str(j)].append({i: quata})
        rose['16'].append({str(j): copp[str(j)]})

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/xjlb.csv', 'r', encoding='gbk')
    reader = csv.reader(f)
    next(reader)
    next(reader)
    for line in reader:
        if line[5][5:10] == '12/31':
            data[line[5][:4]+line[4]] = line
    f.close()
 
    rose['25'] = []
    for j in range(2012, 2022):
        copp[str(j)] = []
        for i in corr_detail.keys():
            if data.get(str(j)+i, -1) != -1:
                quata = {}
                quata['主指标'] = float(data[str(j)+i][8])
                quata['经营收入'] = float(data[str(j)+i][10])
                quata['支付工资'] = -1*float(data[str(j)+i][12])
            else:
                quata = {}
                quata['主指标'] = 0
                quata['经营收入'] = 0
                quata['支付工资'] = 0
            copp[str(j)].append({i: quata})
        rose['25'].append({str(j): copp[str(j)]})

    rose['28'] = []
    for j in range(2012, 2022):
        copp[str(j)] = []
        for i in corr_detail.keys():
            if data.get(str(j)+i, -1) != -1:
                quata = {}
                quata['主指标'] = float(data[str(j)+i][14])
                quata['投资收益'] = float(data[str(j)+i][16])
                quata['长期资产'] = -1*float(data[str(j)+i][12])
            else:
                quata = {}
                quata['主指标'] = 0
                quata['投资收益'] = 0
                quata['长期资产'] = 0
            copp[str(j)].append({i: quata})
        rose['28'].append({str(j): copp[str(j)]})

    rose['31'] = []
    for j in range(2012, 2022):
        copp[str(j)] = []
        for i in corr_detail.keys():
            if data.get(str(j)+i, -1) != -1:
                quata = {}
                quata['主指标'] = float(data[str(j)+i][20])
                quata['子指标1'] = 0
                quata['子指标2'] = 0
            else:
                quata = {}
                quata['主指标'] = 0
                quata['子指标1'] = 0
                quata['子指标2'] = 0
            copp[str(j)].append({i: quata})
        rose['31'].append({str(j): copp[str(j)]})

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/rose.json', 'w')
    json.dump(rose, f, ensure_ascii=False, indent=2)
    f.close()   # 目标散点分布


if __name__ == "__main__":
    rose()