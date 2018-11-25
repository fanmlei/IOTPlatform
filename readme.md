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
  * axios                 0.18.0
  * echarts               4.2.0
  * element-ui            2.4.9
  * vue                   2.5.2
  * vue-router            3.0.1
  * vuex                  3.0.1
* 硬件：
  * pubsubclient
* 消息持久化服务：
  * paho-mqtt             1.4.0
  * SQLAlchemy            1.2.14
* 数据库：
  * MySQL                 5.7.0
* EMQ：
  * emqx                  2.3.0

### 项目整体架构
由EMQ服务器管理设备接入认证、消息分发，项目基本没有对EMQ服务做出修改，主要是对EMQ的权限认证、访问控制规则做了相应的变化，具体的修改方法请查看博客连载https://blog.csdn.net/FanMLei<br>

消息持久化服务使用paho-mqtt实现mqtt通信对注册数据流进行监听，并将收到的消息写入数据库中。服务独立于后端项目独运行方便日后的扩展，每隔一分钟会刷新订阅列表，防止新注册的数据流无法接收消息。<br>

后端提供设备信息、数据流信息、触发器信息、历史数据的管理接口以及网站的常规接口，接口使用rest Framework框架实现，同时通过API接口获取EMQ服务的状态信息和下发指令<br>

前端负责数据展示，界面使用elementUI，图表使用echarts进行渲染，通过axios获取数据内容<br>


### 项目结构简介
APPFont: 前端项目<br>
Hardware: 硬件连接测试代码<br>
IOTPlatform: 后端项目<br>
MQTT: 消息持久化服务<br>

### 联系方式
Email : 15638515832@163.com
QQ: 961160132
