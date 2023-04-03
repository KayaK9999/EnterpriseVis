<template>
  <div class="container">
    <svg width="100%" height="100%"></svg>
  </div>
  <button @click="creatScatterChart">111</button>
</template>

<script>
import axisJson from '../../../backEnd/data/axis2.json'
import pointJson2 from '../../../backEnd/data/point_2.json'
import pointJson3 from '../../../backEnd/data/point_3.json'
import pointJson4 from '../../../backEnd/data/point_4.json'
import pointJson5 from '../../../backEnd/data/point_5.json'
import pointJson6 from '../../../backEnd/data/point_6.json'
import * as d3 from 'd3'

export default {
  name: 'view3_2',
  data () {
    return {
      chartValue: {
        showAll: [14, 18, 25, 24, 22, 7],
        file: [pointJson2, pointJson3, pointJson4, pointJson5, pointJson6]
      },
      chartConfig: {
        margin: 0,
        squareValue: 270,
        axisValue: [30, 80, 130, 180, 230],
        pointColor: [
          ['#C8C8C8', '#000082', '#008200', '#820000', '#828200', '#820082'],
          ['#000000', '#0000FF', '#00FF00', '#FF0000', '#FFFF00', '#FF00FF']
        ]
      }
    }
  },
  methods: {
    getColor (idx, proportion) {
      const palette = [ // 从上到下：绿黄蓝紫灰红
        ['#C8C8FF', '#000082'],
        ['#C8FFC8', '#008200'],
        ['#FFC8C8', '#820000'],
        ['#C8FFC8', '#008200'],
        ['#FFC8C8', '#820000'],
        ['#C8FFC8', '#008200']
      ]
      const i = d3.interpolateLab(palette[idx][0], palette[idx][1])
      return i(proportion)
    },
    creatScatterChart () {
      // D3画图中this指代对象会发生改变
      const that = this
      const main = d3.select('.container svg')
        .append('g')
        .classed('main', true)
        .attr('transform', 'translate(' + 0 + ',' + 0 + ')')
      const coordinations = that.calSquareCoordinates(4)
      const squares = main.append('g')
        .classed('squares', true)
      squares.selectAll('g')
        .data(coordinations)
        .enter()
        .append('g')
        .attr('class', function (d, i) {
          return 'square' + (i + 1)
        })
      for (let i = 0; i < coordinations.length; i++) {
        const square = squares.select('.square' + (i + 1))
        const coordination = coordinations[i]
        square.append('rect')
          .attr('x', coordination.x)
          .attr('y', coordination.y)
          .attr('width', that.chartConfig.squareValue)
          .attr('height', that.chartConfig.squareValue)
          // .attr('stroke', 'red')
          .attr('fill', 'none')
        const axiss = square.append('g')
          .classed('axiss', true)
          .attr('transform', 'translate(' + coordination.x + ',' + coordination.y + ')')
        axiss.selectAll('g')
          .data(that.getAxiss()[that.chartValue.showAll[i]])
          .enter()
          .append('g')
          .attr('class', function (d, i) {
            return 'axis' + (i + 1)
          })
        const smallSquares = square.append('g')
          .classed('smallSquares', true)
          .attr('transform', 'translate(' + coordination.x + ',' + coordination.y + ')')
        smallSquares.selectAll('g')
          .data(that.getAxiss()[that.chartValue.showAll[i]])
          .enter()
          .append('g')
          .attr('class', function (d, i) {
            return 'smallSquare' + (i + 1)
          })
        for (let k = 0; k < that.getAxiss()[that.chartValue.showAll[i]].length; k++) {
          const axis = axiss.select('.axis' + (k + 1))
          const smallSquare = smallSquares.select('.smallSquare' + (k + 1))
          if (i % 2 === 0) {
            axis.append('rect')
              // 按照 4 3 2 1 0进行作图
              .attr('x', that.chartConfig.axisValue[that.getAxiss()[that.chartValue.showAll[i]].length - 1 - k] + 5)
              .attr('y', 10)
              .attr('width', 40)
              .attr('height', 10)
              .attr('fill', function (d, index) {
                return that.getColor(i, that.getAxiss()[that.chartValue.showAll[i]][k].proportion)
              })
            for (let j = 0; j < that.getAxiss()[that.chartValue.showAll[i]].length; j++) {
              smallSquare.append('rect')
                .attr('x', that.chartConfig.axisValue[k])
                .attr('y', that.chartConfig.axisValue[j])
                .attr('width', 50)
                .attr('height', 50)
                .attr('fill', 'none')
                .attr('stroke-width', 1)
                .attr('stroke', 'black')
                .attr('stroke-dasharray', 2)
            }
          } else {
            axis.append('rect')
              .attr('y', that.chartConfig.axisValue[that.getAxiss()[that.chartValue.showAll[i]].length - 1 - k] + 5)
              .attr('x', 10)
              .attr('width', 10)
              .attr('height', 40)
              .attr('fill', function (d, index) {
                return that.getColor(i, that.getAxiss()[that.chartValue.showAll[i]][k].proportion)
              })
            for (let j = 0; j < that.getAxiss()[that.chartValue.showAll[i]].length; j++) {
              smallSquare.append('rect')
                .attr('x', that.chartConfig.axisValue[j])
                .attr('y', that.chartConfig.axisValue[k])
                .attr('width', 50)
                .attr('height', 50)
                .attr('fill', 'none')
                .attr('stroke-width', 1)
                .attr('stroke', 'black')
                .attr('stroke-dasharray', 2)
            }
          }
        }
        const pointsData = that.getPoints(that.chartValue.file[i], 0)
        const pointsCoordinates = that.calPointsCoordinates(pointsData.points, that.getAxiss()[that.chartValue.showAll[i]], that.getAxiss()[that.chartValue.showAll[i + 1]], i % 2)
        const points = main.append('g')
          .classed('points', true)
        points.selectAll('points')
          .data(pointsCoordinates)
          .enter()
          .append('circle')
          .attr('cx', function (d) {
            return d.x + coordinations[i].x
          })
          .attr('cy', function (d) {
            return d.y + coordinations[i].y
          })
          .attr('r', 3)
          .attr('fill', function (d) {
            return d.pointColor
          })
        const starsCoordinates = that.calPointsCoordinates(pointsData.stars, that.getAxiss()[that.chartValue.showAll[i]], that.getAxiss()[that.chartValue.showAll[i + 1]], i % 2)
        const star = main.append('g')
          .attr('transform', 'translate(' + (starsCoordinates[0].x + coordinations[i].x) + ',' + (starsCoordinates[0].y + coordinations[i].y) + ')')
          .append('path')
          .attr('d', d3.symbol().type(d3.symbolStar).size(40))
          .attr('stroke', 'black')
          .attr('stroke-width', 'black')
        star.attr('fill', starsCoordinates[0].pointColor)
      }
    },
    // 获取axis.json文件里的数据，返回一个26*5的数组，元素为min，max，proportion
    getAxiss () {
      // keys为第一层26个title
      // key1为里面title，就一个，只有0可用
      // 读取数组里范围的格式：axisJson[keys[0]][0][keys1[0]][0][0]
      // 读取数组里比例的格式：axisJson[keys[0]][0][keys1[0]][1]
      const keys = Object.keys(axisJson)
      const axiss = []
      for (let i = 0; i < keys.length; i++) {
        const axis = []
        for (let k = 0; k < axisJson[keys[i]].length; k++) {
          const key1 = Object.keys(axisJson[keys[i]][k])
          const min = axisJson[keys[i]][k][key1[0]][0][0]
          const max = axisJson[keys[i]][k][key1[0]][0][1]
          const proportion = axisJson[keys[i]][k][key1[0]][1]
          axis.push({
            min: min,
            max: max,
            proportion: proportion
          })
        }
        axiss.push(axis)
      }
      return axiss
    },
    // 获取point和point_obj文件里点的数据，返回一个数组，元素为x,y,axis
    getPoints (fileName, highLight) {
      const pointsFile = fileName
      const pointKeys = Object.keys(pointsFile)
      const points = []
      const stars = []
      for (let i = 0; i < pointKeys.length; i++) {
        const x = pointsFile[pointKeys[i]][0][0]
        const y = pointsFile[pointKeys[i]][0][1]
        if (x !== '0.00' && y !== '0.00' && pointsFile[pointKeys[i]][3] === 0) {
          const num1 = pointsFile[pointKeys[i]][1]
          const num2 = pointsFile[pointKeys[i]][2]
          points.push({
            name: pointKeys[i],
            x: x,
            y: y,
            pointColor: highLight === num2 ? this.chartConfig.pointColor[1][num1 + 1] : this.chartConfig.pointColor[0][num1 + 1]
          })
        } else if (x !== '0.00' && y !== '0.00' && pointsFile[pointKeys[i]][3] === 1) {
          const num1 = pointsFile[pointKeys[i]][1]
          const num2 = pointsFile[pointKeys[i]][2]
          stars.push({
            name: pointKeys[i],
            x: x,
            y: y,
            pointColor: highLight === num2 ? this.chartConfig.pointColor[1][num1 + 1] : this.chartConfig.pointColor[0][num1 + 1]
          })
        }
      }
      const point = {
        points: points,
        stars: stars
      }
      return point
    },
    // 传入数据分别为点数据，本轴数据，外轴数据，奇偶判别
    // 按轴输出点的坐标,以及对应的颜色
    calPointsCoordinates (pointsData, axisData1, axisData2, flag) {
      const points = []
      for (let i = 0; i < pointsData.length; i++) {
        const sliceX = this.calSliceY(pointsData[i].x, axisData1)
        const sliceY = this.calSliceY(pointsData[i].y, axisData2)
        console.log('1')
        if (flag === 0) {
          const x = this.chartConfig.axisValue[axisData1.length - 1 - sliceX] + 40 - (pointsData[i].x - axisData1[sliceX].min) / (axisData1[sliceX].max - axisData1[sliceX].min) * 40
          const y = this.chartConfig.axisValue[axisData2.length - 1 - sliceY] + 40 - (pointsData[i].y - axisData2[sliceY].min) / (axisData2[sliceY].max - axisData2[sliceY].min) * 40
          points.push({
            x: x,
            y: y,
            pointColor: pointsData[i].pointColor
          })
        } else {
          const y = this.chartConfig.axisValue[axisData1.length - 1 - sliceX] + 40 - (pointsData[i].x - axisData1[sliceX].min) / (axisData1[sliceX].max - axisData1[sliceX].min) * 40
          const x = this.chartConfig.axisValue[axisData2.length - 1 - sliceY] + 40 - (pointsData[i].y - axisData2[sliceY].min) / (axisData2[sliceY].max - axisData2[sliceY].min) * 40
          points.push({
            x: x,
            y: y,
            pointColor: pointsData[i].pointColor
          })
        }
      }
      return points
    },
    calSliceY (y, axisData) {
      for (let i = 0; i < axisData.length; i++) {
        if (y <= axisData[i].max && y >= axisData[i].min) {
          return i
        }
      }
    },
    // 计算大正方形的起点坐标，idx为第idx个
    calSquareCoordinates (idx) {
      const coordinations = []
      for (let i = 0; i <= idx; i++) {
        coordinations.push((i % 2 === 0) ? { x: i / 2 * this.chartConfig.squareValue, y: (i / 2) * this.chartConfig.squareValue } : { x: (i + 1) / 2 * this.chartConfig.squareValue, y: (i - 1) / 2 * this.chartConfig.squareValue })
      }
      return coordinations
    }
  },
  mounted () {
    this.creatScatterChart()
  }
}
</script>

<style scoped>

.container {
  width: 1200px;
  height: 900px;
  /*border: 2px solid black;*/
}

.smallSquare rect {
  border: 2px solid black;
}

.axiss rect {
  border: 2px solid black;
}

</style>
