<template>
  <div>
    <div class="panel-group">
      <el-row>
        <el-col :span="5" :dev_num="dev_num">
          <img src="../../assets/imgs/device.png" alt="">
          <div class="panel-card-description">
            <div class="description-txt"> 接入设备总数</div>
            <span> {{dev_num}} </span>
          </div>
        </el-col>
        <el-col :span="5" :offset="1" :str_num="str_num">
          <img src="../../assets/imgs/dataStream.png" alt="">
          <div class="panel-card-description">
            <div class="description-txt"> 数据流模板</div>
            <span> {{str_num}} </span>
          </div>
        </el-col>
        <el-col :span="5" :offset="1" :dp_num="dp_num">
          <img src="../../assets/imgs/dataPoint.png" alt="">
          <div class="panel-card-description">
            <div class="description-txt"> 数据点总量</div>
            <span> {{dp_num}} </span>
          </div>
        </el-col>
        <el-col :span="5" :offset="1" :trg_num="trg_num">
          <img src="../../assets/imgs/trigger.png" alt="">
          <div class="panel-card-description">
            <div class="description-txt"> 触发器个数</div>
            <span> {{trg_num}} </span>
          </div>
        </el-col>
      </el-row>
    </div>
    <div class="panel-chart">
      <div id="myChart" style="width:100%;height:400px"></div>
    </div>
  </div>
</template>

<script>
  import api from '../../axios.js'
  export default {
    name: "dashboard",
    data() {
      return {
        dev_num: 0,
        str_num: 0,
        dp_num: 0,
        trg_num: 0,
        time_value: '',
        date: [],
        data: [],
      }
    },
    created() {
      api.dashboard().then((res) => {
        console.log(res.data);
        if (res.data.code === 0) {
          this.dev_num = res.data.data.card.dev_num;
          this.str_num = res.data.data.card.str_num;
          this.dp_num = res.data.data.card.dp_num;
          this.trg_num = res.data.data.card.trg_num;
          this.data = res.data.data.chart.point;
          this.date = res.data.data.chart.title;
          /*ECharts图表*/
          let myChart = this.$echarts.init(document.getElementById('myChart'));
          myChart.setOption(
            {
              title: {
                text: '数据点上传趋势',
                subtext: this.date[0] + '至' + this.date[this.data.length - 1],
              },
              tooltip: {
                trigger: 'axis'
              },
              toolbox: {
                show: true,
                feature: {
                  dataView: {show: true, readOnly: false},
                  magicType: {show: true, type: ['line', 'bar']},
                  restore: {show: true},
                  saveAsImage: {show: true}
                }
              },
              calculable: true,
              xAxis: [
                {
                  type: 'category',
                  boundaryGap: false,
                  data: this.date,
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
                  data: this.data,
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
          )
        }
      });
    },
    mounted() {


    },
    methods: {}
  }
</script>

<style scoped>
  .panel-group {
    margin: 60px 0 40px 50px;
  }

  .panel-chart {
    margin: 60px 55px 40px 50px;
    background-color: #ffffff;
    height: 100%;
  }

  .panel-group .el-col {
    height: 100px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    -webkit-box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    border-color: rgba(0, 0, 0, 0.05);
  }

  .panel-group img {
    padding: 18px 30px;
  }

  .panel-card-description {
    float: right;
    padding: 20px 30px 20px 0;
    line-height: 18px;
    color: rgba(0, 0, 0, 0.45);
    font-size: 16px;
    margin-bottom: 12px;
  }

  .description-txt {
    margin-bottom: 20px;
  }

  .panel-card-description span {

    font-size: 25px;
    color: #000;
    display: inline-block;

  }

  .panel-chart span {
    display: block;
    padding-top: 20px;
    margin-left: 40px;
    font-size: 15px;
    color: rgba(0, 0, 0, 0.45);
  }

  .panel-chart .panel-time {
    padding-top: 10px;
    padding-left: 100px;
  }

  .panel-time i {
    font-style: normal;
    font-size: 35px;
    height: 35px;
    position: relative;
    top: 6px;
  }
</style>
