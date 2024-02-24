<template>
  <div class="container">
    <!--左侧-->
    <div class="panel">
      <!--左上-->
      <div class="search">
        <input class="searchCop" v-model.trim="copName" placeholder="请输入公司名称">
        <select class="searchK" v-model="k">
          <option value="">请选择类群个数</option>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
        </select>
<!--        <input class="searchK" v-model.trim="k" placeholder="请输入类群个数">-->
        <button class="searchBtn" @click="search">搜索</button>
      </div>
      <!--左中-->
      <div class="corCopInfo marginSub">
        <div class="corCopDiv">资产负债：
          <button class="corCopBtn" @click="updateTable(1)">{{corCopName[0]}}</button>
          <button class="corCopBtn" @click="updateTable(2)">{{corCopName[1]}}</button>
        </div>
        <div class="corCopDiv">营业收入：
          <button class="corCopBtn" @click="updateTable(3)">{{corCopName[2]}}</button>
          <button class="corCopBtn" @click="updateTable(4)">{{corCopName[3]}}</button>
        </div>
        <div class="corCopDiv">现金流量：
          <button class="corCopBtn" @click="updateTable(5)">{{corCopName[4]}}</button>
          <button class="corCopBtn" @click="updateTable(6)">{{corCopName[5]}}</button>
        </div>
      </div>
      <!--左下-->
      <div class="copInfo marginSub">
        <Table :fields="corTableTitle" :rows="corTableValue" :mulSelect="mulSelect" />
      </div>
    </div>
    <!--中间-->
    <div class="view1 margin">
      <!--中上-->
      <div class="btn">
        <div class="btnSub" v-for="(name, index) in btnTitle" :key="index">
          <button class="btnSubSub" @click="updateChart1(index)">{{name[0]}}</button>
          <input type="radio" v-show="name[1]" :name="name[0]" @click="updateChart2(index, 1)">{{name[1]}}
          <input type="radio" v-show="name[2]" :name="name[0]" @click="updateChart2(index, 2)">{{name[2]}}
        </div>
      </div>
      <!--中中-->
      <div class="view1_1 marginSub">
        <view1 :mainNum="mainNum" :corCop="corCop" :k="k" :key="view1Component"></view1>
      </div>
      <!--中下-->
      <div class="view1_2 marginSub">
        <view2 :subNum="subNum" :corCop="corCop" :key="view2Component"></view2>
      </div>
    </div>
    <!--右侧-->
    <div class="view2 margin">
      <view3 :corCop="corCop" :key="view3Component"></view3>
    </div>
  </div>
</template>

<script>
import view2 from '@/components/view12.vue'
import view1 from '@/components/view11.vue'
import Table from '@/components/table.vue'
import view3 from '@/components/view2.vue'
import axios from 'axios'
import corrCoppJson from '../../../backEnd/data/corr_copp.json'
import corrDetail from '../../../backEnd/data/corr_detail.json'
export default {
  name: 'page_1',
  data () {
    return {
      copName: '',
      k: 5,
      corCopName: ['', '', '', '', '', ''], // 左中对比公司
      corTableTitle: [{ name: '公司细节' }, { name: '目标公司' }, { name: '对比公司' }], // 左下表头
      corTableValue: [{ 公司细节: '报告期', 目标公司: '2021/12/31', 对比公司: '2021/12/31' },
        { 公司细节: '公司代码', 目标公司: '000004.SZ', 对比公司: '603138.SH' },
        { 公司细节: '行业', 目标公司: '软件开发', 对比公司: '软件开发' },
        { 公司细节: '公司名称', 目标公司: 'ST国华', 对比公司: '海量数据' },
        { 公司细节: '总资产', 目标公司: '11.11', 对比公司: '10.94' },
        { 公司细节: '固定资产', 目标公司: '244.70', 对比公司: '754.62' },
        { 公司细节: '货币资金', 目标公司: '16944.81', 对比公司: '85931.06' },
        { 公司细节: '应收账款', 目标公司: '37060.24', 对比公司: '12392.32' },
        { 公司细节: '存贷', 目标公司: '2060.42', 对比公司: '2076.92' },
        { 公司细节: '总负债', 目标公司: '1.62', 对比公司: '1.70' },
        { 公司细节: '应付账款', 目标公司: '5499.80', 对比公司: '3429.63' },
        { 公司细节: '预收账款', 目标公司: '0.00', 对比公司: '0.00' },
        { 公司细节: '股东权益合计', 目标公司: '9.48', 对比公司: '9.24' },
        { 公司细节: '负债资产率', 目标公司: '14.62', 对比公司: '15.53' },
        { 公司细节: '净利润', 目标公司: '-50910.73', 对比公司: '1127.33' },
        { 公司细节: '扣非归母净利润', 目标公司: '-52120.33', 对比公司: '635.03' },
        { 公司细节: '营业总收入', 目标公司: '28894.42', 对比公司: '42061.37' },
        { 公司细节: '营业支出', 目标公司: '12693.63', 对比公司: '27187.44' },
        { 公司细节: '销售费用', 目标公司: '3428.21', 对比公司: '4920.40' },
        { 公司细节: '管理费用', 目标公司: '2028.46', 对比公司: '2862.53' },
        { 公司细节: '财务费用', 目标公司: '-203.13', 对比公司: '-715.14' },
        { 公司细节: '营业总支出', 目标公司: '21504.33', 对比公司: '41793.55' },
        { 公司细节: '营业利润', 目标公司: '-49999.09', 对比公司: '745.79' },
        { 公司细节: '利润总额', 目标公司: '-50219.47', 对比公司: '759.76' },
        { 公司细节: '净现金流', 目标公司: '-1571.77', 对比公司: '39986.69' },
        { 公司细节: '经营性现金流净值', 目标公司: '310.15', 对比公司: '-1792.19' },
        { 公司细节: '商品劳务收入', 目标公司: '32362.67', 对比公司: '36136.55' },
        { 公司细节: '职工现金支出', 目标公司: '7365.94', 对比公司: '10768.79' },
        { 公司细节: '投资性现金流净值', 目标公司: '-1080.70', 对比公司: '-99.50' },
        { 公司细节: '投资收益现金', 目标公司: '63.37', 对比公司: '350.71' },
        { 公司细节: '长期资产支付现金', 目标公司: '135.63', 对比公司: '455.25' },
        { 公司细节: '融资性现金流净值', 目标公司: '-801.22', 对比公司: '41878.49' }
      ], // 左下表数据
      btnTitle: [
        ['总资产', '固定资产', '流动资产'],
        ['总负债', '应付账款', '预收账款'],
        ['营业总支出', '营业支出', '各项费用'],
        ['营业总收入', '营业时间', '净利润'],
        ['经营现金流', '经营收入', '职工支出'],
        ['投资现金流', '投资收益', '长期投资'],
        ['融资现金流', '', '']
      ], // 中上按钮名字
      mainNum: 0, // 中上按钮主指标
      subNum: [0, 0, 0, 0, 0, 0, 0], // 中上按钮子指标，0/1/2分别为未点击，第一个，第二个子指标
      corCop: 4, // 用户选择的子公司
      view1Component: 0,
      view2Component: 0,
      view3Component: 0
    }
  },
  components: {
    view1,
    Table,
    view2,
    view3
  },
  methods: {
    // 搜索公司和K
    search () {
      const data = {
        copName: this.copName,
        k: this.k
      }
      axios.post('http://127.0.0.1:5000/searchCop', data).then((res) => {
        const keys = Object.keys(corrCoppJson)
        for (let i = 0; i < 3; i++) {
          for (let j = 0; j < 2; j++) {
            this.corCopName[i * 2 + j] = corrCoppJson[keys[i]][j]
            this.corCopName.slice(i * 2 + j, 1, corrCoppJson[keys[i]][j])
          }
        }
        this.updateTable(1)
      }).catch((error) => {
        console.log(error)
      })
    },
    forceRerender1 () {
      this.view1Component += 1
    },
    forceRerender2 () {
      this.view2Component += 1
    },
    forceRerender3 () {
      this.view3Component += 1
    },
    updateTable (index) {
      this.corCop = index
      this.forceRerender1()
      this.forceRerender2()
      this.forceRerender3()
      const keys = Object.keys(corrDetail)
      for (let i = 1; i < 32; i++) {
        this.corTableValue[i].目标公司 = corrDetail[keys[0]][i]
      }
      for (let i = 1; i < 32; i++) {
        this.corTableValue[i].对比公司 = corrDetail[keys[index]][i]
      }
    },
    updateChart1 (index) {
      this.mainNum = index
      this.forceRerender1()
    },
    updateChart2 (index, i) {
      this.subNum[index] = i
      this.forceRerender2()
    }
  },
  mounted () {
    const keys = Object.keys(corrCoppJson)
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 2; j++) {
        this.corCopName[i * 2 + j] = corrCoppJson[keys[i]][j]
        this.corCopName.slice(i * 2 + j, 1, corrCoppJson[keys[i]][j])
      }
    }
    this.updateTable(1)
  }
}
</script>

<style scoped>

.container {
  width: 100%;
  height: 900px;
  display: flex;
  /*border: 2px solid black;*/
}

.margin {
   margin-left: 2%;
 }

.panel {
  width: 20%;
  height: 100%;
  /*border: 2px solid yellow;*/
}

.view1 {
  width: 58%;
  height: 100%;
  /*border: 2px solid red;*/
}

.view2 {
  width: 18%;
  height: 100%;
  /*border: 2px solid green;*/
}

.marginSub {
  margin-top: 4%;
}

.search {
  width: 100%;
  height: 4%;
  display: flex;
  /*border: 2px solid brown;*/
}

.searchCop {
  width: 35%;
}

.searchK {
  width: 35%;
  margin-left: 5%;
}

.searchBtn {
  width: 20%;
  margin-left: 5%;
  background: #366AB9;
  color: white;
  font-size: 18px;
}

.corCopInfo {
  width: 100%;
  height: 15%;
  /*border: 2px solid darkgoldenrod;*/
}

.corCopDiv {
  /*text-align: left;*/
  margin-bottom: 10px;
  /*font-size: 10px;*/
  display: flex;
}

.corCopBtn {
  width: 35%;
  height: 30px;
  margin-left: 15px;
  background: #366AB9;
  color: white;
  font-size: 18px;
}

.copInfo {
  width: 100%;
  height: 77%;
  /*border: 2px solid darkorange;*/
}

.btn {
  width: 100%;
  height: 10%;
  display: flex;
  /*border: 2px solid darkred;*/
}

.btnSub {
  width: 10%;
  margin-right: 5%;
  /*border: 2px solid darkred;*/
}

.btnSubSub {
  width: 100%;
  font-size: 16px;
  margin-bottom: 5%;
  background: #366AB9;
  color: white;
}

.view1_1 {
  width: 100%;
  height: 60%;
  /*border: 2px solid darkmagenta;*/
}

.view1_2 {
  width: 100%;
  height: 20%;
  /*border: 2px solid darksalmon;*/
}
</style>
