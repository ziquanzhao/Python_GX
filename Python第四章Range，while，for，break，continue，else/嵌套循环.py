# 编写人：赵子权
# 编写时间：2022/4/22 14:54
# 邮箱:2939818719@qq.com
'''输出一个三行四列的矩形'''

for i in range(1,4):    #表行，执行三次，一次是一行
    for j in range(1,5):   #表列，执行四次，一次是一列
        print('*',end='\t')    #不换行输出
    print()                #换行所必须的


for i in range(1,10):    #行数
    for j in range(1,i+1):
        print('*',end='\t')
    print()              #换行
####输出一个三角形


for i in range(1,10):   #行数
    for j in range(1,i+1):   #每行执行几次列
        print(i,'*',j,'=',i*j,end='\t')   #每列填写什么
    print()                 #换行
#9*9乘法表

#break的嵌套循环
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j,end='\t')
    print()     #换行

#continue的嵌套循环
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()