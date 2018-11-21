<template>
  <div class="login">
    <el-container v-loading="loading" body=true>
      <el-header>
        <el-row>
          <el-col :span="3" :offset="3">
            <router-link to="/home/introduce">
              <img src="../assets/imgs/logo.png"/>
            </router-link>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
        <div class="welcome">欢迎使用IOTforFML开放平台！</div>
        <div class="panel-login">
          <div class="title">
            <p>用户登录</p>
          </div>
          <div class="part">
            <el-form :model="loginForm" ref="loginForm" status-icon :rules="rules">
              <el-form-item prop="username" :error="errorMsg1">
                <el-input type="text" prefix-icon="el-icon-d-arrow-right" placeholder="请输入用户名或者ID"
                          v-model="loginForm.username"></el-input>
              </el-form-item>
              <el-form-item prop="password" :error="errorMsg2">
                <el-input type="password" prefix-icon="el-icon-d-arrow-right" placeholder="请输入密码"
                          v-model="loginForm.password"></el-input>
              </el-form-item>
              <el-form-item prop="verifycode">
                <el-input type="text" style="float: left;width: 340px" prefix-icon="el-icon-d-arrow-right"
                          placeholder="请输入验证码" v-model="loginForm.verifycode"></el-input>
                <div @click="refreshCode">
                  <s-identify :identifyCode="identifyCode"></s-identify>
                </div>
              </el-form-item>
              <el-form-item>
                <el-checkbox :v-model="checked">自动登录</el-checkbox>
                <router-link to="/password">忘记密码？</router-link>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('loginForm')">立即登录</el-button>
                <el-button type="" @click="resetForm('loginForm')">取消</el-button>
              </el-form-item>
            </el-form>
          </div>
        </div>
        <p class="register">没有账户？现在就去注册吧→
          <router-link to="/register">立即注册</router-link>
        </p>
      </el-main>
    </el-container>
  </div>
</template>


<script>
  import api from '../axios.js'
  import SIdentify from "./identify";

  export default {
    name: "Login",
    components: {SIdentify},
    data() {
      let checkName = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入用户名或者ID'));
        }
        else {
          callback();
        }
      };
      let checkPassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          callback();
        }
      };
      let checkVerifyCode = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入验证码'));
        }
        setTimeout(() => {
          if (this.loginForm.verifycode !== this.identifyCode) {
            callback(new Error('验证码错误，请重新输入'));
          } else {
            callback();
          }
        }, 1500);

      };
      return {
        identifyCodes: "1234567890",
        identifyCode: "",
        errorMsg1: "",
        errorMsg2: "",
        checked: "true",
        loading: false,
        loginForm: {
          username: '',
          password: '',
          verifycode: ''
        },
        rules: {
          username: [
            {validator: checkName}
          ],
          password: [
            {validator: checkPassword}
          ],
          verifycode: [
            {validator: checkVerifyCode}
          ]
        }
      };
    },
    mounted() {
      this.identifyCode = "";
      this.makeCode(this.identifyCodes, 4);
    },
    methods: {
      //提交按钮
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) { //验证通过
            let opt = this.loginForm;
            this.loading= true;
            api.userLogin(opt)
              .then(({data}) => {     //解构赋值拿到data
                //账号不存在
                console.log(data);
                if (data.code === 3) {
                  this.$message.error('用户名错误');
                  return;
                }
                //账号存在
                if (!data.code) {
                  this.$message({
                    type: 'success',
                    message: '登录成功'
                  });
                  let token = data.data.token;
                  let username = data.username;
                  this.$store.dispatch('UserLogin', token);
                  this.$store.dispatch('UserName', username);
                  //如果用户手动输入"/"那么会跳转到这里来，即this.$route.query.redirect有参数
                  let redirectUrl = decodeURIComponent(this.$route.query.redirect || '/');
                  //跳转到指定的路由
                  this.$router.push({
                    path: redirectUrl
                  });
                } else {
                  this.$message.error('密码错误');
                }
              });
          } else {
            //验证不通过
            return false;
          }
        });
      },

      //取消按钮
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },

      //验证码相关
      randomNum(min, max) {
        return Math.floor(Math.random() * (max - min) + min);
      },
      refreshCode() {
        this.identifyCode = "";
        this.makeCode(this.identifyCodes, 4);
      },
      makeCode(o, l) {
        for (let i = 0; i < l; i++) {
          this.identifyCode += this.identifyCodes[
            this.randomNum(0, this.identifyCodes.length)
            ];
        }
      }
    },
  }
</script>


<style scoped>
  .el-main {
    background-color: #f4f5f6;
    height: 100%;
    padding: 0;
  }

  .el-form-item__content .el-checkbox {
    float: left;
  }

  .el-form-item__content a {
    float: right;
    text-decoration: none;
  }

  .welcome {
    text-align: center;
    font-size: 16px;
    color: #8F959B;
    margin: 10px 0 25px;
  }

  .panel-login {
    box-sizing: border-box;
    width: 560px;
    margin: 0 auto 35px;
    padding: 25px 0 25px;
    background-color: #fff;
    border-radius: 3px;
    box-shadow: 0 0 10px rgba(153, 153, 153, .15);
  }

  .panel-login .part {
    padding: 45px 50px 15px;
    border-top: 1px solid #E8EBEF;
    text-align: center;
  }

  .panel-login .title {
    width: 325px;
    margin: 0 auto;
    text-align: center;
  }

  .register {
    text-align: center;
    color: #393E4C;
    font-size: 14px;
    padding-bottom: 35px;
  }
</style>
