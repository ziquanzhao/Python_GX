#coding=utf-8
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

import os
import re
a = 'aa1234vo.bam\n22'
a = re.sub('.bam\n', '', a)
b = re.sub('vo\nb', '', a)
print(a)