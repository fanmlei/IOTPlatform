<template>
  <div class="home">

    <el-container direction="vertical">
      <!--顶部-->
      <el-header>
        <top-nav></top-nav>
      </el-header>
      <!--主体内容显示-->
      <el-main>
        <router-view></router-view>
      </el-main>
      <!--底部-->
      <el-footer>
        <Footer></Footer>
      </el-footer>
    </el-container>
  </div>
</template>
<script>
  import topNav from './topNavBar'
  import Footer from './footer'
  export default {
    name: 'Home',
    data(){
      return{

      }
    },
    components:{
      Footer,
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

  .el-main{
    margin: 0 199px;
    min-height: 390px;
  }
</style>
