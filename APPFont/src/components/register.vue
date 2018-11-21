<template>
  <div class="login">
    <el-container>
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
        <div class="welcome">欢迎注册IOTforFML开放平台！</div>
        <div class="panel-register">
          <div class="title">
            <p>用户注册</p>
          </div>
          <div class="part">
            <el-form :model="registerForm" ref="registerForm" status-icon :rules="rules">
              <el-form-item prop="username" :error="errorMsg">
                <el-input type="text" prefix-icon="el-icon-d-arrow-right" placeholder="请输入用户名"
                          v-model="registerForm.username"></el-input>
              </el-form-item>
              <el-form-item prop="password">
                <el-input type="password" prefix-icon="el-icon-d-arrow-right" placeholder="请输入密码"
                          v-model="registerForm.password"></el-input>
              </el-form-item>
              <el-form-item prop="password2">
                <el-input type="password" prefix-icon="el-icon-d-arrow-right" placeholder="请确认密码"
                          v-model="registerForm.password2"></el-input>
              </el-form-item>
              <el-form-item prop="email">
                <el-input type="email" prefix-icon="el-icon-d-arrow-right" placeholder="请输入你的邮箱"
                          v-model="registerForm.email"></el-input>
              </el-form-item>
              <el-form-item prop="verifycode">
                <el-input type="text" style="float: left;width: 340px" prefix-icon="el-icon-d-arrow-right"
                          placeholder="请输入验证码" v-model="registerForm.verifycode"></el-input>
                <div @click="refreshCode">
                  <s-identify :identifyCode="identifyCode"></s-identify>
                </div>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('registerForm')">立即注册</el-button>
                <el-button type="" @click="resetForm('registerForm')">再看一看</el-button>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </el-main>
    </el-container>
  </div>
</template>


<script>
  import SIdentify from './identify'

  export default {
    name: "Register",
    components: {SIdentify},
    data() {
      let checkName = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('用户名不能为空'));
        }
        else {
          callback();
        }
      };
      let checkPassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('密码不能为空'));
        } else {
          callback();
        }
      };
      let checkPassword2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        }
        setTimeout(() => {
          if (value !== this.registerForm.password) {
            callback(new Error('两次输入密码不一致!'));
          } else {
            callback();
          }
        }, 1000)
      };
      let checkEmail = (rule, value, callback) => {
        const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
        if (!value) {
          return callback(new Error("邮箱不能为空"));
        }
        setTimeout(() => {
          if (mailReg.test(value)) {
            callback()
          } else {
            callback(new Error("请输入正确的邮箱格式"))
          }
        }, 100)
      };
      let checkVerifyCode = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入验证码'));
        }
        setTimeout(() => {
          if (this.registerForm.verifycode !== this.identifyCode) {
            callback(new Error('验证码错误，请重新输入'));
          } else {
            callback();
          }
        }, 1500);

      };
      return {
        identifyCodes: "1234567890",
        identifyCode: "",
        errorMsg: "",
        checked: "",
        registerForm: {
          username: '',
          password: '',
          password2: '',
          email: '',
          verifycode: ''
        },
        rules: {
          username: [
            {validator: checkName}
          ],
          password: [
            {validator: checkPassword}
          ],
          password2: [
            {validator: checkPassword2}
          ],
          email: [
            {validator: checkEmail}
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
        this.errorMsg = "";
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$axios.post('/register',
                'username=' + this.registerForm.username +
                '&password=' + this.registerForm.password +
                '&email=' + this.registerForm.email).then(res => {
              if (res.data.code === 0) {
                this.$router.push('/developer')
              }
              else if (res.data.code === 2) {
                this.errorMsg = res.data.message;
                this.refreshCode()
              }
              else{
                this.$message.error('出错了！'+ res.data.message);
                this.refreshCode()
              }
            })
          } else {
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

  .panel-register {
    box-sizing: border-box;
    width: 560px;
    margin: 0 auto 35px;
    padding: 25px 0 25px;
    background-color: #fff;
    border-radius: 3px;
    box-shadow: 0 0 10px rgba(153, 153, 153, .15);
  }

  .panel-register .part {
    padding: 45px 50px 15px;
    border-top: 1px solid #E8EBEF;
    text-align: center;
  }

  .panel-register .title {
    width: 325px;
    margin: 0 auto;
    text-align: center;
  }

</style>
