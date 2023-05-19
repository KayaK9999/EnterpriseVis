<template>
  <div class="container33">
    <svg width="100%" height="100%"></svg>
  </div>
  <button @click="creatRingChart(2)">circul_2</button>
  <button @click="creatRingChart(3)">circul_3</button>
</template>

<script>
import * as d3 from 'd3'
import circleJson2 from '../../../backEnd/data/circul_2.json'
import circleJson3 from '../../../backEnd/data/circul_3.json'
import circleJson4 from '../../../backEnd/data/circul_4.json'

export default {
  name: 'view3_3',
  data () {
    return {
      chartValue: {
        k: 5
      },
      chartConfig: {
        ringColor: ['#2ca25f', '#fdae6b', '#3182bd', '#756bb1', '#636363', '#f03b20'],
        circleColor: '#99ccff',
        arcColor: 'blue',
        outerRadius: [40, 50, 60, 70, 80, 90],
        innerRadius: [35, 45, 55, 65, 75, 85],
        circleRadius: 30,
        arcRadius: 22
      }
    }
  },
  methods: {
    creatRingChart (idx) {
      const that = this
      let fileName
      switch (idx) {
        case 2: {
          fileName = circleJson2
          break
        }
        case 3: {
          fileName = circleJson3
          break
        }
        case 4: {
          fileName = circleJson4
          break
        }
      }
      const ringData = that.getCircleData(fileName)
      const main = d3.select('.container33 svg')
        .append('g')
        .classed('main', true)
        .attr('transform', 'translate(' + 200 + ',' + 200 + ')')
      const views = main.append('g')
        .classed('views', true)
      views.selectAll('g')
        .data(ringData)
        .enter()
        .append('g')
        .attr('class', function (d, i) {
          return 'view' + (i + 1)
        })
      for (let k = 0; k < 5; k++) {
        // 5将来合图的时候要换
        const value = ringData[k]
        let view = views.select('.view' + (k + 1))
        view = main.append('g').attr('transform', 'translate(' + 0 + ',' + 150 * k + ')')
        const circle = view.append('circle')
        circle.attr('cx', 0)
          .attr('cy', 0)
          .attr('r', that.chartConfig.circleRadius)
          .attr('fill', that.chartConfig.circleColor)
        // 设置扇形原点位置,本质是将画笔g移到该有的位置
        const innerArcRight = view.append('g').attr('transform', 'translate(' + 2 + ',' + 0 + ')')
        const arcsRight = d3.arc()
          .outerRadius(that.chartConfig.arcRadius)
          .innerRadius(0)
          .startAngle(Math.PI)
          .endAngle(Math.PI * (1 - value.rightCircle))
        const arcRight = innerArcRight.append('path')
          .attr('d', arcsRight)
        arcRight.attr('fill', that.chartConfig.arcColor)
        const innerArcLeft = view.append('g').attr('transform', 'translate(' + -2 + ',' + 0 + ')')
        const arcsLeft = d3.arc()
          .outerRadius(that.chartConfig.arcRadius)
          .innerRadius(0)
          .startAngle(Math.PI)
          .endAngle(Math.PI * (value.leftCircle + 1))
        const arcLeft = innerArcLeft.append('path')
          .attr('d', arcsLeft)
        arcLeft.attr('fill', 'blue')
        const arcs = view.append('g')
          .classed('arcs', true)
        arcs.selectAll('g')
          .data(value.proportions)
          .enter()
          .append('g')
          .attr('class', function (d, i) {
            return 'arc' + (i + 1)
          })
        for (let i = 0; i < value.proportionLength; i++) {
          let arc = arcs.select('.arc' + (i + 1))
          arc = d3.arc()
            .outerRadius(that.chartConfig.outerRadius[i])
            .innerRadius(that.chartConfig.innerRadius[i])
            .startAngle(0)
            .endAngle(value.proportions[i] * 2 * Math.PI)
          const outArc = view.append('path')
            .attr('d', arc)
          outArc.attr('fill', that.chartConfig.ringColor[i])
        }
      }
    },
    getCircleData (file) {
      const key = Object.keys(file)
      const keys = Object.keys(file[key[0]])
      const ringData = []
      for (let i = 0; i < this.chartValue.k; i++) {
        const proportion = []
        let temp = 0
        for (let j = 2; file[key[0]][keys[i]][j] !== undefined; j++) {
          proportion.push(file[key[0]][keys[i]][j])
          temp = j - 1
        }
        ringData.push({
          proportionLength: temp,
          leftCircle: file[key[0]][keys[i]][0],
          rightCircle: file[key[0]][keys[i]][1],
          proportions: proportion
        })
      }
      return ringData
    }
  },
  mounted () {
    this.creatRingChart(3)
  }
}
</script>

<style scoped>

.container33 {
  width: 1000px;
  height: 1200px;
  border: 2px solid black;
}

</style>
