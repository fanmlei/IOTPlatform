<template>
  <div>
    <el-row class="tac" >
      <el-col :span="24">
        <el-menu class="el-menu-vertical-demo"
                 background-color="#304156"
                 text-color="#bfcbd9"
                 active-text-color="#409eff"
                 :default-active="$route.path"
                 router >
          <el-menu-item index="/developer/dashboard">
            <i class="el-icon-ump-18"></i>
            <span slot="title">主页</span>
          </el-menu-item>
          <el-menu-item index="/developer/charts">
            <i class="el-icon-ump-shuju2"></i>
            <span slot="title">历史数据</span>
          </el-menu-item>
          <el-menu-item index="/developer/devices">
            <i class="el-icon-ump-shebei2"></i>
            <span slot="title">设备管理</span>
          </el-menu-item>
          <el-menu-item index="/developer/streams">
            <i class="el-icon-ump-shuju1"></i>
            <span slot="title">数据流管理</span>
          </el-menu-item>
          <el-menu-item index="/developer/triggers">
            <i class="el-icon-ump-chufaqi"></i>
            <span slot="title">触发器管理</span>
          </el-menu-item>
          <el-menu-item index="/developer/console">
            <i class="el-icon-ump-kongzhitai1"></i>
            <span slot="title">控制台</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: "DleftNavBar",
    data(){
      return{
          router: true,
      }
    }
  }
</script>

<style scoped>
  .el-aside {
    padding: 0;
    margin: 0;
    border: 0;
  }
</style>



