#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 上午9:51
# @Author  : landv
# @File    : mian.py.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    :
from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.logs import log_init
from app.middleware import middleware_init
from app.routers import router_init


async def write_log(api=None, msg=None, user='root'):
    with open("log.log", mode="a", encoding='utf-8') as log:
        now = datetime.now()
        log.write(f"时间：{now}    API调用事件：{api}    用户：{user}    消息：{msg}\n")


async def start_event():
    await write_log(msg='系统启动')


async def shutdown_event():
    await write_log(msg='系统关闭')


lapp = FastAPI(title="landv_API",
               description="landv平台模块接口文档",
               version="1.0.0",
               on_startup=[start_event],
               on_shutdown=[shutdown_event],
               redoc_url=None,  # 禁止显示redoc文档
               # docs_url=None,  # 禁止显示swagger文档
               # openapi_url=None,  # 禁止显示openapi.json
               )


# 路径请求错误，不返回信息
# https://fastapi.tiangolo.com/tutorial/handling-errors/
@lapp.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(
        # str(exc.detail),
        status_code=exc.status_code)


# 请求验证错误，不返回信息
@lapp.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(
        # str(exc),
        status_code=400)


# 初始化日志
log_init()
#
# # 加载配置
# conf_init(app)
#
# 初始化路由配置
router_init(lapp)
#
# 初始化中间件
middleware_init(lapp)

#
# # 建表
# db_init(app)
if __name__ == '__main__':
    uvicorn.run(
        # https://www.cxymm.net/article/qq_43994782/119031998 好吧，骚操作.
        # https://www.uvicorn.org/deployment/
        app='main:lapp',
        # app=lapp,
        # app=app,
        host='0.0.0.0',
        port=8001,
        debug=False,
        # 开发模式
        reload=True,
        # 修改项目运行参数，即reload改为False 用于打包
        # reload=False,
        # workers=1
    )
