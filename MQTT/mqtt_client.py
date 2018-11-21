import paho.mqtt.client as client
from database import DB
import threading


class MqClient(object):
    def __init__(self, client_id, username, password):
        self.client = client.Client(client_id=client_id,
                                    clean_session=False)  # 初始化,clean_session为false的时候EMQ会保存订阅状态，可以不再次订阅
        self.client.username_pw_set(username, password)  # 设置连接用户名
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self._client_status = False  # 连接状态
        self._cloop = None
        self._connect()
        self.db = DB('root', 'fml950826cs', '123.207.87.193', '3306', 'IOTPlatform')

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

        # 读取数据库中所有的已经注册过的topic并且订阅
        sub_list = self.db.get_subscribe()
        # 防止没有获取到订阅列表
        while not sub_list:
            sub_list = self.db.get_subscribe()
        for i in sub_list:
            print(i[0],i[1])
            self.client.subscribe(i[0], i[1])
        # 修改客户端状态
        if rc == 0:
            self._client_status = True

    def on_message(self, client, userdata, msg):
        topic = msg.topic.split('/')
        client_id = topic[0]
        # 系统主题
        if client_id == '$SYS':
            status = 1 if topic[-1] == 'connected' else 0
            device_id = topic[-2]
            while not self.db.update_dev_stus(device_id, status):
                pass
        # 设备消息
        else:
            stream = topic[1]
            data = msg.payload.decode()
            while not self.db.write_data(client_id, stream, data):
                pass





c = MqClient('System', '123', '123')
while True:
    pass