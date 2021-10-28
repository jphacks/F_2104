<template>
<v-app id="inspire">
    <div class="small">
        <line-chart :chart-data="datacollection"></line-chart>
        <div class="text-center">
            <v-btn  depressed small @click="fillData()">Randomize</v-btn>
        </div>
    </div>
</v-app>
</template>

<script>
export default {
    data () {
      return {
        datacollection: null
      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        this.datacollection = {
          labels: [this.getRandomInt(), this.getRandomInt()],
          datasets: [
            {
              label: 'Test Data2',
              backgroundColor: 'rgba(255, 100, 130, 0.2)',
              data: [this.getRandomInt(), this.getRandomInt()]
            }, {
              label: 'Test Data2',
              backgroundColor: 'rgba(100, 130, 255, 0.2)',
              data: [this.getRandomInt(), this.getRandomInt()]
            }
            , {
              label: 'Test Data3',
              backgroundColor: 'rgba(130, 255, 100, 0.2)',
              data: [this.getRandomInt(), this.getRandomInt()]
            }
          ]
        }
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      }
    }
};
</script>
<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
