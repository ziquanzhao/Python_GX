# 编写人：赵子权
# 编写时间：2022/4/22 10:14
# 邮箱:2939818719@qq.com

#range函数可以作为for循环的遍历对象

#range()创建的第一种方式
r=range(10)  #range（stop）小括号只有一个数，意思是创建一个默认从0开始，步长为1，到10结束的列表[0,1,2,3,4,5,6,7,8,9]
print(r)  #range(0,10)
print(list(r))  #只有用list时才会去计算这个列表


#range()创建第二种方式
r=range(1,10)    #range(start,stop)小括号有两个数字。意思是创建一个从1开始，步长为1，到10结束的列表[1,2,3,4,5,6,7,8,9]
print(r)   #range(1,10)
print(list(r))


#range()创建第三种方式
r=range(1,10,2)      #range(start,stop,step)
print(r)
print(list(r))