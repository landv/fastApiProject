#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 上午10:28
# @Author  : landv
# @File    : __init__.py.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    : 路由初始化
from fastapi import APIRouter

from app.api.api_v1 import hello, user
from app.config.config import configs

router = APIRouter()


def router_init(app):
    app.include_router(
        router,
        prefix=configs.API_V1_STR,
        # tags=["app"],
        # dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )
    # 在api/v1基础上增加路径 tags是一个标识
    router.include_router(hello.router,
                          prefix="/hello",
                          tags=['hello'])
    router.include_router(user.router,
                          prefix="/user",
                          tags=['user'])
