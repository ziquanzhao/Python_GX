# 编写人：赵子权
# 编写时间：2022/4/24 20:56
# 邮箱:2939818719@qq.com

#函数的创建
'''
def 函数名 （【输入参数】）：
    函数体
    return xxx
'''

def calc (a,b):  #a，b成为形式参数，出现在函数的定义中
    c=a+b
    return c

result=calc(10,20)  #函数的调用，10，20称为实际参数，出现在函数的调用中，位置实参
print(result)
res=calc(b=20,a=10)  #关键字参数
print(res)