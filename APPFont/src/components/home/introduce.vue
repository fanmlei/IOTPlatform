<template>
  <div>
    <!--首页轮播图-->
    <div style="text-align: center">
      <el-carousel>
        <el-carousel-item v-for="(img,index) in imgs" :key="index">
          <img :src="img.img">
        </el-carousel-item>
      </el-carousel>
    </div>

    <div class="img-title">
      <el-row>
        <el-col :span="8">
          <div>
            <i class="el-icon-ump-mqtt" style="color: #0086b3;"></i>
            <div class="introduce">
              <em>MQTT协议</em>
              <p>支持大多数MQTT协议的物联网设备的接入，提供Arduino接入实例</p>
            </div>
          </div>
        </el-col>
        <el-col :span="8">
          <div>
            <i class="el-icon-ump-page" style="color: #ffbd00;"></i>
            <div class="introduce">
              <em>网页控制</em>
              <p>在开发者中心可对接入设备进行管理、查看、下发指令</p>
            </div>
          </div>
        </el-col>
        <el-col :span="8">
          <div>
            <i class="el-icon-ump-weixin" style="color: #55a532;"></i>
            <div class="introduce">
              <em>微信通知</em>
              <p>绑定微信后可随时随地通过微信公众号实现网页端操作，接收触发器通知</p>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <!--平台特色-->
    <div style="text-align: center">
      <p style=" text-align: center;font-size: 34px;margin: 78px 0 48px;">平台简介</p>
    </div>
    <div class="feature">
      <el-row>
        <el-col :span="7" :offset=1>
          <div>
            <div style="display:inline-block;text-align: center;line-height: 150px;">
              <img src="../../assets/imgs/EMQ.png" alt="">
            </div>
            <div class="f-p">
              <em>基于EMQ消息服务</em>
              <p>MQTT协议，可用传感器数据储存，或是中继服务器，组件自己的传感器网络</p>
            </div>
          </div>
        </el-col>
        <el-col :span="7" :offset=1>
          <div>
            <i class="el-icon-ump-linghuo" style="color: #3a8ee6"></i>
            <div class="f-p">
              <em>高适用性</em>
              <p>对于连接设备的性能没有要求，有网络支持MQTT协议即可使用</p>
            </div>
          </div>
        </el-col>
        <el-col :span="7" :offset=1>
          <div>
            <i class="el-icon-ump-shiyongrenqun" style="color: #304156"></i>
            <div class="f-p">
              <em>适用人群</em>
              <p>适用于创客和物联网爱好者，有能力编写基本的硬件连接代码</p>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
    <!--平台服务-->
    <div style="text-align: center">
      <p style=" text-align: center;font-size: 34px;margin: 78px 0 48px;">平台服务</p>
    </div>
    <div class="service">
      <el-row>
        <el-col :span="6">
          <div style="text-align: center;">
            <div class="f-icon">
              <i class="el-icon-ump-ziyuan" style="color: #0078d7;font-size: 32px"></i>
            </div>
            <h4>天气服务</h4>
            <p>实时广播各大城市天气信息</p>
          </div>
        </el-col>
        <el-col :span="6">
          <div style="text-align: center;">
            <div class="f-icon">
              <i class="el-icon-ump-youxiang1" style="color: #ce0326;font-size: 32px"></i>
            </div>
            <h4>邮箱服务</h4>
            <p>预设报警信息主动推送</p>
          </div>
        </el-col>
        <el-col :span="6">
          <div style="text-align: center;">
            <div class="f-icon">
              <i class="el-icon-ump-gongzhonghao1" style="color: #d7d7d7;font-size: 32px"></i>
            </div>
            <h4>微信服务</h4>
            <p>公众号操作使用更方便</p>
          </div>
        </el-col>
        <el-col :span="6">
          <div style="text-align: center;">
            <div class="f-icon">
              <i class="el-icon-ump-api" style="color: #202529;font-size: 32px"></i>
            </div>
            <h4>API接口</h4>
            <p>开放API方便二次开发</p>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'Introduce',
    data() {
      return {
        imgs: [
          {
            img: require("../../assets/imgs/1.png")
          },
          {
            img: require("../../assets/imgs/nodeMCU.jpg")
          },
          {
            img: require("../../assets/imgs/3.png")
          },
        ],
        active: 1,

      }
    },
    methods: {
      next() {
        if (this.active++ > 2) this.active = 1;
      }
    }

  }
</script>
<style scoped>
  * {
    padding: 0;
    border: 0;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
  }

  .el-carousel img {
    text-align: center;
    width: auto;
    height: 100%;
  }

  .el-row {
    margin-top: 10px;
  }

  .img-title div {
    height: 100px;
    background-color: #f3f6f9;
  }

  .img-title div i {
    padding-top: 20px;
    padding-left: 20px;
    background-color: #f3f6f9;
    border-left: 1px solid #e8ebef;
    font-size: 60px;
  }

  .img-title .introduce {
    width: 210px;
    height: 80px;
    float: right;
    margin-right: 50px;
    margin-top: 10px;
  }

  .img-title em {
    font-size: 18px;
    font-style: normal;
    font-weight: 200;
    color: #333;
  }

  .img-title p {
    font-size: 12px;
    margin-top: 10px;
    color: #666;
    line-height: 20px;
  }

  .feature .el-col{
    height: 150px;
  }

  .feature i{
    padding-top: 20px;
    padding-left: 20px;
    padding-right: 10px;
    font-size: 60px;
  }

  .feature .f-p {
    width: 210px;
    display:inline-block;
    height: 60px;
    float: right;
    margin-top: 10px;
  }

  .feature em {
    font-size: 18px;
    font-style: normal;
    font-weight: 200;
    color: #333;
  }

  .feature p {
    font-size: 12px;
    margin-top: 10px;
    color: #666;
    line-height: 20px;
  }

  .service em{
    font-size: 18px;
    font-style: normal;
    font-weight: 200;
    color: #333;
  }

  .service p{
    font-size: 12px;
    margin-top: 10px;
    color: #666;
    line-height: 20px;
  }

  .f-icon{
    display: inline-block;
    border: 1px solid #e9ecef;
    border-radius: 50%;
    width: 70px;
    height: 70px;
    text-align: center;
    line-height: 70px
  }

  h4{
    font-weight: 500;
    line-height: 1.2;
    color: #2D3238;
  }
</style>
