#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 上午10:29
# @Author  : landv
# @File    : __init__.py.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    : 中间件初始化
from starlette.middleware.cors import CORSMiddleware

# 指定允许跨域请求的url
origins = [
    "*"
]


def middleware_init(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
