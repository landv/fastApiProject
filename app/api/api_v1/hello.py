#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/21 上午11:00
# @Author  : landv
# @File    : hello.py
# @Software: PyCharm
# @Github  : github/landv
# @Email   : landvcn@qq.com
# @Desc    :

from fastapi import APIRouter

# 自己初始化路径
router = APIRouter()


@router.get("/")
async def index():
    return {"message": "Hello World"}


@router.get("/ttt")
async def ttt():
    return {"message": "Hello ttt"}
