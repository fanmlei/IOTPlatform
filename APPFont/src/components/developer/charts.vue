<template>
  <div>
    <div v-for="(value,key,index) in charts_data" :key="index" class="panel-chart">
      <span>{{key}}</span>
      <div v-for="(value1,key1,index1) in charts_data[key]" :key="index1">
        <div :id="gernerateId((index+'-'+index1))" style="width:100%;height:400px;padding-left: 20px"></div>
      </div>
    </div>
  </div>
</template>


<script>
  import api from '../../axios.js'
  export default {
    name: "charts",
    data() {
      return {
        charts_data: {},
        sss: ''
      }
    },
    methods: {
      gernerateId: function (key) {
        return key
      }
    },
    created() {
      api.charts().then((res) => {
        if (res.data.code === 0) {
          this.charts_data = res.data.data;
          console.log(this.charts_data);
        }
      });
    },
    mounted() {
      api.charts().then((res) => {
        if (res.data.code === 0) {
          this.charts_data = res.data.data;
          var index = 0;
          for (var i in this.charts_data) {
            var index1 = 0;
            for (var d in this.charts_data[i]){
              var myChart = this.$echarts.init(document.getElementById(index+'-'+index1));
              myChart.setOption(
                {
                  title: {
                    text: d,
                    subtext: this.charts_data[i][d][0][0] + '至' + this.charts_data[i][d][0][this.charts_data[i][d][0].length - 1],
                  },
                  tooltip: {
                    trigger: 'axis'
                  },

                  calculable: true,
                  xAxis: [
                    {
                      type: 'category',
                      boundaryGap: false,
                      data: this.charts_data[i][d][0],
                    }
                  ],
                  yAxis: [
                    {
                      type: 'value',

                    }
                  ],
                  series: [
                    {
                      type: 'line',
                      data: this.charts_data[i][d][1],
                      smooth: true,
                      itemStyle: {
                        normal: {
                          color: '#5daefd',
                          lineStyle: {
                            color: '#5daefd',
                          },
                          areaStyle: {
                            color: '#5daefd',
                            // type:'default',
                          }
                        }
                      },
                    },
                  ]
                }
              );
              index1 += 1;
            }

            index += 1;
          }
        }
      });
      // console.log(this.charts_data);

    }
  }
</script>

<style scoped>
  .panel-chart {
    margin: 60px 55px 40px 50px;
    background-color: #ffffff;
    height: 100%;
  }
  .panel-chart span {
    display: block;

    font-size: 30px;
  }
</style>
