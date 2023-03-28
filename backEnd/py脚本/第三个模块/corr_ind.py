import json
import csv
import pandas as pd


def corr_ind_1(quota):
    dt = {'2018/3/31': 0, '2018/6/30': 1, '2018/9/30': 2, '2018/12/31': 3,
          '2019/3/31': 4, '2019/6/30': 5, '2019/9/30': 6, '2019/12/31': 7,
          '2020/3/31': 8, '2020/6/30': 9, '2020/9/30': 10, '2020/12/31': 11,
          '2021/3/31': 12, '2021/6/30': 13, '2021/9/30': 14, '2021/12/31': 15}
    data = {}
    ind = {}
    ind_line = {}
    ind_ratio = {}
    corr_ind = {}
    corr_ind_temp = {}
    quota_di = {'总资产': 6, '总负债': 15}

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    ind_copp = {prepare['copp']: {}}

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/zcfzb.csv', 'r', encoding='gbk')
    reader = csv.reader(f)
    next(reader)
    next(reader)
    for line in reader:
        if line[5][:4] > '2017' and line[quota_di[quota]] != '0':
            if data.get(line[5]+'_'+line[3], -1) == -1:
                data[line[5]+'_'+line[3]] = [float(line[quota_di[quota]])]
            else:
                data[line[5]+'_'+line[3]].append(float(line[quota_di[quota]]))  # 行业+日期：公司序列
            if line[4] == prepare['copp'] and line[5][:4] > '2018':
                ind_copp[prepare['copp']][line[5]] = [float(line[quota_di[quota]])]  # 目标公司：标签,序列
    f.close()
    dt_temp = ['2019/3/31', '2019/6/30', '2019/9/30', '2019/12/31',
               '2020/3/31', '2020/6/30', '2020/9/30', '2020/12/31',
               '2021/3/31', '2021/6/30', '2021/9/30', '2021/12/31']
    for i in range(12):
        if ind_copp[prepare['copp']].get(dt_temp[i]) is not None:
            base = ind_copp[prepare['copp']][dt_temp[i]][0]
            for j in range(i, 12):
                if ind_copp[prepare['copp']].get(dt_temp[j]) is not None:
                    ratio = round(ind_copp[prepare['copp']][dt_temp[j]][0]/base, 4)
                    ind_copp[prepare['copp']][dt_temp[j]].append(ratio)
            break

    for i in data:
        length = len(data[i])
        sum = 0
        for j in data[i]:
            sum = sum + j/length
        ind[i] = round(sum, 4)  # 行业+日期:指标均值
    for i in ind.keys():
        report_dt = i[:i.rfind('_')]
        ind_name = i[i.rfind('_')+1:]
        if ind_line.get(ind_name, -1) == -1:
            ind_line[ind_name] = []
            for t in range(16):
                ind_line[ind_name].append(0)
        ind_line[ind_name][dt[report_dt]] = ind[i]  # 行业时间序列[2018-2021]
    for i in ind_line:
        ind_ratio[i] = []
        length = len(ind_line[i])
        for j in range(length):
            ind_ratio[i].append(round(ind_line[i][j]/abs(ind_line[i][0]), 4))  # 行业归一化处理[2018-2021]

    A1 = pd.Series(ind_ratio[prepare['ind']][4:])
    for t in range(5):
        corr_ind[str(t-4)] = []
        corr_ind_temp[str(t-4)] = {}
        for i in ind_ratio:
            if i != prepare['ind']:
                B1 = pd.Series(ind_ratio[i][4-t:16-t])
                corr = round(A1.corr(B1, method='spearman'), 4)
                if abs(corr) > 0.8:
                    corr_ind_temp[str(t-4)][i] = corr
    for i in corr_ind_temp:
        temp = sorted(corr_ind_temp[i].items(), key=lambda x: abs(x[-1]), reverse=True)
        if len(temp) == 0:
            corr_ind[i] = ['无：', '无：']
        elif len(temp) == 1:
            str1 = temp[0][0] + ':' + str(round(temp[0][1], 2))
            corr_ind[i] = [str1, '无：']
        else:
            str1 = temp[0][0] + ':' + str(round(temp[0][1], 2))
            str2 = temp[1][0] + ':' + str(round(temp[1][1], 2))
            corr_ind[i] = [str1, str2]

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_dt.json', 'w')
    json.dump(data, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/corr_ind.json', 'w')
    json.dump({prepare['ind']: corr_ind}, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_ratio.json', 'w')
    json.dump(ind_ratio, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_line.json', 'w')
    json.dump(ind_line, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_copp.json', 'w')
    json.dump(ind_copp, f, ensure_ascii=False, indent=2)
    f.close()


def corr_ind_2(quota):
    dt = {'2017/3/31': 0, '2017/6/30': 1, '2017/9/30': 2, '2017/12/31': 3,
          '2018/3/31': 4, '2018/6/30': 5, '2018/9/30': 6, '2018/12/31': 7,
          '2019/3/31': 8, '2019/6/30': 9, '2019/9/30': 10, '2019/12/31': 11,
          '2020/3/31': 12, '2020/6/30': 13, '2020/9/30': 14, '2020/12/31': 15,
          '2021/3/31': 16, '2021/6/30': 17, '2021/9/30': 18, '2021/12/31': 19}
    data = {}
    ind = {}
    ind_line = {}
    ind_ratio = {}
    corr_ind = {}
    corr_ind_temp = {}
    quota_di = {'净利润': 6, '营业总支出': 12, '营业总收入': 10, '经营性现金流': 8, '投资性现金流': 14, '融资性现金流': 20}

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/prepare.json', 'r')
    prepare = json.load(f)
    f.close()

    ind_copp = {prepare['copp']: {}}

    if quota in ('净利润', '营业总支出', '营业总收入'):
        f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/lrb.csv', 'r', encoding='gbk')
    else:
        f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/xjlb.csv', 'r', encoding='gbk')
    reader = csv.reader(f)
    next(reader)
    next(reader)
    for line in reader:
        if line[5][:4] > '2016' and line[quota_di[quota]] != '0':
            if data.get(line[5]+'_'+line[3], -1) == -1:
                data[line[5]+'_'+line[3]] = [float(line[quota_di[quota]])]
            else:
                data[line[5]+'_'+line[3]].append(float(line[quota_di[quota]]))  # 行业+日期：公司序列
            if line[4] == prepare['copp'] and line[5][:4] > '2018':
                ind_copp[prepare['copp']][line[5]] = [float(line[quota_di[quota]]), round(float(line[quota_di[quota] + 1])/100, 4)]
    f.close()
    for i in data:
        length = len(data[i])
        sum = 0
        for j in data[i]:
            sum = sum + j
        ind[i] = round(sum/length, 4)  # 行业+日期:指标均值
    for i in ind.keys():
        report_dt = i[:i.rfind('_')]
        ind_name = i[i.rfind('_')+1:]
        if ind_line.get(ind_name, -1) == -1:
            ind_line[ind_name] = []
            for t in range(20):
                ind_line[ind_name].append(0)
        ind_line[ind_name][dt[report_dt]] = ind[i]  # 行业时间序列[2017-2021]
    for i in ind_line:
        ind_ratio[i] = []
        length = len(ind_line[i])
        for j in range(4, length):
            ind_ratio[i].append(round((ind_line[i][j] - ind_line[i][j-4])/abs(ind_line[i][j-4]), 4))  # 行业同比增长率[2018-2021]

    A1 = pd.Series(ind_ratio[prepare['ind']][4:])
    for t in range(5):
        corr_ind[str(t-4)] = []
        corr_ind_temp[str(t-4)] = {}
        for i in ind_ratio:
            if i != prepare['ind']:
                B1 = pd.Series(ind_ratio[i][4-t:16-t])
                corr = round(A1.corr(B1, method='spearman'), 4)
                if abs(corr) > 0.8:
                    corr_ind_temp[str(t-4)][i] = corr
    for i in corr_ind_temp:
        temp = sorted(corr_ind_temp[i].items(), key=lambda x: abs(x[-1]), reverse=True)
        if len(temp) == 0:
            corr_ind[i] = ['无：', '无：']
        elif len(temp) == 1:
            str1 = temp[0][0] + ':' + str(round(temp[0][1], 2))
            corr_ind[i] = [str1, '无：']
        else:
            str1 = temp[0][0] + ':' + str(round(temp[0][1], 2))
            str2 = temp[1][0] + ':' + str(round(temp[1][1], 2))
            corr_ind[i] = [str1, str2]

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_dt.json', 'w')
    json.dump(data, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/corr_ind.json', 'w', encoding='utf-8')
    json.dump({prepare['ind']: corr_ind}, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_ratio.json', 'w')
    json.dump(ind_ratio, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_line.json', 'w')
    json.dump(ind_line, f, ensure_ascii=False, indent=2)
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/ind_copp.json', 'w')
    json.dump(ind_copp, f, ensure_ascii=False, indent=2)
    f.close()


def corr_ind(quota):
    print('corr_ind')
    if quota in ('总资产', '总负债'):
        corr_ind_1(quota)
    else:
        corr_ind_2(quota)


if __name__ == "__main__":
    corr_ind('总资产')
