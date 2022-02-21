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

router = APIRouter()
api = "/api/v1"


@router.get("/")
async def index():
    return {"message": "Hello World"}


def router_init(app):
    app.include_router(
        router,
        prefix=api,  # TODO 后面优化改成配置文件
        # tags=["apiv1"],
        # dependencies=[Depends(get_token_header)],
        responses={404: {"description": "Not found"}},
    )
    # 在api/v1基础上增加路径 tags是一个标识
    router.include_router(hello.router, tags=['hello'])
    router.include_router(user.router, tags=['user'])
