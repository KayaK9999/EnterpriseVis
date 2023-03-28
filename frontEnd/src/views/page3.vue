<template>
  <div class="container1">
    <div class="top">
      <button class="btn" @click="searchClass(0)">总资产</button>
      <button class="btn" @click="searchClass(1)">总负债</button>
      <button class="btn" @click="searchClass(2)">净利润</button>
      <button class="btn" @click="searchClass(3)">营业总支出</button>
      <button class="btn" @click="searchClass(4)">营业总收入</button>
      <button class="btn" @click="searchClass(5)">经营现金流</button>
      <button class="btn" @click="searchClass(6)">投资现金流</button>
      <button class="btn" @click="searchClass(7)">融资现金流</button>
    </div>
    <div class="below">
      <button class="tarInd">{{chartValue.targetInd}}</button>
      <div class="corrBtn" v-for="(p,index) in chartValue.correlation" :key="p">
        <div class="marginDiv">
          <h4 class="text">{{chartValue.idx[index]}}</h4>
          <button class="corr" @click="searchInd(index, 0)">{{p[0]}}</button><br>
          <button class="corr" @click="searchInd(index, 1)">{{p[1]}}</button>
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <view4></view4>
  </div>
</template>

<script>
import view4 from '@/components/view4.vue'
import corrInd from '../../../../pyCharm/ybcProject/data/corr_ind.json'
import axios from 'axios'
export default {
  name: 'page_3',
  components: {
    view4
  },
  data () {
    return {
      chartValue: {
        indicator: ['总资产', '总负债', '净利润', '营业总支出', '营业总收入', '经营性现金流', '投资性现金流', '融资性现金流'],
        targetInd: '',
        correlation: [['', ''], ['', ''], ['', ''], ['', ''], ['', '']],
        idx: [0, -1, -2, -3, -4],
        correlationName: [['', ''], ['', ''], ['', ''], ['', ''], ['', '']]
      }
    }
  },
  methods: {
    // 按钮数据读取
    getBtnData () {
      const indName = Object.getOwnPropertyNames(corrInd)
      this.chartValue.targetInd = indName[0]
      const keys = Object.keys(corrInd[indName[0]])
      for (let i = 0; i < 5; i++) {
        if (keys[i] === '0') {
          this.chartValue.correlation[0][0] = corrInd[indName[0]][keys[i]][0]
          this.chartValue.correlation[0][1] = corrInd[indName[0]][keys[i]][1]
        } else if (keys[i] === '-1') {
          this.chartValue.correlation[1][0] = corrInd[indName[0]][keys[i]][0]
          this.chartValue.correlation[1][1] = corrInd[indName[0]][keys[i]][1]
        } else if (keys[i] === '-2') {
          this.chartValue.correlation[2][0] = corrInd[indName[0]][keys[i]][0]
          this.chartValue.correlation[2][1] = corrInd[indName[0]][keys[i]][1]
        } else if (keys[i] === '-3') {
          this.chartValue.correlation[3][0] = corrInd[indName[0]][keys[i]][0]
          this.chartValue.correlation[3][1] = corrInd[indName[0]][keys[i]][1]
        } else if (keys[i] === '-4') {
          this.chartValue.correlation[4][0] = corrInd[indName[0]][keys[i]][0]
          this.chartValue.correlation[4][1] = corrInd[indName[0]][keys[i]][1]
        }
      }
    },
    // 读冒号前的字符串
    getCoorelation () {
      for (let i = 0; i < 5; i++) {
        this.chartValue.correlationName[i][0] = this.chartValue.correlation[i][0].split(':')[0]
        this.chartValue.correlationName[i][1] = this.chartValue.correlation[i][1].split(':')[0]
      }
    },
    searchInd (idx, temp) {
      const data = {
        ind: this.chartValue.correlationName[idx][temp],
        temp: this.chartValue.idx[idx]
      }
      axios.post('http://127.0.0.1:5000/searchInd', data).then((res) => {
        this.getBtnData()
        this.getCoorelation()
      }).catch((error) => {
        console.log(error)
      })
    },
    searchClass (idx) {
      const data = {
        indicator: this.chartValue.indicator[idx]
      }
      axios.post('http://127.0.0.1:5000/searchIndicator', data).then((res) => {
        this.getBtnData()
        console.log('成功')
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  mounted () {
    this.getBtnData()
    this.getCoorelation()
  }
}
</script>

<style scoped>

.container1 {
  width: 1700px;
  height: 150px;
  /*border: 2px solid black;*/
}

.top {
  width: 100%;
  height: 20%;
  display: flex;
  /*border: 1px dashed black;*/
}

.btn {
  width: 160px;
  height: 100%;
  background: #9DC3E6;
  margin-left: 40px;
  border-color: white;
  font-size: 16px;
}

.below {
  width: 100%;
  height: 60%;
  display: flex;
  margin-top: 20px;
}

.tarInd {
  width: 80px;
  height: 60%;
  margin-top: 35px;
  background: #366AB9;
  color: white;
  font-size: 16px;
}

.corrBtn {
  width: 15%;
  height: 100%;
  display: flex;
  margin-left: 40px;
  /*border: 1px dashed black;*/
}

.marginDiv {
  margin-left: 1px;
  width: 100%;
}

.text {
  margin-top: 0;
  margin-bottom: 0;
}

.corr {
  margin-top: 10px;
  width: 200px;
  background: #54B435;
  color: white;
  border-color: white;
}

</style>
