<template>
  <div>
    <div class="box">
      <div class="box-title">
        <label style="color: #999;font-size: 14px;padding-left: 30px">触发器个数</label>
        <label style="font-size: 14px">{{trigger.length}}</label>
      </div>
      <div class="box-table">
        <el-table :data="trigger" style="width: 100%">
          <el-table-column
            label="数据流名称"
            prop="name"
            align="center">
          </el-table-column>
          <el-table-column
            label="所属设备ID"
            prop="dev_id"
            align="center">
          </el-table-column>
          <el-table-column
            label="所属设备名"
            prop="dev_name"
            align="center">
          </el-table-column>
          <el-table-column
            label="单位符号"
            prop="unit_symbol"
            align="center">
          </el-table-column>
          <el-table-column label="阈值设置" align="center">
            <el-table-column
              label="数值"
              prop="max"
              align="center">
            </el-table-column>
            <el-table-column
              label="判断类型"
              prop="trigger_type"
              align="center">
            </el-table-column>
          </el-table-column>
          <el-table-column
            label="是否开启触发器"
            prop="trigger"
            align="center">
          </el-table-column>
          <el-table-column label="操作" align="center">
            <template slot-scope="scope">
              <el-tooltip content="编辑" placement="top">
                <i class="el-icon-ump-bianji1"></i>
              </el-tooltip>
              <el-tooltip content="删除" placement="top">
                <i class="el-icon-ump-shanchu"
                   style="padding-left:5px;"></i>
              </el-tooltip>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
  import api from '../../axios'
  export default {
    name: "trigger",
    data(){
      return{
        trigger: []
      }
    },
    created(){
      api.getTrigger().then((res)=>{
        if(!res.data.code){
          this.trigger = res.data.data
        }
      })
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
</style>
