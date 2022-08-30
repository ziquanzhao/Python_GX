#coding=utf-8
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

import os
import re


a = 'WF113_sort_dedup_chr11.gvcf\na'
b = re.sub('_sort_dedup_chr\d*.gvcf\n', '', a)
print(b)