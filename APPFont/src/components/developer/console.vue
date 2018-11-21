<template>
  <div>
    <div class="box">
      <!--表头-->
      <div class="box-title">
        <label style="color: #999;font-size: 14px;padding-left: 30px">控制台</label>
      </div>
      <!--介绍-->
      <div class="introduce">
        <p>如果你只是希望控制自己的设备，那么选择好设备号，输入需要发送的内容</p>
        <p>如果你的设备订阅了自己的主题，那么需要选择自定义方式发送，填写主题名和消息内容</p>
      </div>
      <!--控制台-->
      <div class="control-zone">
        <el-row>
        <p>默认消息</p>
        <el-form v-model="msg1" :inline="true" style="padding-left: 25px">
          <el-col :span="7"><el-form-item label="选择设备">
            <el-select v-model="msg1.topic" placeholder="请选择你的设备">
              <el-option
                v-for="item in device_info"
                :key="item.id"
                :label="item.name"
                :value="'$client/'+item.id">
              </el-option>
            </el-select>
          </el-form-item></el-col>
          <el-col :span="7"><el-form-item label="Qos设置">
            <el-select v-model="msg1.qos" placeholder="请选择QoS">
              <el-option label="0" key="0" value="0"></el-option>
              <el-option label="1" key="1" value="1"></el-option>
              <el-option label="2" key="2" value="2"></el-option>
            </el-select>
          </el-form-item></el-col>
          <el-col :span="7"> <el-form-item label="消息内容">
            <el-input v-model="msg1.payload" autocomplete="off" placeholder="请输入发送的内容"></el-input>
          </el-form-item></el-col>
          <el-col :span="3"><el-button type="primary"  @click="send1">确认发送</el-button></el-col>
        </el-form>
        </el-row>
        <el-row>
        <p>自定义消息</p>
        <el-form v-model="msg2" :inline="true" style="padding-left: 25px">
          <el-col :span="7"><el-form-item label="消息主题">
            <el-input v-model="msg2.topic" autocomplete="off" placeholder="请输入主题名" ></el-input>
          </el-form-item></el-col>
          <el-col :span="7"><el-form-item label="Qos设置">
            <el-select v-model="msg2.qos" placeholder="请选择QoS">
              <el-option label="0" key=0 value=0></el-option>
              <el-option label="1" key=1 value=1></el-option>
              <el-option label="2" key=2 value=2></el-option>
            </el-select>
          </el-form-item></el-col>
          <el-col :span="7"><el-form-item label="消息内容">
            <el-input v-model="msg2.payload" autocomplete="off" placeholder="请输入消息内容"></el-input>
          </el-form-item></el-col>
          <el-col :span="3"><el-button type="primary" @click="send2">确认发送</el-button></el-col>
        </el-form>
        </el-row>
      </div>
    </div>
  </div>
</template>

<script>
  import api from '../../axios'

  export default {
    name: "console",
    data() {
      return {
        device_info: [],
        msg1: {
          topic: "",
          qos: "",
          payload: ""
        },
        msg2: {
          topic: "",
          qos: "",
          payload: ""
        },
      }
    },
    created() {
      api.getDevice().then(res => {
        if (!res.data.code) {
          this.device_info = res.data.data;
        }
        else {
          this.$message({
            message: '设备信息获取失败！可能有部分功能无法正常使用。',
            type: 'warning'
          });
        }
      }).catch(res => {
        this.$message({
          message: '设备信息获取失败！可能有部分功能无法正常使用。',
          type: 'warning'
        });
      });
    },
    methods:{
      send1(){
        api.publish(this.msg1).then((res)=>{
          if(!res.data.code){
            this.$notify({
              title: '消息发送成功',
              type: 'success'
            });
          }
          else{
            this.$notify.error({
              title: '消息发送失败',
              message: '请检查消息内容重试'
            });
          }
        }).catch((res)=>{
          this.$notify.error({
            title: '消息发送失败',
            message: '请检查消息内容重试'
          });
        });
      },
      send2(){
        api.publish(this.msg2).then((res)=>{
          console.log(res.data)
        })
      }
    }
  }
</script>

<style scoped>
  .box {
    min-width: 897px;
    margin: 50px 60px 10px;
    background-color: #FFF;
    min-height: 600px;
    border-radius: 5px;
  }

  .box-title {
    padding-bottom: 10px;
    padding-top: 10px;
    border-bottom: 1px solid #dbe1e4;
  }

  .introduce {
    min-width: 855px;
    padding: 10px 0;
    border-bottom: 1px solid #dbe1e4;
  }

  .introduce p {
    font-size: 14px;
    color: #5e6d82;
    line-height: 1.5em;
    text-indent: 2em;
  }
  .control-zone p{
    font-size: 22px;
    font-weight: 400;
    color: #1f2f3d;
    margin: 20px;
    display: block;
  }
</style>
