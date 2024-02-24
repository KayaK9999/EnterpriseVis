import json

from flask import Flask, request
from flask_cors import *

from py脚本.第一个模块.k_means import k_means
from py脚本.第一个模块.corr_copp import corr_copp
from py脚本.第一个模块.axis import axis as axis1
from py脚本.第一个模块.rose import rose
from py脚本.第一个模块.radar import radar

from py脚本.第二个模块.axis import axis as axis2
from py脚本.第二个模块.circul import circul
from py脚本.第二个模块.eclat import eclat
from py脚本.第二个模块.eclat_cluster import eclat_cluster
from py脚本.第二个模块.point import point

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
    axis1(int(s2))
    rose()
    radar(s1)
    eclat(s1, 5)
    axis2(5)
    return "page1"

# page2里点选按钮
@app.route('/tree', methods=['post', 'get'])
def tree():
    data = request.json
    s1 = data['idx']
    s2 = data['level']
    eclat_cluster(s1, s2)
    point(s2)
    circul(s2)
    return 'page2'


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
    eclat_cluster('10_0', 1)
    point(6)
    circul(6)
    return 'hello'

if __name__ == '__main__':
    app.run()
