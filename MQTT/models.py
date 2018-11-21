# sqlacodegen mysql+pymysql://root:fml950826cs@123.207.87.193:3306/IOTPlatform > models.py
#

# coding: utf-8
from sqlalchemy import Column, ForeignKey, Index, String,Table,Integer
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, LONGTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

stream_data = Table(
    'website_datastream_data', Base.metadata,
    Column('datastream_id', Integer, ForeignKey('website_datastream.id')),
    Column('data_id', Integer, ForeignKey('website_data.id'))
)

device_stream = Table(
    'website_device_dev_stream', Base.metadata,
    Column('device_id', Integer, ForeignKey('website_device.id')),
    Column('datastream_id', Integer, ForeignKey('website_datastream.id'))
)

class Data(Base):
    __tablename__ = 'website_data'
    id = Column(INTEGER(11), primary_key=True)
    data = Column(String(10), nullable=False)
    date = Column(DATETIME(fsp=6), nullable=False)

class Stream(Base):
    __tablename__ = 'website_datastream'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(32), nullable=False)
    min = Column(INTEGER(11))
    max = Column(INTEGER(11))
    qos = Column(INTEGER(11), nullable=False)
    unit = Column(VARCHAR(32))
    unit_symbol = Column(VARCHAR(32))
    trigger = Column(TINYINT(1), nullable=False)
    data = relationship('Data',  secondary=stream_data)

class Device(Base):
    __tablename__ = 'website_device'

    id = Column(INTEGER(11), primary_key=True)
    device_id = Column(INTEGER(11), nullable=False, unique=True)
    device_key = Column(String(32))
    device_name = Column(VARCHAR(32), nullable=False)
    dev_status = Column(TINYINT(1), nullable=False)
    apiKey = Column(String(32))
    date = Column(DATETIME(fsp=6), nullable=False)
    dev_introduce = Column(LONGTEXT)
    tag = Column(VARCHAR(32))
    stream = relationship('Stream',  secondary=device_stream)

# class WebsiteData(Base):
#     __tablename__ = 'website_data'
#
#     id = Column(INTEGER(11), primary_key=True)
#     data = Column(String(10), nullable=False)
#     date = Column(DATETIME(fsp=6), nullable=False)


# class WebsiteDatastream(Base):
#     __tablename__ = 'website_datastream'
#
#     id = Column(INTEGER(11), primary_key=True)
#     name = Column(VARCHAR(32), nullable=False)
#     min = Column(INTEGER(11))
#     max = Column(INTEGER(11))
#     qos = Column(INTEGER(11), nullable=False)
#     unit = Column(VARCHAR(32))
#     unit_symbol = Column(VARCHAR(32))
#     trigger = Column(TINYINT(1), nullable=False)


# class WebsiteDevice(Base):
#     __tablename__ = 'website_device'
#
#     id = Column(INTEGER(11), primary_key=True)
#     device_id = Column(INTEGER(11), nullable=False, unique=True)
#     device_key = Column(String(32))
#     device_name = Column(VARCHAR(32), nullable=False)
#     dev_status = Column(TINYINT(1), nullable=False)
#     apiKey = Column(String(32))
#     date = Column(DATETIME(fsp=6), nullable=False)
#     dev_introduce = Column(LONGTEXT)
#     tag = Column(VARCHAR(32))


# class WebsiteUserinfo(Base):
#     __tablename__ = 'website_userinfo'
#
#     id = Column(INTEGER(11), primary_key=True)
#     username = Column(VARCHAR(32), nullable=False, unique=True)
#     user_id = Column(INTEGER(11), nullable=False, unique=True)
#     password = Column(VARCHAR(64), nullable=False)
#     weixin_id = Column(VARCHAR(64), index=True)
#     sex = Column(VARCHAR(16))
#     birthday = Column(VARCHAR(64))
#     tel = Column(VARCHAR(64))
#     email = Column(VARCHAR(64))
#     address = Column(VARCHAR(64))
#     introduction = Column(VARCHAR(255))
#     token = Column(VARCHAR(255))


# class WebsiteDatastreamData(Base):
#     __tablename__ = 'website_datastream_data'
#     __table_args__ = (
#         Index('website_datastream_data_datastream_id_data_id_3b3216eb_uniq', 'datastream_id', 'data_id', unique=True),
#     )
#
#     id = Column(INTEGER(11), primary_key=True)
#     datastream_id = Column(ForeignKey('website_datastream.id'), nullable=False)
#     data_id = Column(ForeignKey('website_data.id'), nullable=False, index=True)
#
#     data = relationship('WebsiteData')
#     datastream = relationship('WebsiteDatastream')


# class WebsiteDeviceDevStream(Base):
#     __tablename__ = 'website_device_dev_stream'
#     __table_args__ = (
#         Index('website_device_dev_stream_device_id_datastream_id_6d32e5c0_uniq', 'device_id', 'datastream_id', unique=True),
#     )
#
#     id = Column(INTEGER(11), primary_key=True)
#     device_id = Column(ForeignKey('website_device.id'), nullable=False)
#     datastream_id = Column(ForeignKey('website_datastream.id'), nullable=False, index=True)
#
#     datastream = relationship('WebsiteDatastream')
#     device = relationship('WebsiteDevice')


# class WebsiteUserinfoDevice(Base):
#     __tablename__ = 'website_userinfo_device'
#     __table_args__ = (
#         Index('website_userinfo_device_userinfo_id_device_id_e34001e8_uniq', 'userinfo_id', 'device_id', unique=True),
#     )
#
#     id = Column(INTEGER(11), primary_key=True)
#     userinfo_id = Column(ForeignKey('website_userinfo.id'), nullable=False)
#     device_id = Column(ForeignKey('website_device.id'), nullable=False, index=True)
#
#     device = relationship('WebsiteDevice')
#     userinfo = relationship('WebsiteUserinfo')
