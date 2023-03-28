import json

from flask import Flask, request
from flask_cors import *

from py脚本.第一个模块.k_means import k_means
from py脚本.第一个模块.corr_copp import corr_copp
from py脚本.第一个模块.axis import axis
from py脚本.第一个模块.rose import rose
from py脚本.第一个模块.radar import radar

from py脚本.第三个模块.corr_ind import corr_ind
from py脚本.第三个模块.corr_ind_obj import corr_ind_obj


app = Flask(__name__)
CORS(app, supports_credentials=True)

# page1的搜索公司按钮和k分类
@app.route('/searchCop', methods=['POST', 'get'])
def searchCop():  # put application's code here
    data = request.json
    s1 = data['copName']
    s2 = data['k']
    k_means(s1, int(s2))
    corr_copp(s1)
    axis(int(s2))
    rose()
    radar(s1)
    return "hello"

# page3里的不同行业选择
@app.route('/searchInd', methods=['POST', 'get'])
def searchInd():
    data = request.json
    s1 = data['ind']
    s2 = data['temp']
    corr_ind_obj(s1, s2)
    return 'hello'

# page3总资产总负债按钮
@app.route('/searchIndicator', methods=['POST', 'get'])
def searchIndicator():
    data = request.json
    s1 = data['indicator']
    corr_ind(s1)
    return 'hello'

# 测试
@app.route('/')
def test():
    file_name = '/Users/younggaming/Documents/pyCharm/ybcProject/data/prepare.json'
    with open(file_name, 'r') as file:
        load_dict = json.load(file)

    return load_dict['copp']

if __name__ == '__main__':
    app.run()
