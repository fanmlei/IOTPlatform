from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *              # 导入生成的model


class DB(object):
    def __init__(self):
        engine = create_engine('mysql+pymysql://root:fml950826cs@123.207.87.193:3306/IOTPlatform')
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def update_dev_stus(self, device_id, status):
        """
        更改设备状态
        :param device_id: 设备ID
        :param status: 状态
        :return: None
        """
        try:
            self.session.query(WebsiteDevice).filter(WebsiteDevice.device_id==device_id).update({WebsiteDevice.dev_status:status})
            self.session.flush()
            self.session.commit()
            return True
        except Exception as e:
            return False



# db = DB()
# db.update_dev_stus(123456,0)