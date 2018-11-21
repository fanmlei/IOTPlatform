<template>
  <div>
    <div class="box">
      <div class="box-title">
        <label style="color: #999;font-size: 14px;padding-left: 30px">设备数量：</label>
        <label style="font-size: 14px">{{devices.length}}</label>
      </div>
      <div class="device-search">
        <div class="show-search-input">
          <el-input v-model="input" placeholder="输入设备ID或者设备名称" class="search-input"></el-input>
          <el-button type="primary" icon="el-icon-search">搜索</el-button>
          <el-button type="primary" icon="el-icon-ump-shuaxin" @click="reload">刷新</el-button>
          <el-button type="primary" round style="margin-right: 60px;float: right" @click="openForm1">添加设备</el-button>
        </div>
      </div>
      <div class="box-dev">
        <el-table
          :data="devices"
          style="width: 100%">
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="设备ID">
                  <span>{{ props.row.id }}</span>
                </el-form-item>
                <el-form-item label="设备名称">
                  <span>{{ props.row.name }}</span>
                </el-form-item>
                <el-form-item label="设备状态">
                  <i :class=" props.row.status ? 'el-icon-ump-zaixian' : 'el-icon-ump-lixian1'"
                     :style="props.row.status ? 'color: #2ea1f8' : 'color: #ff0000'"></i>
                  <span :style="props.row.status ? 'color: #2ea1f8' : 'color: #ff0000'">{{ props.row.status ?'在线' : '离线' }}</span>
                </el-form-item>
                <el-form-item label="创建时间">
                  <span>{{ props.row.create_time }}</span>
                </el-form-item>
                <el-form-item label="设备简介">
                  <span>{{ props.row.introduce }}</span>
                </el-form-item>
                <el-form-item label="鉴权信息">
                  <span>{{ props.row.APIkey }}</span>
                </el-form-item>
                <el-form-item label="设备标签">
                  <div v-if="props.row.tag">
                    <el-tag>{{props.row.tag}}</el-tag>
                  </div>
                  <div v-else>
                    <span>无</span>
                  </div>
                </el-form-item>
                <el-form-item label="数据流个数">
                  <span>{{ props.row.stream_num }}</span>
                </el-form-item>
                <div style="margin-top: 20px">
                  <el-button type="primary" @click="openForm(props.row)">编辑设备信息</el-button>
                  <el-button type="danger" @click="delDevice(props.row.id,props.row.APIkey)">删除设备</el-button>
                </div>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column
            label="设备ID"
            prop="id">
          </el-table-column>
          <el-table-column
            label="设备名称"
            prop="name">
          </el-table-column>
          <el-table-column
            label="设备状态"
            prop='status'>
            <template slot-scope="scope">
              <i :class=" scope.row.status ? 'el-icon-ump-zaixian' : 'el-icon-ump-lixian1'"
                 :style="scope.row.status ? 'color: #2ea1f8' : 'color: #ff0000'"></i>
              <span :style="scope.row.status ? 'color: #2ea1f8' : 'color: #ff0000'">
                {{ scope.row.status ?'在线' : '离线' }}
              </span>
            </template>
          </el-table-column>
          <el-table-column
            label="创建时间"
            prop="create_time">
          </el-table-column>
          <el-table-column
            label="设备标签"
            prop="tag">
            <template slot-scope="scope">
              <div v-if="scope.row.tag">
                <el-tag>{{scope.row.tag}}</el-tag>
              </div>
              <div v-else>
                <span>无</span>
              </div>
            </template>
          </el-table-column>

        </el-table>
      </div>
    </div>
    <!--修改设备信息-->
    <div>
      <el-dialog title="修改设备信息" :visible.sync="dialogFormVisible">
        <el-form v-model="new_dev_info">
          <el-form-item label="设备名称" :label-width="formLabelWidth" >
            <el-input v-model="new_dev_info.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="设备简介" :label-width="formLabelWidth">
            <el-input type="textarea" autosize placeholder="请输入内容" v-model="new_dev_info.introduce"></el-input>
          </el-form-item>
          <el-form-item label="设备标签" :label-width="formLabelWidth">
            <el-input v-model="new_dev_info.tag" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="updateDevice">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <!--新建设备-->
    <div>
      <el-dialog title="新建设备" :visible.sync="dialogFormVisible1">
        <el-form v-model="dev_info">
          <el-form-item label="设备名称" :label-width="formLabelWidth" >
            <el-input v-model="dev_info.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="设备简介" :label-width="formLabelWidth">
            <el-input type="textarea" autosize placeholder="请输入内容" v-model="dev_info.introduce"></el-input>
          </el-form-item>
          <el-form-item label="设备标签" :label-width="formLabelWidth">
            <el-input v-model="dev_info.tag" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible1 = false">取 消</el-button>
          <el-button type="primary" @click="addDevice">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
  import api from '../../axios.js'

  export default {
    name: "device",
    data() {
      return {
        input: "",   //搜索框
        devices: [],  // 后台获取到的设备信息
        dialogFormVisible: false,  //修改框显示状态
        dialogFormVisible1: false,  //新建设备显示状态
        new_dev_info: {},   //修改框的数据
        dev_info: {},    // 新建框数据
        formLabelWidth: '120px',
        get_info_status: true  //获取设备信息的状态
      }
    },
    created() {
      this.getDevice();
    },
    methods: {
      //打开修改框
      openForm(info) {
        this.dialogFormVisible = true;
        this.new_dev_info = {}; //重置防止前一个造成影响
        this.new_dev_info = info;  //填充默认信息
      },
      // 打开新建窗口
      openForm1(){
        this.dev_info = {};
        this.dialogFormVisible1 = true;
      },
      // 修改设备信息
      updateDevice() {
        this.dialogFormVisible = false;
        //向服务器发送新的设备信息
        api.updateDevice(this.new_dev_info).then((res) => {
          if(!res.data.code){
            this.$notify({
              title: '修改成功',
              type: 'success'
            });
            this.reload();
          }
          else{
            this.$notify.error({
              title: '修改失败',
              message: '设备信息修改失败！请检查重试！'
            });
            //修改失败但是页面数据已经变了，暂且重新向服务器请求一次刷新一下数据
            this.getDevice();
          }
        }).catch(res=>{
          this.$notify.error({
            title: '修改失败',
            message: '设备信息修改失败！请检查重试！'
          });
        });
      },
      // 删除设备
      delDevice(id, apiKey) {
        this.$confirm('警告！此操作将永久删除该设备所有信息,包括已经上传的数据, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          api.delDevice(id, apiKey).then((res)=>{
            if(!res.data.code){
              this.$message({
                type: 'success',
                message: '删除成功!'
              });
              // 重新获取设备信息
              this.getDevice();
            }
            else{
              this.$notify.error({
                title: '删除失败',
                message: res.data.message,
              });
            }
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      // 新建设备
      addDevice(){
        this.dialogFormVisible1=false; //关闭弹窗
        api.addDevice(this.dev_info).then((res) => {
          console.log(res.data);
          if(!res.data.code){
            this.$notify({
              title: '创建成功',
              type: 'success'
            });
            this.getDevice();
          }
          else{
            this.$notify.error({
              title: '创建失败',
              message: '请检查重试！'
            });

          }
        });

      },
      //获取设备信息
      getDevice(){
        api.getDevice().then((res) => {
          if(!res.data.code){
            this.devices = res.data.data;
            this.get_info_status = true;
          }
          else{
            this.get_info_status = false;
            this.$message.error('设备信息获取失败！');
          }
        }).catch(res=>{
          this.get_info_status = false;
          this.$message.error('设备信息获取失败！');
        });
      },
      // 刷新
      reload(){
        this.getDevice();
        if(this.get_info_status){
          this.$message({
            type: 'success',
            message: '刷新成功！'
          });
        }
      }
    }
  }
</script>

<style scoped>
  .box {
    min-width: 897px;
    margin: 50px 60px 0;
    background-color: #FFF;
    min-height: 600px;
    border-radius:5px;
  }

  .box-title {
    padding-bottom: 10px;
    padding-top: 10px;
    border-bottom: 1px solid #dbe1e4;
  }

  .device-search {
    height: 76px;
    min-width: 855px;
    padding-top: 18px;
    border-bottom: 1px solid #dbe1e4;
  }

  .search-input {
    width: 400px;
    padding-left: 20px;
    height: 40px;
  }

  .box-dev {
    padding: 10px 20px 0;
  }

  .demo-table-expand {
    font-size: 0;
  }

  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }

  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
