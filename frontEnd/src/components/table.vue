<template>
  <div class="mtable">
    <table class="table" >
      <thead>
      <th v-if="mulSelect" >
        <div><input type="checkbox" v-model="allSelected" /></div>
      </th>
      <th v-for="field in fields" :key="field">
        {{field.name}}
      </th>
      </thead>
      <tbody>
      <tr v-for="(data, index) in rows" :key="index">
        <td v-if="mulSelect" >
          <div><input type="checkbox" v-model="items[index].seleced" /></div>
        </td>
        <td v-for="field in fields" :key="field">
          {{data[field.name]}}
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
function getItems () {
  const items = []
  for (let i = 0; i < 100; i++) { // 定义支持最大行数为100行
    items.push({
      seleced: false
    })
  }
  return items
}

const ITEMS = getItems()
export default {
  name: 'table_1',
  data () {
    return {
      items: ITEMS
    }
  },
  props: [
    'fields',
    'rows',
    'mulSelect'
  ],
  computed: {
    allSelected: {
      get: function () {
        return this.items.reduce(function (prev, curr) {
          return prev && curr.seleced
        }, true)
      },
      set: function (newValue) {
        this.items.forEach(function (item) {
          item.seleced = newValue
        })
      }
    }
  }
}
</script>

<style scoped>

table.table{
  margin: 0 auto;
  empty-cells:show;
  border-collapse: collapse;
  width: 100%;
}

.table tr{
  background: white;

}

.mtable{
  width: 100%;
  max-height: 100%;
  overflow: auto;
  background: #FFEFC8;
}
.table td,.table th{
  border: 1px #eee solid;
  height: 30px;
  line-height: 30px;
  min-width: 100px;
  overflow: hidden;
  font-size: 10px;
}

.table tr td:first-child,.table thead th:first-child{
  width: 32px;
  padding: 0px;
  background: #DDECD6;
}
.table input[type=checkbox]{
  zoom: 180%;
  margin-top: 8px;
  background: darkmagenta;
}

</style>
