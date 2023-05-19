<template>
  <div class="container">
    <div class="basic" v-for="value1 in values" v-bind:key="value1.id">
      <div class="text">{{value1.names}}</div>
      <button class="margin1 btn" :class="value1.eclat1>25 ? 'color1' : 'color0'" v-show=this.showAll[0]&this.isShow(0,value1.idx) @click="clickBtn(1, value1.idx,value1.id)">{{value1.id.slice(-1)}} | {{value1.eclat1}}%</button>
      <button class="margin2 btn" :class="value1.eclat2>25 ? 'color2' : 'color0'" v-show=this.showAll[1]&this.isShow(1,value1.idx) @click="clickBtn(2, value1.idx,value1.id)">{{value1.id.slice(-1)}} | {{value1.eclat2}}%</button>
      <button class="margin2 btn" :class="value1.eclat3>25 ? 'color3' : 'color0'" v-show=this.showAll[2]&this.isShow(2,value1.idx) @click="clickBtn(3, value1.idx,value1.id)">{{value1.id.slice(-1)}} | {{value1.eclat3}}%</button>
      <button class="margin2 btn" :class="value1.eclat4>25 ? 'color4' : 'color0'" v-show=this.showAll[3]&this.isShow(3,value1.idx) @click="clickBtn(4, value1.idx,value1.id)">{{value1.id.slice(-1)}} | {{value1.eclat4}}%</button>
      <button class="margin2 btn" :class="value1.eclat5>25 ? 'color5' : 'color0'" v-show=this.showAll[4]&this.isShow(4,value1.idx) @click="clickBtn(5, value1.idx,value1.id)">{{value1.id.slice(-1)}} | {{value1.eclat5}}%</button>
      <button class="margin2 btn" :class="value1.eclat6>25 ? 'color6' : 'color0'" v-show=this.showAll[5]&this.isShow(5,value1.idx) @click="clickBtn(6, value1.idx,value1.id)">{{value1.id.slice(-1)}} | {{value1.eclat6}}%</button>
    </div>
    <View31></View31>
    <View32></View32>
    <View33></View33>
  </div>
</template>

<script>
import eclat1 from '../../../backEnd/data/eclat_1.json'
import eclat2 from '../../../backEnd/data/eclat_2.json'
import eclat3 from '../../../backEnd/data/eclat_3.json'
import eclat4 from '../../../backEnd/data/eclat_4.json'
import eclat5 from '../../../backEnd/data/eclat_5.json'
import eclat6 from '../../../backEnd/data/eclat_6.json'
import view31 from '@/components/view31.vue'
import view32 from '@/components/view32.vue'
import view33 from '@/components/view33.vue'
import axios from 'axios'
export default {
  name: 'page_2',
  components: {
    view31,
    view32,
    view33
  },
  data () {
    return {
      values: [
        { id: '4_0', idx: '1', names: '总资产', eclat1: 51, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '5_0', idx: '2', names: '固定资产', eclat1: 33, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '6_0', idx: '3', names: '货币资产', eclat1: 66, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '7_1', idx: '4', names: '应收账款', eclat1: 24, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '8_0', idx: '5', names: '存货', eclat1: 54, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '9_0', idx: '6', names: '总负债', eclat1: 51, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '10_0', idx: '7', names: '应付账款', eclat1: 49, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '12_0', idx: '8', names: '股东权益', eclat1: 6, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '14_1', idx: '9', names: '净利润', eclat1: 6, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '15_1', idx: '10', names: '扣非归母利润', eclat1: 48, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '16_0', idx: '11', names: '营业总收入', eclat1: 6, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '17_0', idx: '12', names: '营业支出', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '18_0', idx: '13', names: '销售费用', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '19_0', idx: '14', names: '管理费用', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '20_2', idx: '15', names: '财务费用', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '21_0', idx: '16', names: '营业总支出', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '22_1', idx: '17', names: '营业利润', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '23_1', idx: '18', names: '利润总额', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '24_2', idx: '19', names: '净现金流', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '25_1', idx: '20', names: '经营性现金流', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '26_0', idx: '21', names: '商品劳务收入', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '27_0', idx: '22', names: '职工现金支出', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '28_3', idx: '23', names: '投资性现金流', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '29_0', idx: '24', names: '投资收益现金', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '30_0', idx: '25', names: '购买长期资产', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 },
        { id: '31_2', idx: '26', names: '融资性现金流', eclat1: 32, eclat2: 13, eclat3: 25, eclat4: 54, eclat5: 34, eclat6: 8 }
      ],
      showAll: [1, 0, 0, 0, 0, 0],
      showSin: [-1, -1, -1, -1, -1, -1],
      eclatCount: 6,
      flag: 1
    }
  },
  methods: {
    clickBtn (level, idx, id) {
      this.getValues(level + 1)
      for (let i = this.eclatCount - 1; i >= 0; i--) {
        this.showAll[i] = (level < i) ? 0 : 1
        if (level <= i) this.showSin[i] = -1
        else if (level === i + 1) this.showSin[i] = idx
      }
      const data = {
        idx: id,
        level: level
      }
      axios.post('http://127.0.0.1:5000/tree', data).then((res) => {
        console.log('传输' + id + '成功')
      }).catch((error) => {
        console.log(error)
      })
    },
    isShow (col, idx) {
      for (let i = 0; i < col; i++) {
        if (idx === this.showSin[i]) return 0
      }
      return 1
    },
    // 读取eclat文件中的数据
    getValues (idx) {
      let eclatJson = {}
      let ids = {}
      switch (idx) {
        case 1 :
          eclatJson = eclat1
          ids = Object.keys(eclatJson)
          for (let i = 0; i < this.values.length; i++) {
            // if (this.isShow(idx, i)) break
            this.values[i].id = ids[i]
            this.values[i].eclat1 = Math.round(eclatJson[ids[i]] * 100)
          }
          break
        case 2 : {
          eclatJson = eclat2
          ids = Object.keys(eclatJson)
          for (let i = 0; i < this.values.length; i++) {
            this.values[i].id = ids[i]
            this.values[i].eclat2 = Math.round(eclatJson[ids[i]] * 100)
          }
          break
        }
        case 3 :
          eclatJson = eclat3
          ids = Object.keys(eclatJson)
          for (let i = 0; i < this.values.length; i++) {
            this.values[i].id = ids[i]
            this.values[i].eclat3 = Math.round(eclatJson[ids[i]] * 100)
          }
          break
        case 4 :
          eclatJson = eclat4
          ids = Object.keys(eclatJson)
          for (let i = 0; i < this.values.length; i++) {
            this.values[i].id = ids[i]
            this.values[i].eclat4 = Math.round(eclatJson[ids[i]] * 100)
          }
          break
        case 5 :
          eclatJson = eclat5
          ids = Object.keys(eclatJson)
          for (let i = 0; i < this.values.length; i++) {
            this.values[i].id = ids[i]
            this.values[i].eclat5 = Math.round(eclatJson[ids[i]] * 100)
          }
          break
        case 6 :
          eclatJson = eclat6
          ids = Object.keys(eclatJson)
          for (let i = 0; i < this.values.length; i++) {
            this.values[i].id = ids[i]
            this.values[i].eclat6 = Math.round(eclatJson[ids[i]] * 100)
          }
          break
      }
    }
  },
  mounted () {
    this.getValues(1)
  }
}
</script>

<style scoped>

.container {
  width: 560px;
  height: 800px;
  border: 2px solid black;
}

.basic {
  /*border: 2px solid blue;*/
  width: 1275px;
  height: 25px;
  display: flex;
}

/*据文字左边界*/
.margin1 {
  margin-left: 10px;
}

/*按钮之间边界距离*/
.margin2 {
  margin-left: 15px;
}

.text {
  width: 80px;
  height: 20px;
  border: 1px solid blue;
  border-radius: 4px;
  text-align: center;
  font-size: 10px;
  /*display: table-cell;*/
  /*vertical-align: middle;*/
}

.btn {
  width: 65px;
  height: 24px;
  border-radius: 4px;
  text-align: center;
  /*color: white;*/
  border-color: white;
  font-size: 10px;
}

.color0 {
  background: #D9D9D9;
  pointer-events: none;
}

.color1 {
  background: #9DC3E6;
}

.color2 {
  background: #A9D18E;
}

.color3 {
  background: #F8CBAD;
}

.color4 {
  background: #A9D18E;
}

.color5 {
  background: #F8CBAD;
}

.color6 {
  background: #A9D18E;
}

</style>
