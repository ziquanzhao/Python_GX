# 编写人：赵子权
# 编写时间： 20:36
#python函数----print()

#1.可以打印输出数字，不用加引号
print(520)
print(98.5)

#2.可以打印输出字符串，需要加引号，单引号双引号都可以，意思就是让计算机直接打印我们的内容而不需要变化
print('helloworld')
print("helloworld")

#3.可以打印输出含有运算符的表达式，注意python会运算你的表达式并输出结果，如果不想运算，加引号
print(3+5)
print('3+5')

#4.可以将数据输出到文件中，没有文件会自动创建文件
fp=open('E:/Python/text.txt','a+')#打开一个text.txt文件，如果没有则创建，‘a+’意思是追加数据，fp就是一个临时变量，可以是其他的x呀，y呀都行，后面对应就行
print('helloworld',file=fp)#打印helloworld然后指定输出文件
fp.close()#关闭保存文件

#5.可以不进行换行输出
print('hello','world','python')

