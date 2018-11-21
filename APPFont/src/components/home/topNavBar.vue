<template>
  <div>
    <el-menu class="el-menu-demo"
             mode="horizontal"
             :default-active="$route.path"
             router>
      <el-col :span="3" :offset="3">
        <el-menu-item index="introduce">
          <img src="../../assets/imgs/logo.png"/>
        </el-menu-item>
      </el-col>
      <el-col :span="2" :offset="1">
        <el-menu-item index="introduce">
          <span>平台介绍</span>
        </el-menu-item>
      </el-col>
      <el-col :span="2">
        <el-menu-item index="document">
          <span>接入指南</span>
        </el-menu-item>
      </el-col>
      <el-col :span="2">
        <el-menu-item index="resource">
          <span>资源下载</span>
        </el-menu-item>
      </el-col>
      <el-col :span="2">
        <el-menu-item index="/developer">
          <span>开发者中心</span>
        </el-menu-item>
      </el-col>
      <el-col :span="1" :offset="2">
        <el-menu-item index="/login">
          <span>登录</span>
        </el-menu-item>
      </el-col>
      <el-col :span="1">
        <el-menu-item index="/register">
          <span>注册</span>
        </el-menu-item>
      </el-col>
      <el-col :span="2">
        <el-submenu index="7">
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
    name: "HTopNavBar",
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
