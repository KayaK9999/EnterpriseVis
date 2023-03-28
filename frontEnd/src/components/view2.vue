<template>
  <div class="container" id="view3">
    <svg width="100%" height="100%"></svg>
  </div>

</template>

<script>
import radarAxisJson from '../../../../pyCharm/ybcProject/data/radar_axis.json'
import radarJson from '../../../../pyCharm/ybcProject/data/radar_detail.json'
import bordJson from '../../../../pyCharm/ybcProject/data/bord.json'
import * as d3 from 'd3'
export default {
  name: 'view_2',
  data () {
    return {
      chartData: {
        fieldNames: [
          ['流动比率', '速动比率', '现金比率', '资产负债率', '所有者权益比率', '产权比率'],
          ['流动资产周转率', '流动资产利润率', '固定资产周转率', '固定资产利润率', '总资产周转率', '总资产利润率'],
          ['营业毛利率', '净利润率', '营业利润率', '成本费用利润率', '总资产报酬率', '总负债报酬率']
        ],
        title: ['偿债能力分析', '运营能力分析', '获利能力分析'],
        maxValue: [
          [-1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1]
        ],
        minValue: [
          [-1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1]
        ],
        values: [
          [[10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 100, 100]],
          [[10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 100, 100]],
          [[10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 100, 100]]
        ],
        values_coop_num: [
          [[1, 1, 0, 1, 0], [1, 2, 3, 4, 5], [30, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 30, 4, 5], [1, 2, 3, 4, 5]],
          [[1, 1, 0, 1, 0], [1, 2, 3, 4, 5], [30, 30, 30, 30, 30], [1, 2, 3, 4, 5], [1, 2, 30, 4, 5], [1, 2, 3, 4, 5]],
          [[1, 1, 0, 1, 0], [1, 2, 3, 4, 5], [30, 30, 30, 30, 30], [1, 2, 3, 4, 5], [1, 2, 30, 4, 5], [30, 30, 30, 30, 30]]
        ]
      },
      chartConfig: {
        // 调整雷达图的大小
        radius: 75,
        // 雷达图外扇形半径
        sector_radius: 80,
        // 雷达图外扇形高度
        sector_height: 15,
        // 指标的数量，和fieldNames的长度相同
        total: 6,
        // 网轴的级数，网轴上从小到大有多少个正方形
        level: 5,
        rangeMin: 0,
        rangeMax: 100,
        arc: 2 * Math.PI,
        mainColor: ['#0081C9', '#54B435', '#F7A4A4'],
        count: 0
      }
    }
  },
  props: {
    corCop: Number
  },
  methods: {
    // 计算轴颜色和扇形颜色盘
    // 公司和对比公司的颜色盘
    getColorCoop (idx) {
      const palette = ['#0081C9', '#54B435']
      return palette[idx % palette.length]
    },
    getColor (idx, proportion) {
      const palette = [ // 从上到下：绿黄蓝紫灰红
        ['#2ca25f', '#99d8c9'],
        ['#fdae6b', '#ffeda0'],
        ['#3182bd', '#9ecae1'],
        ['#756bb1', '#bcbddc'],
        ['#636363', '#bdbdbd'],
        ['#f03b20', '#feb24c']
      ]
      const i = d3.interpolateLab(palette[idx][0], palette[idx][1])
      return i(proportion)
    },
    createRadarChart (width, height, idx) {
      // 给data里的值赋值
      // this.chartData.values_main[0][0] = 100
      const that = this
      const main = d3.select('#view3 svg')
        .append('g')
        .classed('main', true)
        // 可以这么写数据，圆中心位置
        .attr('transform', 'translate(' + width + ',' + height + ')')
      const onePiece = this.chartConfig.arc / this.chartConfig.total
      // 每个点坐标
      const polygons = {
        webs: [],
        webPoints: [],
        // 同心圆半径
        radius_circle: []
      }
      // 计算每一层坐标
      for (let k = this.chartConfig.level; k > 0; k--) {
        let webs = ''
        const webPoints = []
        const r = this.chartConfig.radius / this.chartConfig.level * k
        polygons.radius_circle.push(r)
        // 计算一层中每个点的坐标
        for (let i = 0; i < this.chartConfig.total; i++) {
          const x = r * Math.sin(i * onePiece)
          const y = r * Math.cos(i * onePiece)
          const temp = this.findMax(this.chartData.values_coop_num[idx][i])
          webs += x + ',' + y + ' '
          webPoints.push({
            x: x,
            y: y,
            proportion: this.chartData.values_coop_num[idx][i][k] / temp
          })
        }
        polygons.webs.push(webs)
        polygons.webPoints.push(webPoints)
      }
      // 画圆外侧扇形区域
      const sectorsData = this.calcSectorData(idx)
      const pointsData = this.calcPointData(idx)
      const sectors = main.append('g')
        .classed('sectors', true)
      sectors.selectAll('g')
        .data(sectorsData)
        .enter()
        .append('g')
        .attr('class', function (d, i) {
          return 'sector' + (i + 1)
        })
      for (let i = 0; i < sectorsData.length; i++) {
        // 遍历每个雷达图区域
        const sector = sectors.select('.sector' + (i + 1))
        const sectorData = sectorsData[i]
        sector.append('polygon')
          .attr('points', sectorData.polygon)
          .attr('fill', function (d, index) {
            return that.getColor(i, 0.5)
          })
        // .attr('fill', 'none')
        // const circles = sector.append('g')
        //   .classed('circles', true)
        // circles.selectAll('circles')
        //   .data(sectorData.points)
        //   .enter()
        //   .append('circle')
        //   .attr('cx', function (d) {
        //     return d.x
        //   })
        //   .attr('cy', function (d) {
        //     return d.y
        //   })
        //   .attr('r', 1.5)
        //   .attr('stroke', function (d, index) {
        //     return that.getColor(i, 0.5)
        //   })
      }
      // 给两条直线中上色可转换成一条线上色，将第二条线内换成别的颜色就可以
      // 将扇形的多余部分用空白圆覆盖
      const shadow = main.append('circle')
      shadow.attr('cx', 0)
        .attr('cy', 0)
        .attr('r', this.chartConfig.sector_radius)
        .attr('fill', 'white')
      // 画面积图上的标点
      const pointsAreas = main.append('g')
        .classed('pointsAreas', true)
      pointsAreas.selectAll('g')
        .data(pointsData)
        .enter()
        .append('g')
        .attr('class', function (d, i) {
          return 'pointsArea' + (i + 1)
        })
      for (let i = 0; i < pointsData.length; i++) {
        const pointsArea = pointsAreas.select('.pointsArea' + (i + 1))
        const pointArea = pointsArea.append('g')
          .classed('pointArea', true)
        pointArea.selectAll('circles')
          .data(pointsData[i])
          .enter()
          .append('circle')
          .attr('cx', function (d) {
            return that.chartConfig.sector_radius * Math.sin(d)
          })
          .attr('cy', function (d) {
            return that.chartConfig.sector_radius * Math.cos(d)
          })
          .attr('r', 2)
          .attr('fill', that.chartConfig.mainColor[i])
      }
      // 同心圆
      const webs = main.append('g')
        .classed('webs', true)
      webs.selectAll('circle')
        .data(polygons.radius_circle)
        .enter()
        .append('circle')
        .attr('cx', '0')
        .attr('cy', '0')
        .attr('r', function (d) {
          return d
        })
      // 画轴
      // const axissData = this.calcAxisData(polygons, idx)
      // const lines = main.append('g')
      //   .classed('lines', true)
      // lines.selectAll('g')
      //   .data(axissData)
      //   .enter()
      //   .append('g')
      //   .attr('class', function (d, i) {
      //     return 'line' + (i + 1)
      //   })
      // for (let i = 0; i < this.chartConfig.total * this.chartConfig.level; i++) {
      //   const line = lines.select('.line' + (i + 1))
      //   line.append('line')
      //     .attr('x1', 0)
      //     .attr('y1', 0)
      //     .attr('x2', axissData[i].x)
      //     .attr('y2', axissData[i].y)
      //     .attr('stroke-width', 12)
      //     .attr('stroke', 'none')
      // }
      // 标注公司位置
      const copData = this.calcCopData(polygons, idx)
      const pointsLines = main.append('g')
        .classed('pointsLines', true)
      pointsLines.selectAll('g')
        .data(copData)
        .enter()
        .append('g')
        .attr('class', function (d, i) {
          return 'pointsLine' + (i + 1)
        })
      for (let i = 0; i < copData.length; i++) {
        const pointsLine = pointsLines.select('.pointsLine' + (i + 1))
        const pointLine = pointsLine.append('g')
          .classed('pointLine', true)
        pointLine.selectAll('circles')
          .data(copData[i])
          .enter()
          .append('circle')
          .attr('cx', function (d) {
            return d.x
          })
          .attr('cy', function (d) {
            return d.y
          })
          .attr('r', 2)
          .attr('stroke', that.getColor(i, 1))
          .attr('fill', that.getColor(i, 1))
      }
      // 计算点的位置
      const areasData = this.calcAreaData(idx)
      // 添加g分组包含所有雷达图区域
      const areas = main.append('g')
        .classed('areas', true)
      // 添加g分组包含雷达图区域下的多边形和圆点
      areas.selectAll('g')
        .data(areasData)
        .enter()
        .append('g')
        .attr('class', function (d, i) {
          return 'area' + (i + 1)
        })
      for (let i = 0; i < areasData.length; i++) {
        // 遍历每个雷达图区域
        const area = areas.select('.area' + (i + 1))
        const areaData = areasData[i]
        area.append('polygon')
          .attr('points', areaData.polygon)
          .attr('stroke', function (d, index) {
            return that.getColorCoop(i)
          })
          .attr('stroke-width', 0.1)
          .attr('fill', 'none')
        // 绘制雷达图定点
        const circles = area.append('g')
          .classed('circles', true)
        circles.selectAll('circles')
          .data(areaData.points)
          .enter()
          .append('circle')
          .attr('cx', function (d) {
            return d.x
          })
          .attr('cy', function (d) {
            return d.y
          })
          .attr('r', 0.1)
          .attr('stroke', function (d, index) {
            return that.getColorCoop(i)
          })
          .attr('fill', function (d, index) {
            return that.getColorCoop(i)
          })
      }
      // 计算文字坐标
      const textPoints = []
      // 文字坐标位置
      const textRadius = this.chartConfig.radius + 30
      for (let i = 0; i < this.chartConfig.total; i++) {
        const x = textRadius * Math.sin(i * onePiece)
        const y = textRadius * Math.cos(i * onePiece)
        textPoints.push({
          x: x,
          y: y
        })
      }
      const title = main.append('text')
        .classed('title', true)
      title
        // .select('text')
        .attr('x', -160)
        .attr('y', -120)
        // .text('123')
        .text(that.chartData.title[idx])
      // 添加到画布
      const texts = main.append('g')
        .classed('texts', true)
      texts.selectAll('text')
        .data(textPoints)
        .enter()
        .append('text')
        .attr('x', function (d) {
          return d.x
        })
        .attr('y', function (d) {
          return d.y
        })
        .text(function (d, i) {
          return that.chartData.fieldNames[idx][i]
        })
    },
    // 计算面积图上目标公司，对比公司以及均值的点
    calcPointData (idx) {
      const keys = Object.keys(bordJson)
      const copNames = Object.keys(radarJson)
      const pointsData = []
      for (let k = 0; k < 3; k++) {
        const pointData = []
        for (let i = 0; i < 6; i++) {
          let sum = 0
          if (k === 0) {
            for (let j = 0; j < radarAxisJson[keys[idx * 6 + i]].length; j++) {
              sum += radarAxisJson[keys[idx * 6 + i]][j]
            }
            const avg = sum / radarAxisJson[keys[idx * 6 + i]].length
            pointData.push((avg - bordJson[keys[idx * 6 + i]][0][0][0]) / (bordJson[keys[idx * 6 + i]][0][4][1] - bordJson[keys[idx * 6 + i]][0][0][0]) * this.chartConfig.arc / 30 * 4 + i * this.chartConfig.arc / 6)
          } else if (k === 1) {
            pointData.push((radarJson[copNames[0]][idx * 6 + i] - bordJson[keys[idx * 6 + i]][0][0][0]) / (bordJson[keys[idx * 6 + i]][0][4][1] - bordJson[keys[idx * 6 + i]][0][0][0]) * this.chartConfig.arc / 30 * 4 + i * this.chartConfig.arc / 6)
          } else {
            pointData.push((radarJson[copNames[this.corCop]][idx * 6 + i] - bordJson[keys[idx * 6 + i]][0][0][0]) / (bordJson[keys[idx * 6 + i]][0][4][1] - bordJson[keys[idx * 6 + i]][0][0][0]) * this.chartConfig.arc / 30 * 4 + i * this.chartConfig.arc / 6)
          }
        }
        pointsData.push(pointData)
      }
      return pointsData
    },
    calcCopData (polygons, idx) {
      const keys = Object.keys(radarAxisJson)
      const copDatas = []
      for (let i = 0; i < 6; i++) {
        const copData = []
        for (let j = 0; j < radarAxisJson[keys[idx * 6 + i]].length; j++) {
          let sector = -1
          for (let k = 0; k < 5; k++) {
            if (radarAxisJson[keys[idx * 6 + i]][j] <= bordJson[keys[idx * 6 + i]][0][k][1] && radarAxisJson[keys[idx * 6 + i]][j] >= bordJson[keys[idx * 6 + i]][0][k][0]) {
              sector = k
            }
          }
          const min = bordJson[keys[idx * 6 + i]][0][sector][0]
          const max = bordJson[keys[idx * 6 + i]][0][sector][1]
          copData.push({
            x: polygons.webPoints[0][i].x / 5 * (5 - ((radarAxisJson[keys[idx * 6 + i]][j] - min) / (max - min) + sector)),
            y: polygons.webPoints[0][i].y / 5 * (5 - ((radarAxisJson[keys[idx * 6 + i]][j] - min) / (max - min) + sector))
          })
        }
        copDatas.push(copData)
      }
      return copDatas
    },
    calcAxisData (polygons, idx) {
      const axisData = []
      for (let i = 0; i < polygons.webPoints.length; i++) {
        for (let j = 0; j < polygons.webPoints[i].length; j++) {
          axisData.push({
            x: polygons.webPoints[i][j].x,
            y: polygons.webPoints[i][j].y,
            proportion: this.chartData.values_coop_num[idx][j][i]
          })
        }
      }
      return axisData
    },
    calcAreaData (idx) {
      const keys = Object.keys(radarJson)
      for (let i = 0; i < 6; i++) {
        this.chartData.values[idx][0][i] = radarJson[keys[0]][idx * 6 + i]
        this.chartData.values[idx][1][i] = radarJson[keys[this.corCop]][idx * 6 + i]
      }
      const areasData = []
      const onePiece = this.chartConfig.arc / this.chartConfig.total
      const values = this.chartData.values[idx]
      // this.chartConfig.rangeMax = this.find1Max(values[0], values[1])
      // this.chartConfig.rangeMin = this.find1Min(values[0], values[1])
      for (let i = 0; i < values.length; i++) {
        const value = values[i]
        let area = ''
        const points = []
        for (let k = 0; k < this.chartConfig.total; k++) {
          // const r = this.chartConfig.radius * (1 - (value[k] - this.chartConfig.rangeMin) / (this.chartConfig.rangeMax - this.chartConfig.rangeMin))
          const r = this.chartConfig.radius * (1 - (value[k] - this.chartData.minValue[idx][k]) / (this.chartData.maxValue[idx][k] - this.chartData.minValue[idx][k]))
          const x = r * Math.sin(k * onePiece)
          const y = r * Math.cos(k * onePiece)
          area += x + ',' + y + ' '
          points.push({
            x: x,
            y: y
          })
        }
        areasData.push({
          // 用于画连线的定义
          polygon: area,
          // 用于计算单个点的定义
          points: points
        })
      }
      return areasData
    },
    calcSectorData (idx) {
      const keys = Object.keys(bordJson)
      for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 5; j++) {
          this.chartData.values_coop_num[idx][i][j] = bordJson[keys[idx * 6 + i]][1][j]
        }
      }
      const sectorData = []
      const onePiece = this.chartConfig.arc / 30
      const values = this.chartData.values_coop_num[idx]
      // 分6次画扇形
      for (let i = 0; i < values.length; i++) {
        const value = values[i]
        let sector = ''
        const points = []
        // 每个扇形中有5个点
        const temp = this.findMax(value)
        for (let j = 0; j < value.length; j++) {
          const r = this.chartConfig.sector_radius + value[j] / temp * this.chartConfig.sector_height
          const x = r * Math.sin((i * 5 + j) * onePiece)
          const y = r * Math.cos((i * 5 + j) * onePiece)
          sector += x + ',' + y + ' '
          points.push({
            x: x,
            y: y
          })
          if (j === value.length - 1) {
            sector += 0 + ',' + 0 + ' '
          }
        }
        sectorData.push({
          polygon: sector,
          points: points
        })
      }
      return sectorData
    },
    findMax (array) {
      let temp = 0
      for (let i = 0; i < array.length; i++) {
        if (array[i] > temp) {
          temp = array[i]
        }
      }
      return temp
    },
    getMaxMin () {
      const keys = Object.keys(radarAxisJson)
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 6; j++) {
          this.chartData.maxValue[i][j] = radarAxisJson[keys[i * 6 + j]][radarAxisJson[keys[i * 6 + j]].length - 1]
          this.chartData.minValue[i][j] = radarAxisJson[keys[i * 6 + j]][0]
        }
      }
    }
  },
  mounted () {
    this.getMaxMin()
    this.createRadarChart(180, 150, 0)
    this.createRadarChart(180, 450, 1)
    this.createRadarChart(180, 750, 2)
  }
}
</script>

<style>

.container {
  /*margin: 30px auto;*/
  width: 100%;
  height: 100%;
  /*border: 1px solid #000;*/
}

.webs circle {
  fill: white;
  fill-opacity: 0.5;
  stroke: white;
  stroke-dasharray: 10, 5;
}

.lines line {
  fill: white;
  fill-opacity: 0.5;
  /*stroke: red;*/
  /*stroke-dasharray: 10, 5;*/
}

.areas polygon {
  fill-opacity: 0.5;
  stroke-width: 3;
}

.areas circle {
  fill: white;
  stroke-width: 3;
}

.sectors polygon {
  fill-opacity: 0.5;
  stroke-width: 3;
}

.sectors circle {
  fill: white;
  stroke-width: 1;
}

.texts text {
  font-size: 10px;
  text-anchor: middle;
}

.webs circle:nth-child(odd) {
  fill: lightgray;
}

</style>
