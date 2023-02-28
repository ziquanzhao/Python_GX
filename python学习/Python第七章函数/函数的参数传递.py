# 编写人：赵子权
# 编写时间：2022/4/24 21:12
# 邮箱:2939818719@qq.com


def fun (arg1,arg2):
    print('arg1:',arg1)
    print('arg2:',arg2)
    arg1=100
    arg2.append(10)
    print('arg1:', arg1)
    print('arg2:', arg2)
    return

n1=10
n2=[10,20,30]
fun(arg1=n1,arg2=n2)
