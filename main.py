#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 上午9:51
# @Author  : landv
# @File    : mian.py.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    :

# 打包命令
# https://blog.csdn.net/weixin_41916986/article/details/122342035
# http://kmanong.top/kmn/qxw/form/article?id=11512&cate=56
# http://mrdoc.zmister.com/project-53/doc-1389/
# nuitka3 ./main.py --include-plugin-directory=./app --output-dir=./build -o ./build/main
# https://nuitka.net/doc/user-manual.html#command-line
# nuitka3 --follow-imports main.py
# nuitka3 --standalone --follow-import-to=app --nofollow-imports --show-progress main.py
# nuitka3 --onefile main.py
# nuitka3 打包速度慢，打包执行总出现错误。

# 使用pyinstaller 进行打包
# 多文件
# pyinstaller -D --hidden-import="main"  main.py
# 避免 pyinstaller -D --hidden-import="main"  main.py
# 单文件
# pyinstaller -F --hidden-import="main"  main.py

import uvicorn
from fastapi import FastAPI

from app import start_event, shutdown_event, router_init, middleware_init

lapp = FastAPI(title="landv_API",
               description="landv平台模块接口文档",
               version="1.0.0",
               on_startup=[start_event],
               on_shutdown=[shutdown_event],
               redoc_url=None,  # 禁止显示redoc文档
               # docs_url=None,  # 禁止显示swagger文档
               # openapi_url=None,  # 禁止显示openapi.json
               )
# # 初始化日志
# log_init()
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
        # https://www.cxymm.net/article/qq_43994782/119031998 好吧，骚操作
        # https://www.uvicorn.org/deployment/
        app='main:lapp',
        # app=lapp,
        # app=app,
        host='0.0.0.0',
        port=8001,
        debug=False,
        # reload=True,
        # 修改项目运行参数，即reload改为False 用于打包
        reload=False,
        workers=1
    )
