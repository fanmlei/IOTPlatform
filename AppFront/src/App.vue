<template>
  <div id="app">
    <p>{{ msg }}</p>
    <p v-once>{{ msg1 }}</p>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data () {
      return {
        msg: 'hello vue',
        msg1: 'hello world'
      }
    }
  }
</script>



<!--<template>-->
  <!--<el-container>-->
    <!--<el-header>-->
      <!--<el-menu-->
          <!--background-color="#242f42"-->
          <!--mode="horizontal">-->
        <!--<el-menu-item index="1">处理中心</el-menu-item>-->
        <!--<el-menu-item index="3">消息中心</el-menu-item>-->
        <!--<el-menu-item index="4">订单管理</el-menu-item>-->
      <!--</el-menu>-->
    <!--</el-header>-->
    <!--<el-container>-->
      <!--<el-aside width="200px">-->
        <!--<el-menu-->
          <!--default-active="1-1"-->
          <!--unique-opened="true"-->
          <!--background-color="#324157"-->
          <!--text-color="#a9b5c5"-->
          <!--active-text-color="#20a0ff"-->
          <!--class="el-menu-vertical-demo"-->
          <!--@open="handleOpen"-->
          <!--@close="handleClose">-->
          <!--<el-submenu index="1">-->
            <!--<template slot="title">-->
              <!--<i class="el-icon-location"></i>-->
              <!--<span>导航一</span>-->
            <!--</template>-->
            <!--<el-menu-item-group>-->
              <!--<template slot="title">分组一</template>-->
              <!--<el-menu-item index="1-1">选项1</el-menu-item>-->
              <!--<el-menu-item index="1-2">选项2</el-menu-item>-->
            <!--</el-menu-item-group>-->
            <!--<el-menu-item-group title="分组2">-->
              <!--<el-menu-item index="1-3">选项3</el-menu-item>-->
            <!--</el-menu-item-group>-->
            <!--<el-submenu index="1-4">-->
              <!--<template slot="title">选项4</template>-->
              <!--<el-menu-item index="1-4-1">选项1</el-menu-item>-->
            <!--</el-submenu>-->
          <!--</el-submenu>-->
          <!--<el-submenu index="2">-->
            <!--<template slot="title">-->
              <!--<i class="el-icon-location"></i>-->
              <!--<span>导航二</span>-->
            <!--</template>-->
            <!--<el-menu-item-group>-->
              <!--<template slot="title">分组一</template>-->
              <!--<el-menu-item index="1-1">选项1</el-menu-item>-->
              <!--<el-menu-item index="1-2">选项2</el-menu-item>-->
            <!--</el-menu-item-group>-->
            <!--<el-menu-item-group title="分组2">-->
              <!--<el-menu-item index="1-3">选项3</el-menu-item>-->
            <!--</el-menu-item-group>-->
            <!--<el-submenu index="1-4">-->
              <!--<template slot="title">选项4</template>-->
              <!--<el-menu-item index="1-4-1">选项1</el-menu-item>-->
            <!--</el-submenu>-->
          <!--</el-submenu>-->
          <!--<el-menu-item index="3">-->
            <!--<i class="el-icon-document"></i>-->
            <!--<span slot="title">导航三</span>-->
          <!--</el-menu-item>-->
          <!--<el-menu-item index="4">-->
            <!--<i class="el-icon-setting"></i>-->
            <!--<span slot="title">导航四</span>-->
          <!--</el-menu-item>-->
        <!--</el-menu>-->
      <!--</el-aside>-->

      <!--<el-main>主要</el-main>-->

    <!--</el-container>-->
  <!--</el-container>-->

<!--</template>-->

<!--<script>-->
  <!--export default {-->
    <!--methods: {-->
      <!--handleOpen(key, keyPath) {-->
        <!--console.log(key, keyPath);-->
      <!--},-->
      <!--handleClose(key, keyPath) {-->
        <!--console.log(key, keyPath);-->
      <!--}-->
    <!--}-->
  <!--}-->
<!--</script>-->

<!--<style>-->
  <!--.el-header {-->
    <!--background-color: #242f42;-->
    <!--color: #333;-->
    <!--text-align: center;-->
    <!--line-height: 60px;-->
  <!--}-->

  <!--.el-aside {-->
    <!--background-color: #D3DCE6;-->
    <!--color: #333;-->
    <!--text-align: center;-->
    <!--line-height: 200px;-->
  <!--}-->

  <!--.el-main {-->
    <!--background-color: #E9EEF3;-->
    <!--color: #333;-->
    <!--text-align: center;-->
    <!--line-height: 160px;-->
  <!--}-->

  <!--body > .el-container {-->
    <!--margin-bottom: 40px;-->
  <!--}-->
  <!--body {-->
    <!--margin: 0;-->
    <!--height: 100%;-->
  <!--}-->

<!--</style>-->
