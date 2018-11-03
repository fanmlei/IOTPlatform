import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

HOST = "123.207.87.193"
PORT = 1883
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))

if __name__ == '__main__':
    client_id = 'python_mqtt'
    client = mqtt.Client()
    # client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
    # client.username_pw_set("admin", "123456")  # 必须设置，否则会返回「Connected with result code 4」
    # client.on_connect = on_connect
    # client.on_message = on_message
    # client.connect(HOST, PORT, 60)
    # client.publish("test", "你好 MQTT", qos=0, retain=False)  # 发布消息
    client.connect("123.207.87.193", 1883, 60)
    publish.single("test", "你好 MQTT", qos = 1,hostname=HOST,port=PORT, client_id=client_id,auth = {'username':"admin", 'password':"123456"})










# import paho.mqtt.client as mqtt
#
# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#
#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("intopic")
#
# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))
#
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
#
# client.connect("123.207.87.193", 1883, 60)
#
# # Blocking call that processes network traffic, dispatches callbacks and
# # handles reconnecting.
# # Other loop*() functions are available that give a threaded interface and a
# # manual interface.
# client.loop_forever()












# import requests
# from requests.auth import AuthBase
# from requests.auth import HTTPBasicAuth
#
# auth = HTTPBasicAuth('admin', 'fml950826cs')
# r = requests.get(url="http://123.207.87.193:18083/api/v2/management/nodes", auth=auth)
# # r = requests.get(url="http://123.207.87.193:18083/api/v2/nodes/emq@127.0.0.1/sessions/{mqttjs_69667e5069}", auth=auth)
# # print('kkk')
# print(r.text)
