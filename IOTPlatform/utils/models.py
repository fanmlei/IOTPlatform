# pip install sqlacodegen
# sqlacodegen mysql+pymysql://root:fml950826cs@123.207.87.193:3306/IOTPlatform > models.py


# coding: utf-8
from sqlalchemy import Column, ForeignKey, Index, String
from sqlalchemy.dialects.mysql import DATETIME, INTEGER, LONGTEXT, SMALLINT, TINYINT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(80), nullable=False, unique=True)


class AuthUser(Base):
    __tablename__ = 'auth_user'

    id = Column(INTEGER(11), primary_key=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DATETIME(fsp=6))
    is_superuser = Column(TINYINT(1), nullable=False)
    username = Column(String(150), nullable=False, unique=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(TINYINT(1), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    date_joined = Column(DATETIME(fsp=6), nullable=False)


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        Index('django_content_type_app_label_model_76bd3d3b_uniq', 'app_label', 'model', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    app_label = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)


class DjangoMigration(Base):
    __tablename__ = 'django_migrations'

    id = Column(INTEGER(11), primary_key=True)
    app = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    applied = Column(DATETIME(fsp=6), nullable=False)


class DjangoSession(Base):
    __tablename__ = 'django_session'

    session_key = Column(String(40), primary_key=True)
    session_data = Column(LONGTEXT, nullable=False)
    expire_date = Column(DATETIME(fsp=6), nullable=False, index=True)


class WebsiteDatum(Base):
    __tablename__ = 'website_data'

    id = Column(INTEGER(11), primary_key=True)
    data = Column(String(10), nullable=False)
    date = Column(DATETIME(fsp=6), nullable=False)


class WebsiteDatastream(Base):
    __tablename__ = 'website_datastream'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(VARCHAR(32), nullable=False)
    min = Column(INTEGER(11))
    max = Column(INTEGER(11))
    qos = Column(INTEGER(11), nullable=False)
    unit = Column(VARCHAR(32))
    unit_symbol = Column(VARCHAR(32))
    trigger = Column(TINYINT(1), nullable=False)


class WebsiteDevice(Base):
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


class WebsiteUserinfo(Base):
    __tablename__ = 'website_userinfo'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(VARCHAR(32), nullable=False, unique=True)
    user_id = Column(INTEGER(11), nullable=False, unique=True)
    password = Column(VARCHAR(64), nullable=False)
    weixin_id = Column(VARCHAR(64), index=True)
    sex = Column(VARCHAR(16))
    birthday = Column(VARCHAR(64))
    tel = Column(VARCHAR(64))
    email = Column(VARCHAR(64))
    address = Column(VARCHAR(64))
    introduction = Column(VARCHAR(255))
    token = Column(VARCHAR(255))


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        Index('auth_permission_content_type_id_codename_01ab375a_uniq', 'content_type_id', 'codename', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id'), nullable=False)
    codename = Column(String(100), nullable=False)

    content_type = relationship('DjangoContentType')


class AuthUserGroup(Base):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        Index('auth_user_groups_user_id_group_id_94350c0c_uniq', 'user_id', 'group_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    user = relationship('AuthUser')


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'

    id = Column(INTEGER(11), primary_key=True)
    action_time = Column(DATETIME(fsp=6), nullable=False)
    object_id = Column(LONGTEXT)
    object_repr = Column(String(200), nullable=False)
    action_flag = Column(SMALLINT(5), nullable=False)
    change_message = Column(LONGTEXT, nullable=False)
    content_type_id = Column(ForeignKey('django_content_type.id'), index=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False, index=True)

    content_type = relationship('DjangoContentType')
    user = relationship('AuthUser')


class WebsiteDatastreamDatum(Base):
    __tablename__ = 'website_datastream_data'
    __table_args__ = (
        Index('website_datastream_data_datastream_id_data_id_3b3216eb_uniq', 'datastream_id', 'data_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    datastream_id = Column(ForeignKey('website_datastream.id'), nullable=False)
    data_id = Column(ForeignKey('website_data.id'), nullable=False, index=True)

    data = relationship('WebsiteDatum')
    datastream = relationship('WebsiteDatastream')


class WebsiteDeviceDevStream(Base):
    __tablename__ = 'website_device_dev_stream'
    __table_args__ = (
        Index('website_device_dev_stream_device_id_datastream_id_6d32e5c0_uniq', 'device_id', 'datastream_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    device_id = Column(ForeignKey('website_device.id'), nullable=False)
    datastream_id = Column(ForeignKey('website_datastream.id'), nullable=False, index=True)

    datastream = relationship('WebsiteDatastream')
    device = relationship('WebsiteDevice')


class WebsiteUserinfoDevice(Base):
    __tablename__ = 'website_userinfo_device'
    __table_args__ = (
        Index('website_userinfo_device_userinfo_id_device_id_e34001e8_uniq', 'userinfo_id', 'device_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    userinfo_id = Column(ForeignKey('website_userinfo.id'), nullable=False)
    device_id = Column(ForeignKey('website_device.id'), nullable=False, index=True)

    device = relationship('WebsiteDevice')
    userinfo = relationship('WebsiteUserinfo')


class AuthGroupPermission(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        Index('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'group_id', 'permission_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    group_id = Column(ForeignKey('auth_group.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    group = relationship('AuthGroup')
    permission = relationship('AuthPermission')


class AuthUserUserPermission(Base):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        Index('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq', 'user_id', 'permission_id', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('auth_user.id'), nullable=False)
    permission_id = Column(ForeignKey('auth_permission.id'), nullable=False, index=True)

    permission = relationship('AuthPermission')
    user = relationship('AuthUser')
