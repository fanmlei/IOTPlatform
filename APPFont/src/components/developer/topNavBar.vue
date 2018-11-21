<template>
  <div>
    <el-menu class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-col :span="3">
        <el-menu-item index="0">
          <router-link to="/home/introduce" style="padding-left: 20px">
            <img src="../../assets/imgs/logo.png"/>
          </router-link>
        </el-menu-item>
      </el-col>
      <el-col :span="2" :offset="17">
        <el-submenu index="4">
          <template slot="title">
            <div class="head-img">
              <img src="../../assets/imgs/default-head.png">
            </div>
          </template>
          <el-menu-item index="4-1">个人中心</el-menu-item>
          <el-menu-item index="4-2">账户设置</el-menu-item>
          <el-menu-item index="4-3">退出</el-menu-item>
        </el-submenu>
      </el-col>
    </el-menu>
    <!--顶部-->
  </div>
</template>
<script>
  export default {
    name: "DTopNavBar",
    data() {
      return {

      }
    },
    methods: {
      handleSelect() {

      }
    }
  }
</script>
<style scoped>
  * {
    padding: 0;
    border: 0;
  }
  .el-header {
    color: #333;
    text-align: center;
    border: 0;
    padding: 0;
  }

  .head-img {
    border-radius: 50%;
    overflow: hidden;
    float: left;
  }

  a {
    text-decoration: none;
  }

  .router-link-active {
    text-decoration: none;
  }
</style>
