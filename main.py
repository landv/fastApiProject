#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 上午9:51
# @Author  : landv
# @File    : mian.py.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    :
import uvicorn
from app import create_app
"""
程序入口
注意事项：使用pyinstaller进行打包时，需要将reload修改为False。
"""
lapp = create_app()
if __name__ == '__main__':
    uvicorn.run(
        # https://www.cxymm.net/article/qq_43994782/119031998 好吧，骚操作.
        # https://www.uvicorn.org/deployment/
        app='main:lapp',
        # app=lapp,
        host='0.0.0.0',
        port=8001,
        debug=False,
        # 开发模式
        reload=True,
        # 修改项目运行参数，即reload改为False 用于打包
        # reload=False,
        # workers=1
    )
