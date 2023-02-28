# 编写人：赵子权
# 编写时间： 21:49

#整数型-->int 98  100
#浮点型-->float  3.1415926
#布尔型-->True,False
#字符串型--> ’人生苦短，我用python‘


#整数型，可以是正数，负数，0
n1=90
n2=-2
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
#整数可以表示位二进制，十进制，八进制，十六进制
print('十进制',123)
print('二进制',0b01010101)#二进制用0b开头
print('八进制',0o123456)#八进制用0o开头
print('十六进制',0x123456ABCDEF)#十六进制用0x开头


#浮点型，直接浮点型运算会有误差，可以用Decimal这个模块计算
n1=1.1
n2=2.2
print(n1+n2)#结果会有3.300000000003，这是不对的。
from decimal import Decimal
print(Decimal(n1)+Decimal(n2))#结果也不对，3.0000000000000026645
print(Decimal('1.1')+Decimal('2.2'))#结果位3.3，这才对

#布尔型，python中的布尔类型是可以用于数字计算的，True为1，False为0
print(True+1)   #2
print(False+1)   #1


#字符串，单引号，双引号，三引号，注意单引号和双引号尽可以在一行显示，而三引号可以多行显示
print('helloworld')#helloworld
print("helloworld")#helloworld
print('''hello
world''')#helloworld,可以不在一行


name='张三'
age=20

print(type(name),type(age))#结果显示数据类型不同
#print('My name is'+name+'My age is'+age)#报错，数据类型不统一，你不能使用通过’+‘连接符连接，注意+是连接符
print('My name is '+name+'\n'+'My age is'+str(age))

#str()其他类型转为字符串类型
#int()其他类型转为整数型，注意小数转整数时只会截取整数部分，字符串转整数必须为整数串
#float()其他类型转换为浮点型
