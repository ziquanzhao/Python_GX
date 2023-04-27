#! /usr/bin/python3
# coding=utf-8
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os
import re


a = []
for i in os.listdir('./'):
    if '.fq.gz' in i:
        a.append(f'-V /Script/{i}')
print(a)