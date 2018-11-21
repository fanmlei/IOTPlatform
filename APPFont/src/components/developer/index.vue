<template>
  <div class="developer">

    <el-container direction="vertical">
      <!--顶部-->
      <el-header>
        <top-nav></top-nav>
      </el-header>
      <el-container>
        <el-aside style="width: 200px"><left-nav-bar></left-nav-bar></el-aside>
        <el-main  style="background-color: #f0f2f5;"><router-view></router-view></el-main>
      </el-container>
    </el-container>
  </div>
</template>
<script>
  import topNav from './topNavBar';
  import leftNav from './leftNavBar';
  export default {
    name: 'index',
    data(){
      return{

      }
    },
    components:{
      leftNavBar: leftNav,
      topNav: topNav
    },
  }
</script>
<style scoped>
  * {
    padding: 0;
    border: 0;
    margin:0;
  }

  .el-carousel img{
    width:100%;
    height:auto;
  }
  .el-aside {
    height: 100%;
    position: fixed;
    z-index: 1000;
    padding-top: 60px;
    background-color: #304156;
  }
  .el-header {
    width: 100%;
    height: 60px;
    position: fixed;
    padding: 0;
    z-index: 1001;
  }
  .el-main {
    height: 100%;
    margin-left: 200px;
    padding: 0;
    margin-top: 60px;
  }
</style>
