# 编写人：赵子权
# 编写时间：2022/4/25 17:43
# 邮箱:2939818719@qq.com


#第三方安装
'''pip install 模块名'''
#这个要在cmd 然后输入 pip install 模块名

#使用模块
'''import 模块名'''

import schedule
import time   #导入模块

def job():
    print('haha')   #定义一个函数

schedule.every(3).seconds.do(job)  #每间隔3秒执行这个函数

while True:
    schedule.run_pending()
    time.sleep(1)        #执行完休眠1秒继续执行