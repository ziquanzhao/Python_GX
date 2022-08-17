# 编写人：赵子权
# 编写时间：2022/4/22 10:25
# 邮箱:2939818719@qq.com


#while循环
#while 条件判断式
#    条件执行

a=1
while a<10:
    print(a)
    a=a+1
#if的单分支结构和while很类似，只是if仅仅判断一次，而while是循环判断多次

b=c=0        #初始化变量
while b<5:   #条件判断
    c=c+b    #条件执行体，循环体
    b=b+1    #改变变量
print(c)

x=1
b=0
while x<=100:
    if x%2==0:
        b=b+x
    x=x+1
print(b)
