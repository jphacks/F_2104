<template>
  <div>
    <Card :status="status" :icon="icon_status" :color="color" />
    <button v-if="icon_status==`check-circle`" class="button is-fullwidth" @click="icon_status=`close-circle`,color=`danger`,status='汚い状況です'">UIサンプル用機能：O⇄X表示切り替え</button>
    <button v-if="icon_status==`close-circle`" class="button is-fullwidth" @click="icon_status=`check-circle`,color=`success`,status='問題ありません'">UIサンプル用機能：O⇄X表示切り替え</button>
    <table class="table is-fullwidth is-hoverable scrollable">
      <thead>
        <tr>
          <th>実測値</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items.data" :key="item.datetime" >
          <td>{{JSON.parse(JSON.stringify(item.value.replace(/\"/g, '\"\"')))}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
// const csvParse = require('csv-parse/lib/sync')

export default {
  // async mounted() {
  //   try {
  //     const csv = await this.$axios.$get(
  //       'https://raw.githubusercontent.com/jphacks/F_2104/dev_esp32/output/dustsensor_data/dustsensor_data.csv'
  //     )
  //     this.items = csvParse(csv, { columns: true })
  //   } catch (error) {
  //     // とりあえず放置
  //   }
  // }
  async asyncData({ $axios }) {
    const items = await $axios.$get('https://sv-souji-f2104.herokuapp.com/data/datas')
    return { items }
  },
  data() {
    return {
      items: [],
      color: "success",
      status: '問題ありません',
      icon_status: 'check-circle',
    }
  },
  // methods: {
  //   evaluation(){
  //     if (this.items.data[array.length -1].value === "{'detect_times': 0, 'detect_ratio': 0, 'value': 0.6200000047683716}") {
  //       alert(this.items.data[array.length -1])
  //       this.color = "success"
  //       this.status = '問題ありません'
  //       this.icon_status = 'check-circle'
  //     } else {
  //       this.color = "danger"
  //       this.status = '問題あります'
  //       this.icon_status = 'exclamation-circle'
  //     }
  //   }
  // }
}
</script>
