<template>
  <div>
    <div class="box">
      <div class="box-title">
        <label style="color: #999;font-size: 14px;padding-left: 30px">数据流个数：</label>
        <label style="font-size: 14px">{{streams.length}}</label>
      </div>
      <div class="device-search">
        <div class="show-search-input">
          <el-input v-model="input" placeholder="输入输入数据流名称" class="search-input"></el-input>
          <el-button type="primary" icon="el-icon-search" @click="search(input)">搜索</el-button>
          <el-button type="primary" icon="el-icon-ump-shuaxin" @click="reload">刷新</el-button>
          <el-button type="primary" round style="margin-right: 60px;float: right" @click="openForm1">添加数据流</el-button>
        </div>
      </div>
      <div class="box-table">
        <el-table :data="streams" style="width: 100%">
          <el-table-column
            label="数据流名称"
            prop="name"
            align="center">
          </el-table-column>
          <el-table-column
            label="所属设备ID"
            prop="dev_id"
            align="center">
          </el-table-column>
          <el-table-column
            label="所属设备名"
            prop="dev_name"
            align="center">
          </el-table-column>
          <el-table-column
            label="单位名称"
            prop="unit"
            align="center">
          </el-table-column>
          <el-table-column
            label="单位符号"
            prop="unit_symbol"
            align="center">
          </el-table-column>
          <el-table-column label="阈值设置" align="center">
            <el-table-column
              label="数值"
              prop="max"
              align="center">
            </el-table-column>
            <el-table-column
              label="判断类型"
              prop="trigger_type"
              align="center">
              <!--<template slot-scope="scope">-->
                <!--<span>{{ trigger_type[scope.row.min] }}</span>-->
                <!--&lt;!&ndash;<span>{{ scope.row.min }}</span>&ndash;&gt;-->
              <!--</template>-->
            </el-table-column>
          </el-table-column>
          <el-table-column
            label="是否开启触发器"
            prop="trigger"
            align="center">
          </el-table-column>
          <el-table-column
            label="QoS"
            prop="qos"
            align="center">
          </el-table-column>
          <el-table-column label="操作" align="center">
            <template slot-scope="scope">
              <el-tooltip content="编辑" placement="top">
                <i class="el-icon-ump-bianji1" @click="openForm(scope.row)"></i>
              </el-tooltip>
              <el-tooltip content="删除" placement="top">
                <i class="el-icon-ump-shanchu" @click="delStream(scope.row.dev_id,scope.row.name)"
                   style="padding-left:5px;"></i>
              </el-tooltip>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
    <!--修改数据流信息-->
    <div>
      <el-dialog title="修改信息" :visible.sync="dialogFormVisible" width="35%">
        <el-form v-model="streams_info">
          <el-form-item label="数据流名称" label-width="100px">
            <el-input v-model="streams_info.name" autocomplete="off" disabled=true></el-input>
          </el-form-item>
          <el-form-item label="单位名称" label-width="100px">
            <el-input v-model="streams_info.unit" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="单位符号" label-width="100px">
            <el-input v-model="streams_info.unit_symbol" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Qos设置" label-width="100px">
            <el-select v-model="streams_info.qos" placeholder="请选择">
              <el-option label="0" key="0" value=0></el-option>
              <el-option label="1" key="1" value=1></el-option>
              <el-option label="2" key="2" value=2></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="判断类型:" label-width="100px">
            <el-select v-model="streams_info.min">
              <el-option v-for="item in trigger_type"
                         :key="item.value"
                         :label="item.label"
                         :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="数值:" label-width="100px">
            <el-input-number v-model="streams_info.max"></el-input-number>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="updateStream">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <!--新建数据流-->
    <div>
      <el-dialog title="新建数据流" :visible.sync="dialogFormVisible1" width="35%">
        <el-form v-model="new_streams_info">
          <el-form-item label="数据流名称" label-width="100px">
            <el-input v-model="new_streams_info.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="单位名称" label-width="100px">
            <el-input v-model="new_streams_info.unit" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="单位符号" label-width="100px">
            <el-input v-model="new_streams_info.unit_symbol" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Qos设置" label-width="100px">
            <el-select v-model="new_streams_info.qos" placeholder="请选择">
              <el-option label="0" key="0" value=0></el-option>
              <el-option label="1" key="1" value=1></el-option>
              <el-option label="2" key="2" value=2></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="选择设备" label-width="100px">
            <el-select v-model="new_streams_info.dev_id" placeholder="请选择">
              <el-option
                v-for="item in dev_info"
                :key="item.id"
                :label="item.name"
                :value="item.id">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="判断类型" label-width="100px">
            <el-select v-model="new_streams_info.min">
              <el-option v-for="item in trigger_type"
              :key="item.value"
              :label="item.label"
              :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="数值" label-width="100px">
            <el-input-number v-model="new_streams_info.max"></el-input-number>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible1 = false">取 消</el-button>
          <el-button type="primary" @click="addStream">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
  import api from '../../axios'

  export default {
    name: "stream",
    data() {
      return {
        input: "",
        stream_num: 0,
        dialogFormVisible: false,
        dialogFormVisible1: false,
        get_info_status: true,
        streams: [],
        streams_info: {}, //修改之后的数据流
        new_streams_info: {}, //新数据流
        dev_info: [], //这里要获取设备信息，在新建数据流的时候需要用到
        trigger_type: [
          {
            value: 0,
            label:'无',
          },{
            value: 1,
            label:'<',
          },{
            value: 2,
            label:'<=',
          },{
            value: 3,
            label:'==',
          },{
            value: 4,
            label:'>',
          },{
            value: 5,
            label:'>=',
          },{
            value: 6,
            label:'change',
          },{
            value: 7,
            label:'inout',
          },

        ],

      }
    },
    created() {
      this.getStream();
      api.getDevice().then(res => {
        if (!res.data.code) {
          this.dev_info = res.data.data;
        }
        else {
          this.$message({
            message: '设备信息获取失败！可能有部分功能无法正常使用。',
            type: 'warning'
          });
        }
      }).catch(res => {
        this.$message({
          message: '设备信息获取失败！可能有部分功能无法正常使用。',
          type: 'warning'
        });
      });
    },
    methods: {
      //打开修改框
      openForm(info) {
        this.streams_info = info;
        this.dialogFormVisible = true;
      },
      // 打开新建窗口
      openForm1() {
        this.new_streams_info = {};
        this.dialogFormVisible1 = true;
      },
      // 修改数据
      updateStream() {
        this.dialogFormVisible = false;
        api.updateStream(this.streams_info).then((res) => {
          if (!res.data.code) {
            this.$notify({
              title: '修改成功',
              type: 'success'
            });
          }
          else {
            this.$notify.error({
              title: '修改失败',
              message: '数据流修改失败！请检查重试！'
            });
            //修改失败但是页面数据已经变了，暂且重新向服务器请求一次刷新一下数据
            this.getStream();
          }
        }).catch(res => {
          this.$notify.error({
            title: '修改失败',
            message: '数据流修改失败！请检查重试！'
          });
        });
      },
      //获取设备信息
      getStream() {
        api.getStream().then((res) => {
          if (!res.data.code) {
            this.streams = res.data.data;
            this.get_info_status = true;
          }
          else {
            this.get_info_status = false;
            this.$message.error('设备信息获取失败！');
          }
        }).catch(res => {
          this.get_info_status = false;
          this.$message.error('设备信息获取失败！');
        });
      },
      // 新增数据流
      addStream() {
        this.dialogFormVisible1 = false;
        api.addStream(this.new_streams_info).then((res) => {
          if (!res.data.code) {
            this.$notify({
              title: '添加成功',
              type: 'success'
            });
            this.reload();
          }
          else {
            this.$notify.error({
              title: '添加失败',
              message: '数据流信息有误！请检查重试！'
            });
            //修改失败但是页面数据已经变了，暂且重新向服务器请求一次刷新一下数据
            this.getStream();
          }
        }).catch(res => {
          this.$notify.error({
            title: '添加失败',
            message: '数据流信息有误！请检查重试！'
          });
        });
      },
      //刷新数据
      delStream(id, name) {
        this.$confirm('警告！此操作将永久删除该数据流所有信息,包括已经上传的数据, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          api.delStream(id, name).then((res) => {
            if (!res.data.code) {
              this.$message({
                type: 'success',
                message: '删除成功!'
              });
              // 重新获取设备信息
              this.getStream();
            }
            else {
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
      // 刷新
      reload() {
        this.getStream();
        if (this.get_info_status) {
          this.$message({
            type: 'success',
            message: '刷新成功！'
          });
        }
      },
      // 搜索
      search(name) {
        let l = this.streams.length;
        for (let i = 0; i < l; i++) {
          console.log(i);
          if (this.streams[i].name != name) {
            this.streams.pop(i - 1);
            // delete this.streams[i];
            // this.streams.slice(i,1);
            console.log(this.streams);
          }
        }
        console.log(this.streams);
      },
    }
  }
</script>

<style scoped>
  .box {
    min-width: 897px;
    margin: 50px 60px 10px;
    background-color: #FFF;
    min-height: 600px;
    border-radius: 5px;
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

  .box-table {
    text-align: center;
  }

  .el-form .el-input {
    width: 90%;
  }

</style>
