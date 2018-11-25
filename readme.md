### 项目地址
http://www.iotforfml.cn
### 项目简介
此项目使用基于MQTT协议，采用EMQ消息服务器实现MQTT通信功能。设备接入需完成auth认证，如果需要对消息进行持久化处理还需要在后台注册你的设备和设备流信息，除此之外还可用于组件自己的网络，自定义主题收发消息即可。在后台可直接对已注册的设备发送指令，默认发送主题为$system/clientID，也可自定义发送主题（系统主题除外）。后台提供对设备、数据流、触发器的管理、查看历史上传数据、下发指令等功能。
### 开发环境
* 后端：
  * Django                2.1.2
  * django-cors-headers   2.4.0
  * djangorestframework   3.9.0
  * requests              2.20.0
  * PyMySQL               0.9.2
* 前端：
  * axios             0.18.0
  * echarts           4.2.0
  * element-ui        2.4.9
  * vue               2.5.2
  * vue-router        3.0.1
  * vuex              3.0.1
* 硬件：
  * pubsubclient
* 消息持久化服务：
  * paho-mqtt             1.4.0
  * SQLAlchemy            1.2.14

### 项目结构简介
APPFont: 前端项目
Hardware: 硬件连接测试代码
IOTPlatform: 后端项目
MQTT: 消息持久化服务
消息持久化通过系统客户端进行订阅消息主题接收客户端消息，同时写入MySQL数据库中。后台又Django搭建，前端使用Vue编写
