# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish
# import time
#
# HOST = "123.207.87.193"
# PORT = 1883
# # def on_connect(client, userdata, flags, rc):
# #     print("Connected with result code "+str(rc))
# #     client.subscribe("test")
#
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+msg.payload.decode("utf-8"))
#
# if __name__ == '__main__':
#     client_id = 'python_test'
#     client = mqtt.Client()
#     # client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
#     # client.username_pw_set("admin", "123456")  # 必须设置，否则会返回「Connected with result code 4」
#     # client.on_connect = on_connect
#     # client.on_message = on_message
#     # client.connect(HOST, PORT, 60)
#     # client.publish("test", "你好 MQTT", qos=0, retain=False)  # 发布消息
#     client.connect("123.207.87.193", 1883, 60)
#     publish.single("test", "你好 MQTT", qos = 1,hostname=HOST,port=PORT, client_id=client_id,auth = {'username':"admin", 'password':"123456"})









#
# import paho.mqtt.client as mqtt
#
# def on_connect(client, userdata, flags, rc):
#     # print("Connected with result code " + str(rc))
#     # client.subscribe("inTopic")
#     client.subscribe('NodeMCU/test')
#     # client.subscribe("$SYS/brokers/emq@127.0.0.1/clients/#")
#
# def on_message(client, userdata, msg):
#     # print('\n'.join(['%s:%s' % item for item in msg.__dict__.items()]))
#     print(msg.topic + " " + str(msg.payload))
#
# def cal():
#     print('i am callback')
#
#
# client = mqtt.Client(client_id='System1',clean_session=True)
# client.username_pw_set('433580290', '123')  # 设置连接用户名
# client.on_connect = on_connect
# client.on_message = on_message
# # client.message_callback_add("outTopic", on_message)
#
# client.connect("123.207.87.193", 1883, 60)
# client.loop_forever()



#
# import time,datetime
# print(datetime.time)







import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import json
data = {

    "topic" : "$client/123456",
    "payload": "1",
    "qos": 0,
    "retain" : False,
    "client_id": "mqttjs_b4b9e8e2c3"
}
d = json.dumps(data)
auth = HTTPBasicAuth('admin', 'fml950826cs')
# auth = HTTPBasicAuth('123', '123')
r = requests.post(url="http://123.207.87.193:18083/api/v2/mqtt/publish", auth=auth,data=d)
print('kkk')
print(r.text)
