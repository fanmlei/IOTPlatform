from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *  # 导入生成的model

from datetime import datetime


class DB(object):
    def __init__(self, name, password, host, port, dbname):
        # 初始化的过程中直接连接数据库
        engine = create_engine('mysql+pymysql://' + name + ':' + password + '@' + host + ':' + port + '/' + dbname)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def reconnect(self):
        """"断开重连"""
        self.session = self.Session()

    def update_dev_stus(self, device_id, status):
        """
        更改设备状态
        :param device_id: 设备ID
        :param status: 状态
        :return: True
        """
        try:
            self.session.query(Device).filter(Device.device_id == device_id).update(
                {Device.dev_status: status})
            self.session.flush()
            self.session.commit()
            return True
        except Exception as e:
            self.reconnect()

    def write_data(self, device_id, dev_stream, data):
        """
        写入数据
        :param device_id: 设备ID
        :param dev_stream: 数据流名称
        :param data: 数据
        :return: True
        """
        try:
            new_data = Data(data=data,date=datetime.now())
            device_obj = self.session.query(Device).filter(Device.device_id==device_id).first()
            if device_obj:
                for i in device_obj.stream:
                    if i.name == dev_stream:
                        i.data.append(new_data)
            self.session.flush()
            self.session.commit()
            return True
        except Exception as e:
            self.reconnect()


    def get_subscribe(self):
        """
        获取需要订阅的主题名
        :return: list
        """
        try:
            subscribe_list = []
            devive_objs = self.session.query(Device).all()
            for i in devive_objs:
                for j in i.stream:
                    subscribe_list.append([str(i.device_id) + '/' + j.name, j.qos])
            return subscribe_list
        except Exception as e:
            self.reconnect()




# db = DB('root', 'fml950826cs','123.207.87.193','3306','IOTPlatform')

# db.update_dev_stus(123456,1)
# db.write_data('123456', 'temp1', '213213123')
# db.update_dev_stus('123456',1)

# print(db.get_subscribe())
