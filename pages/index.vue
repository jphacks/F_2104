<template>
  <div>
    <table class="table is-fullwidth is-hoverable">
      <thead>
        <tr>
          <th>detect_times</th>
          <th>detect_ratio</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id" >
          <td>{{item.detect_times}}</td>
          <td>{{item.detect_ratio}}</td>
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
      items: []
    }
  },
  async mounted() {
    try {
      const csv = await this.$axios.$get(
        'https://raw.githubusercontent.com/jphacks/F_2104/dev_esp32/output/dustsensor_data/test.csv'
      )
      this.items = csvParse(csv, { columns: true })
    } catch (error) {
      // とりあえず放置
    }
  }
}
</script>
