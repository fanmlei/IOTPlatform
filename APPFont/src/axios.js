import axios from 'axios'
import store from './store'
import router from './router'

//设置全局axios默认值
// axios.defaults.timeout = 5000; //5000的超时验证
// axios.defaults.baseURL = 'http://127.0.0.1:8000/';
axios.defaults.baseURL = 'http://123.207.87.193:8000/';
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';

//创建一个axios实例
const instance = axios.create();
instance.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';
// axios.defaults.baseURL = 'http://127.0.0.1:8000/';
axios.interceptors.request.use = instance.interceptors.request.use;

//request拦截器
instance.interceptors.request.use(
  config => {
    //每次发送请求之前检测都vuex存有token,那么都要放在请求头发送给服务器
    if (store.state.token) {
      config.headers.Authorization = `${store.state.token}`;
    }
    return config;
  },
  err => {
    return Promise.reject(err);
  }
);
//respone拦截器
instance.interceptors.response.use(
  response => {
    return response;
  },
  error => { //默认除了2XX之外的都是错误的，就会走这里
    if (error.response) {
      switch (error.response.status) {
        case 401:
          store.dispatch('UserLogout'); //可能是token过期，清除它
          router.replace({ //跳转到登录页面
            path: 'login',
            query: {redirect: router.currentRoute.fullPath} // 将跳转的路由path作为参数，登录成功后跳转到该路由
          });
      }
    }
    return Promise.reject(error.response);
  }
);

export default {
  //用户注册
  userRegister(data) {
    return instance.post('/register', data);
  },
  //用户登录
  userLogin(data) {
    return instance.post('/login', data);
  },
  //获取用户
  getUser() {
    return instance.get('/api/user');
  },
  //获取概览页面数据
  dashboard() {
    return instance.get('/dashboard');
  },
  //获取历史数据
  charts() {
    return instance.get('/charts');
  },
  // 获取设备信息
  getDevice() {
    return instance.get('/devices');
  },
  // 删除设备
  delDevice(id,apiKey) {
    return instance.delete('/devices', {data:{id:id,apiKey:apiKey}});
  },
  // 更新设备信息
  updateDevice(data) {
    return instance.put('/devices', data)
  },
  // 新增设备
  addDevice(data) {
    return instance.post('/devices', data);
  },
  updateStream(data) {
    return instance.put('/streams', data)
  },
  addStream(data) {
    return instance.post('/streams', data);
  },
  delStream(id,name) {
    return instance.delete('/streams', {data:{dev_id:id,name:name}});
  },
  getStream(){
    return instance.get('/streams');
  },
  publish(data){
    return instance.post('/console', data)
  },
  getTrigger(){
    return instance.get('/triggers')
  }
}
