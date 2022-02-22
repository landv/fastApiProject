#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/22 上午10:24
# @Author  : landv
# @File    : database.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    :

# mysql数据库url
import redis


# 数据库迁移配置
TORTOISE_ORM = {
    "connections": {"default": SQLALCHEMY_DATABASE_URL},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.models.model"],
            # 须添加“aerich.models” 后者“models”是上述models.py文件的路径
            "default_connection": "default",
        },
    },
}

pool = redis.ConnectionPool(
    host=configs.REDIS_HOST,
    port=configs.REDIS_PORT,
    # password=configs.REDIS_PASSWORD,
    db=configs.REDIS_DB,
)
redis_session = redis.Redis(connection_pool=pool)
