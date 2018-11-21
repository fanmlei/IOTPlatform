import Vue from 'vue'
import store from '../store/index.js'
import Router from 'vue-router'

//路由懒加载

const Home = resolve => {
  require.ensure(['../components/home/Home.vue'], () => {
    resolve(require('../components/home/Home.vue'));
  });
};

const Document = resolve => {
  require.ensure(['../components/home/document.vue'], () => {
    resolve(require('../components/home/document.vue'));
  });
};

const Introduce = resolve => {
  require.ensure(['../components/home/introduce.vue'], () => {
    resolve(require('../components/home/introduce.vue'));
  });
};

const Resource = resolve => {
  require.ensure(['../components/home/resource.vue'], () => {
    resolve(require('../components/home/resource.vue'));
  });
};

const Login = resolve => {
  require.ensure(['../components/login.vue'], () => {
    resolve(require('../components/login.vue'));
  });
};

const Register = resolve => {
  require.ensure(['../components/register.vue'], () => {
    resolve(require('../components/register'));
  });
};

const NotFound = resolve => {
  require.ensure(['../components/notFound.vue'], () => {
    resolve(require('../components/notFound.vue'));
  });
};

import Developer from '../components/developer/index'
import Dashboard from '../components/developer/dashboard'
import Charts from '../components/developer/charts'
import Devices from '../components/developer/device'
import Streams from '../components/developer/stream'
import Triggers from '../components/developer/trigger'
import Console from '../components/developer/console'
import test from '../components/test'

Vue.use(Router);

const router = new Router({
  mode:'history',
  routes: [
    {path: '/', redirect: {path: '/home/introduce'}},
    {path: '/home', redirect: {path: '/home/introduce'}},
    {path: '/developer', redirect: {path: '/developer/dashboard'}},
    {
      name: 'home',
      path: '/home',
      component: Home,
      children: [
        {name: 'introduce', path: 'introduce', component: Introduce},
        {name: 'document', path: 'document', component: Document},
        {name: 'resource', path: 'resource', component: Resource},
      ]
    },
    {
      name: 'developer',
      path: '/developer',
      component: Developer,
      meta: {
        requiresAuth: true
      },
      children: [
        {name: 'dashboard', path: 'dashboard', component: Dashboard,meta: {requiresAuth: true}},
        {name: 'charts', path: 'charts', component: Charts,meta: {requiresAuth: true}},
        {name: 'devices', path: 'devices', component: Devices,meta: {requiresAuth: true}},
        {name: 'streams', path: 'streams', component: Streams,meta: {requiresAuth: true}},
        {name: 'console', path: 'console', component: Console,meta: {requiresAuth: true}},
        {name: 'triggers', path: 'triggers', component: Triggers,meta: {requiresAuth: true}},
      ]
    },
    {name: 'login', path: '/login', component: Login},
    {name: 'register', path: '/register', component: Register},
    {name: 'test', path: '/test', component: test},
    {path: '*', component: NotFound}
  ]
});

router.beforeEach((to, from, next) => {
  //获取store里面的token
  let token = store.state.token;
  //判断要去的路由有没有requiresAuth
  if (to.meta.requiresAuth) {

    if (token) {
      next();
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}  // 将刚刚要去的路由path（却无权限）作为参数，方便登录成功后直接跳转到该路由
      });
    }

  } else {
    next();//如果无需token,那么随它去吧
  }
});
export default router;

