<template>
  <div>
    <Card :status="status" :icon="icon_status" :color="color" />
    <button v-if="icon_status==`check-circle`" class="button is-fullwidth" @click="icon_status=`close-circle`,color=`danger`,status='汚い状況です'">UIサンプル用機能：O⇄X表示切り替え</button>
    <button v-if="icon_status==`close-circle`" class="button is-fullwidth" @click="icon_status=`check-circle`,color=`success`,status='問題ありません'">UIサンプル用機能：O⇄X表示切り替え</button>
    <table class="table is-fullwidth is-hoverable scrollable">
      <thead>
        <tr>
          <th>detect_times</th>
          <th>detect_ratio</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.datetime" >
          <td>{{item.detect_times}}</td>
          <td>{{item.value/item.detect_ratio}}</td>
          <td>{{item.value}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
const csvParse = require('csv-parse/lib/sync')

export default {
  data() {
    return {
      items: [],
      color: "success",
      status: '問題ありません',
      icon_status: 'check-circle',
    }
  },
  async mounted() {
    try {
      const csv = await this.$axios.$get(
        'https://raw.githubusercontent.com/jphacks/F_2104/dev_esp32/output/dustsensor_data/dustsensor_data.csv'
      )
      this.items = csvParse(csv, { columns: true })
    } catch (error) {
      // とりあえず放置
    }
  }
}
</script>
