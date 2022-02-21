#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 上午11:39
# @Author  : landv
# @File    : info.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    : 用户信息

# 自己初始化路径
from fastapi import APIRouter

router = APIRouter()


@router.get("/user/info")
async def info():
    return {"message": "Hello info"}
