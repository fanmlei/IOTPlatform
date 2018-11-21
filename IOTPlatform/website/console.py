import requests,json
from requests.auth import HTTPBasicAuth


def send(data):
    """
    调用EMQ http接口发送消息
    :param data: 消息内容  dict
    :return: dict
    """
    try:
        data = json.dumps(data)
        auth = HTTPBasicAuth('admin', 'fml950826cs')  # basicAuth认证
        res = requests.post(url="http://123.207.87.193:18083/api/v2/mqtt/publish", auth=auth,data=data)
        # success: {"code": 0, "result": []}
        if res.status_code==200:
            return json.loads(res.text)
        else:
            return {"code": 1, "result": []}
    except Exception as e:
        return {"code": 1, "result": []}



# 测试
# data = {
#     "topic" : "$client/123456",
#     "payload": "0",
#     "qos": 0,
#     "retain" : False,
#     "client_id": "mqttjs_b4b9e8e2c3"
# }
# data={'topic': '$client/123456', 'payload': '1', 'qos': 0}
# print(send(data))