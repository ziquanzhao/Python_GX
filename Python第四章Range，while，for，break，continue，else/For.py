# 编写人：赵子权
# 编写时间：2022/4/22 11:01
# 邮箱:2939818719@qq.com


#可迭代对象目前只有range（）以及字符串
for i in 'python':
    print(i)


for i in range(1,50,4):
    print(i)


for _ in range(5):
    print('人生苦短，我用python')
#如何你的自定义变量不会用到后面的输出里，你可以用下划线代替，一般用于重复输出多少个一样的东西，用染range（）控制输出次数、

print('------------for计算1到100偶数和------------')
a=0
for i in range(2,101,2):
    a=a+i
print(a)


print('---------------输出100到999中间的水仙花数-----------')
sum=0
for i in range(100,1000,1):
    ge=i%10  #个位
    shi=i//10%10    #十位
    bai=i//100    #百位
    if ge**3+shi**3+bai**3==i:
        print(i)

#银行输入密码
for i in range(1,3,1):
    uname=input('请输入你的用户名：')
    pwd=input('请输入你的密码：')
    if uname=='admin' and pwd=='123':
        print('登陆成功')
        break
    else:
        print('输入有误，请重新输入！')
else:
    print('对不起，您输入三次全部有误')