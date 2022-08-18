# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

import os

a = os.listdir('./')
for i in a:
    if 'chr1' in i and 'idx' not in i:
        print(i)