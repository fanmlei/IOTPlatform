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


import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('admin', 'fml950826cs')
# r = requests.get(url="http://123.207.87.193:18083/api/v2/management/nodes", auth=auth)
r = requests.get(url="http://123.207.87.193:18083/api/v2/nodes/emq@127.0.0.1/sessions/{mqttjs_69667e5069}", auth=auth)
# print('kkk')
print(r.text)
