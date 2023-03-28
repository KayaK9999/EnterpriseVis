<template>
  <div class="container1" id="view1">
    <svg width="100%" height="100%"></svg>
  </div>
</template>

<script>
import axisJson from '../../../../pyCharm/ybcProject/data/axis.json'
import corrDetailJson from '../../../../pyCharm/ybcProject/data/corr_detail.json'
import paraDetailJson from '../../../../pyCharm/ybcProject/data/para_detail.json'
import * as d3 from 'd3'
export default {
  name: 'view1_1',
  props: {
    mainNum: Number,
    corCop: Number,
    k: Number
  },
  data () {
    return {
      chartConfig: {
        axis: { width: 40, height: 90 },
        axisMargin: { left: 118, top: 10 },
        lineColor: ['#C8C8FF', '#C8FFC8', '#FFC8C8', '#FFFFC8', '#FFC8FF'],
        highLightColor: ['#0000C8', '#00C800', '#C80000', '#C80000', '#C800C8']
        // lineColor: ['#fef0d9', '#fdcc8a', '#fc8d59', '#e34a33', '#b30000']
      },
      chartValue: {
        axisValue: ['4', '9', '16', '21', '25', '28', '31'],
        copData: [4, 9, 16, 21, 25, 28, 31]
      }
    }
  },
  methods: {
    creatPCchart () {
      const that = this
      const main = d3.select('#view1 svg')
        .append('g')
        .classed('main', true)
        // 可以这么写数据，圆中心位置
        .attr('transform', 'translate(' + 50 + ',' + 0 + ')')

      // 画坐标轴
      const axisData = that.getAxisData(axisJson)
      const axiss = main.append('g')
        .classed('axiss', true)
      axiss.selectAll('g')
        .data(axisData.axisPosition)
        .enter()
        .append('g')
        .attr('class', function (d, i) {
          return 'axis' + (i + 1)
        })
      for (let i = 0; i < axisData.axisPosition.length; i++) {
        const axis = axiss.select('.axis' + (i + 1))
        axis.append('rect')
          .attr('x', axisData.axisPosition[i].x)
          .attr('y', axisData.axisPosition[i].y)
          .attr('width', that.chartConfig.axis.width)
          .attr('height', that.chartConfig.axis.height)
          .attr('fill', 'none')
          .attr('stroke-width', 2)
          .attr('stroke', 'black')
      }

      // 画线
      const markData = that.getMarkData(axisData.axissValue, paraDetailJson)
      const lines = main.append('g')
        .classed('lines', true)
      lines.selectAll('g')
        .data(markData.line)
        .enter()
        .append('g')
        .attr('class', function (d, i) {
          return 'line' + (i + 1)
        })
      for (let i = 0; i < markData.line.length; i++) {
        let lineGanerator = lines.select('.line' + (i + 1))
        lineGanerator = d3.line() // .curve(d3.curveCatmullRom)
        const linePath = lineGanerator(markData.line[i].copData)
        main.append('path')
          .attr('d', linePath)
          .attr('fill', 'none')
          .attr('stroke-width', 0.5)
          .attr('stroke', markData.line[i].copColor)
      }
      const lineData = that.getLineData(axisData.axissValue, corrDetailJson)
      const copLine = d3.line() // .curve(d3.curveCatmullRom)
      const copPath = copLine(lineData[0]) // 如果是0的话将来要不改数据传输回来的形式要不前面加判断
      main.append('path')
        .attr('d', copPath)
        .attr('fill', 'none')
        .attr('stroke-width', 4)
        .attr('stroke', '#0081C9')
      const copCorLine = d3.line() // .curve(d3.curveCatmullRom)
      const copCorPath = copCorLine(lineData[that.corCop]) // 如果是0的话将来要不改数据传输回来的形式要不前面加判断
      main.append('path')
        .attr('d', copCorPath)
        .attr('fill', 'none')
        .attr('stroke-width', 4)
        .attr('stroke', '#54B435')
    },

    getMarkData (axis, cop) {
      const keys = Object.keys(cop)
      const data = []
      const mark = []
      for (let i = 0; i < keys.length; i++) {
        const copData = []
        let copColor = ''
        for (let j = 0; j < 7; j++) {
          const key = Object.keys(axis[j])
          for (let k = 0; k < axis[j][key[0]].length; k++) {
            if (Number(cop[keys[i]][j]) <= axis[j][key[0]][k].max && Number(cop[keys[i]][j]) >= axis[j][key[0]][k].min) {
              if (j === this.mainNum) {
                // 改高亮
                if (k === -1) {
                  copColor = this.chartConfig.highLightColor[k]
                } else {
                  copColor = this.chartConfig.lineColor[k]
                }
              }
              copData.push([j * (this.chartConfig.axis.width + this.chartConfig.axisMargin.left), (4 - k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top) + this.chartConfig.axis.height * (axis[j][key[0]][k].max - Number(cop[keys[i]][j])) / (axis[j][key[0]][k].max - axis[j][key[0]][k].min) - (5 - this.k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top)])
              copData.push([j * (this.chartConfig.axis.width + this.chartConfig.axisMargin.left) + this.chartConfig.axis.width, (4 - k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top) + this.chartConfig.axis.height * (axis[j][key[0]][k].max - Number(cop[keys[i]][j])) / (axis[j][key[0]][k].max - axis[j][key[0]][k].min) - (5 - this.k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top)])
              mark.push([j * (this.chartConfig.axis.width + this.chartConfig.axisMargin.left), (4 - k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top) + this.chartConfig.axis.height * (axis[j][key[0]][k].max - Number(cop[keys[i]][j])) / (axis[j][key[0]][k].max - axis[j][key[0]][k].min) - (5 - this.k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top)])
              break
            }
          }
        }
        data.push({
          copData: copData,
          copColor: copColor
        })
      }
      return { line: data, mark: mark }
    },

    getLineData (axis, cop) {
      const keys = Object.keys(cop)
      const data = []
      for (let i = 0; i < keys.length; i++) {
        const point = []
        for (let j = 0; j < 7; j++) {
          const key = Object.keys(axis[j])
          for (let k = 0; k < axis[j][key[0]].length; k++) {
            if (Number(cop[keys[i]][this.chartValue.copData[j]]) <= axis[j][key[0]][k].max && Number(cop[keys[i]][this.chartValue.copData[j]]) >= axis[j][key[0]][k].min) {
              point.push([j * (this.chartConfig.axis.width + this.chartConfig.axisMargin.left), (4 - k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top) + this.chartConfig.axis.height * (axis[j][key[0]][k].max - Number(cop[keys[i]][this.chartValue.copData[j]])) / (axis[j][key[0]][k].max - axis[j][key[0]][k].min) - (5 - this.k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top)])
              point.push([j * (this.chartConfig.axis.width + this.chartConfig.axisMargin.left) + this.chartConfig.axis.width, (4 - k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top) + this.chartConfig.axis.height * (axis[j][key[0]][k].max - Number(cop[keys[i]][this.chartValue.copData[j]])) / (axis[j][key[0]][k].max - axis[j][key[0]][k].min) - (5 - this.k) * (this.chartConfig.axis.height + this.chartConfig.axisMargin.top)])
              break
            }
          }
        }
        data.push(point)
      }
      return data
    },

    getAxisData (file) {
      const keys = Object.keys(file)
      let pos = 0
      const axissValue = []
      const axisPosition = []
      for (let i = 0; i < keys.length; i++) {
        const axisValue = []
        if (keys[i] === this.chartValue.axisValue[pos]) {
          for (let k = 0; k < file[keys[i]].length; k++) {
            const key1 = Object.keys(file[keys[i]][k])
            const min = file[keys[i]][k][key1[0]][0][0]
            const max = file[keys[i]][k][key1[0]][0][1]
            axisValue.push({
              min: min,
              max: max
            })
            axisPosition.push({
              x: (this.chartConfig.axis.width + this.chartConfig.axisMargin.left) * pos,
              y: (this.chartConfig.axis.height + this.chartConfig.axisMargin.top) * k
            })
          }
          axissValue.push({
            axis: axisValue,
            key: keys[i]
          })
          pos += 1
        }
      }
      // 交换axiss第3个与第4个元素
      axissValue.splice(2, 1, ...axissValue.splice(3, 1, axissValue[2]))
      const axis = {
        axissValue: axissValue,
        axisPosition: axisPosition
      }
      return axis
    }
  },
  mounted () {
    this.creatPCchart()
  }
}
</script>

<style scoped>

.container1 {
  width: 100%;
  height: 100%;
  /*border: 2px solid black;*/
}

</style>
