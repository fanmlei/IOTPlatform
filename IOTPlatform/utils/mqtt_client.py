import paho.mqtt.client as client
import threading
from database import DB

class MqClient(object):
    def __init__(self, client_id, username, password):
        self.client = client.Client(client_id=client_id,
                                    clean_session=True)  # 初始化,clean_session为false的时候EMQ会保存订阅状态，可以不再次订阅
        self.client.username_pw_set(username, password)  # 设置连接用户名
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self._client_status = False  # 连接状态
        self._cloop = None
        self._connect()  # 实例化会自动连接
        self.db = DB()

    def _connect(self, host="123.207.87.193", port=1883, keepalive=60):
        """连接服务器"""
        self.client.connect_async(host, port, keepalive)
        # self.client.loop_forever()
        # 开启线程执行
        self._cloop = threading.Thread(target=self.client.loop_start())
        self._cloop.start()

    def on_connect(self, client, userdata, flags, rc):
        """连接成功的回调函数"""
        # 订阅上下线消息
        self.client.subscribe("$SYS/brokers/emq@127.0.0.1/clients/#")
        # 修改客户端状态
        if rc == 0:
            self._client_status = True

    def init_sub(self):

        # 读取数据库中所有的已经注册过的topic并且订阅
        # for i in models.Device.objects.all():
        #     for j in i.dev_stream.all():
        #         self.client.subscribe(str(i.device_id) + '/' + j.name, j.qos)
        pass

    def on_message(self,client, userdata, msg):
        topic = msg.topic.split('/')
        client = topic[0]
        # 系统主题
        if client=='$SYS':
            status = 1 if topic[-1] == 'connected' else 0
            device_id = topic[-2]
            print(status,device_id)
            # 修改设备在线状态
            print(self.db.update_dev_stus(device_id, status))
            # print(status,id)
            # print(models.Device.objects.filter(device_id=id).update(dev_status=status))

        # else:
        #     stream = topic[1]
        #     data = msg.payload.decode()
        #     # print(client_id,data_stream,data)
        #     # 接收订阅信息写入到数据库中
        #     models.DataStream.objects.filter(device__device_id=client).filter(name=stream).first().data.add(
        #         models.Data.objects.create(data=data))
        # pass

c = MqClient('System', '123', '123')
while True:
    pass

