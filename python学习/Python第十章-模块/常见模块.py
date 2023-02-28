# 编写人：赵子权
# 编写时间：2022/4/25 17:20
# 邮箱:2939818719@qq.com

import sys  #与python解释器和环境相关的标准库
print(sys.getsizeof('python'))   #模块.方法（‘变量’）

import time  #提供与时间相关的各种函数的标准库

import os   #提供与访问操作系统服务功能相关的各种函数的标准库

import calendar  #提供与日期相关的各种函数的标准库

import urllib #用于读取来自网上的数据库资料
print(urllib.request.urlopen('http://www.baidu.com').read())  #爬虫，读取网址百度的数据

import json  #用于使用JSON序列话和反序列化对象

import re #用于在字符串中执行正则表达式匹配和替换

import math  #提供标准算数运算的标准库

import decimal  #用于进行精确控制运算精度，有效位数，四舍五入的十进制计算

import logging  #提供了灵活的记录事件、错误、警告、调试信息等日志