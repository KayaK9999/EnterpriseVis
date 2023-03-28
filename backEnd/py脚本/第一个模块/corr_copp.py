import json
import csv


def corr_copp(copp):
    print('corr_copp1')
    data_copp = {}
    corr_copp = {'zcfz': ['', ''], 'yysz': ['', ''], 'xjll': ['', '']}
    detail = {}
    para_detail = {}
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/result_detail.csv', 'r' , encoding='gbk')
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        data_copp[line[3]] = line
        para_detail[line[3]] = [line[4], line[9], line[21], line[16], line[25], line[28], line[31]]
    f.close()

    detail[copp] = list(data_copp[copp])
    data_copp.pop(copp)
    for i in data_copp.keys():
        if corr_copp['zcfz'][0] == '':
            corr_copp['zcfz'][0] = i
            corr_copp['yysz'][0] = i
            corr_copp['xjll'][0] = i
            dis1_1 = ((float(data_copp[i][4]) - float(detail[copp][4]))**2 + (float(data_copp[i][9]) - float(detail[copp][9]))**2)**0.5
            dis2_1 = ((float(data_copp[i][16]) - float(detail[copp][16]))**2 + (float(data_copp[i][21]) - float(detail[copp][21]))**2 + (float(data_copp[i][23]) - float(detail[copp][23]))**2)**0.5
            dis3_1 = ((float(data_copp[i][25]) - float(detail[copp][25]))**2 + (float(data_copp[i][28]) - float(detail[copp][28]))**2 + (float(data_copp[i][31]) - float(detail[copp][31]))**2)**0.5
        elif corr_copp['zcfz'][1] == '':
            dis1_2 = ((float(data_copp[i][4]) - float(detail[copp][4]))**2 + (float(data_copp[i][9]) - float(detail[copp][9]))**2)**0.5
            dis2_2 = ((float(data_copp[i][16]) - float(detail[copp][16]))**2 + (float(data_copp[i][21]) - float(detail[copp][21]))**2 + (float(data_copp[i][23]) - float(detail[copp][23]))**2)**0.5
            dis3_2 = ((float(data_copp[i][25]) - float(detail[copp][25]))**2 + (float(data_copp[i][28]) - float(detail[copp][28]))**2 + (float(data_copp[i][31]) - float(detail[copp][31]))**2)**0.5
            if dis1_2 < dis1_1:
                corr_copp['zcfz'][1] = corr_copp['zcfz'][0]
                corr_copp['zcfz'][0] = i
                temp = dis1_1
                dis1_1 = dis1_2
                dis1_2 = temp
            else:
                corr_copp['zcfz'][1] = i
            if dis2_2 < dis2_1:
                corr_copp['yysz'][1] = corr_copp['yysz'][0]
                corr_copp['yysz'][0] = i
                temp = dis2_1
                dis2_1 = dis2_2
                dis2_2 = temp
            else:
                corr_copp['zcfz'][1] = i
            if dis3_2 < dis3_1:
                corr_copp['xjll'][1] = corr_copp['xjll'][0]
                corr_copp['xjll'][0] = i
                temp = dis3_1
                dis3_1 = dis3_2
                dis3_2 = temp
            else:
                corr_copp['xjll'][1] = i
        else:
            dis1_temp = ((float(data_copp[i][4]) - float(detail[copp][4]))**2 + (float(data_copp[i][9]) - float(detail[copp][9]))**2)**0.5
            dis2_temp = ((float(data_copp[i][16]) - float(detail[copp][16]))**2 + (float(data_copp[i][21]) - float(detail[copp][21]))**2 + (float(data_copp[i][23]) - float(detail[copp][23]))**2)**0.5
            dis3_temp = ((float(data_copp[i][25]) - float(detail[copp][25]))**2 + (float(data_copp[i][28]) - float(detail[copp][28]))**2 + (float(data_copp[i][31]) - float(detail[copp][31]))**2)**0.5
            if dis1_temp < dis1_1:
                corr_copp['zcfz'][1] = corr_copp['zcfz'][0]
                corr_copp['zcfz'][0] = i
                dis1_2 = dis1_1
                dis1_1 = dis1_temp
            elif dis1_temp < dis1_2:
                corr_copp['zcfz'][1] = i
                dis1_2 = dis1_temp
            if dis2_temp < dis2_1:
                corr_copp['yysz'][1] = corr_copp['yysz'][0]
                corr_copp['yysz'][0] = i
                dis2_2 = dis2_1
                dis2_1 = dis2_temp
            elif dis2_temp < dis2_2:
                corr_copp['yysz'][1] = i
                dis2_2 = dis2_temp
            if dis3_temp < dis3_1:
                corr_copp['xjll'][1] = corr_copp['xjll'][0]
                corr_copp['xjll'][0] = i
                dis3_2 = dis3_1
                dis3_1 = dis3_temp
            elif dis3_temp < dis3_2:
                corr_copp['xjll'][1] = i
                dis3_2 = dis3_temp
    for i in corr_copp:
        for j in corr_copp[i]:
            detail[j] = list(data_copp[j])

    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/corr_copp.json', 'w')
    json.dump(corr_copp, f, ensure_ascii=False, indent=2)
    f.close()
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/corr_detail.json', 'w')
    json.dump(detail, f, ensure_ascii=False, indent=2)
    f.close()
    f = open('/Users/younggaming/Documents/pyCharm/ybcProject/data/para_detail.json', 'w')
    json.dump(para_detail, f, ensure_ascii=False, indent=2)
    f.close()


if __name__ == "__main__":
    corr_copp('日上集团')