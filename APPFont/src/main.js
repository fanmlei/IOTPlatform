// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
//引入路由
import router from './router'

//引入elementUI
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
//引入图标
import './assets/icon/iconfont.css'
import SIdentify from './components/identify'
Vue.use(SIdentify);

//安装插件
Vue.use(ElementUI);

//引入axios
// import Axios from 'axios'
// //设置全局URL
// Axios.defaults.baseURL = 'http://127.0.0.1:8000/';
// Axios.defaults.headers.common["Authorization"] = '9a14fb9da6d2ffbf1d0e663d401e201b';
// // Axios.defaults.headers.common["Authorization"] = '7a88e6d7177a1360b06a3a437079c34d';
// Axios.defaults.headers.post['Content-Type']='application/x-www-form-urlencoded';
// Vue.prototype.$axios = Axios;




import store from './store'





//引入echarts
import echarts from 'echarts'
Vue.prototype.$echarts = echarts;


// router.beforeEach((to, from, next) => {
//   next()
// });

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
