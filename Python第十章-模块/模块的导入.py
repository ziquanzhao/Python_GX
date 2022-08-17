# 编写人：赵子权
# 编写时间：2022/4/25 11:31
# 邮箱:2939818719@qq.com

#创建模块
'''其实就是创建一个.py文件'''

#模块的导入
import math  #导入模块
print(math.pow(2,3)) #2的三次方

#如何导入自定义模块
import aaa  #导入我的自定义模块aaa
print(aaa.calr(10,20))  #调用我aaa模块中的calr函数计算求和

def add(a,b):
    return  a+b
if __name__=='__main__':    #加入这句话后，只有我运行模块的导入.py这个文件时才会去执行print（add（10，20））.如果我在其他py文件中导入add模块，他也不会执行打印
    print(add(10,20))

#导入带有包的模块时注意事项
import math.pow   #使用import方式导入，只能跟包或者模块名称
'''import 包名.模块名'''

from math import pow  #使用from....import....导入时，可以时包，模块，函数名。变量