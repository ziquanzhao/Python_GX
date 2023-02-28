# 编写人：赵子权
# 编写时间：2022/4/24 21:20
# 邮箱:2939818719@qq.com

def fun (num):
    odd=[]   #创建一个空列表用于存奇数
    even=[]  #创建一个空列表用于存偶数
    for i in num:
        if i%2==True:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

a=[1,2,3,4,5,6]
print(fun(a))   #([1,3,5],[2,4,6]) 返回值为一个元组


'''
1.如果函数没有返回值，可以不屑return
2.如果函数的返回值为1个，则返回的原类型数据
3.如果函数的返回值多个，则返回值为元组
'''