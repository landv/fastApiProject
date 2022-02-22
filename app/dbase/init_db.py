#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/22 上午11:39
# @Author  : landv
# @File    : init_db.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    : 初始化数据库
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.config import configs
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017803857459008
# 创建对象的基类:
Base = declarative_base()

# 数据库连接URL
SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}:{}/{}?charset=utf8".format(
    configs.MYSQL_USER,
    configs.MYSQL_PASSWORD,
    configs.MYSQL_SERVER,
    configs.MYSQL_PORT,
    configs.MYSQL_DB_NAME
)
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 初始化数据库连接
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# 创建DBSession类型:
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
