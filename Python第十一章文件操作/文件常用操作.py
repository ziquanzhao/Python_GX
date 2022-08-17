# 编写人：赵子权
# 编写时间：2022/4/25 19:34
# 邮箱:2939818719@qq.com

'''read（）  读取文件中的内容'''
b=open('c.txt','r')  #打开a.txt，r只读方式打开
print(b.read())  #读取c.txt中全部的内容
print(b.read(1))  #d读取c.txt中前两个字符

'''readline()   读取文本文件中一行内容'''
b=open('c.txt','r')
print(b.readline())   #读取一行内容

'''readlines()   读取所有行，把每一行的内容作为列表中的一个元素，结果为一个列表'''
b=open('c.txt','r')
print(b.readlines())

'''write()   将字符串写入文件'''
b=open('c.txt','a+')  #追加打开c.txt文件
b.write('hello')   #把字符串’hello‘写入c.txt文件中
lst=['a','b']  #此列表必须全为字符串
b.writelines(lst)   #把列表追加到c.txt文件中，注意不会加换行符或者制表符，会挤到一起
b.close()

'''seek(),调正文件指针，默认文件指针在第一个字节后面，特别注意是字节字节字节字节'''
b=open('c.txt','r')
b.seek(3)  #把文件指针调整到第三个字节后，一个中文占两个字节，一个字母占一个字节
print(b.read())
b.close()

'''tell()   返回当前指针位置'''
b=open('c.txt','r')
b.seek(3)
print(b.tell())  #返回当前指针位置
b.close()

'''close()   关闭资源'''

#with语句（上下文管理器）可以自动关闭释放资源，不用我们自己手动关闭
'''语法格式是：with open('c.txt','r') as b:'''
with open('c.txt','r') as b:
    print(b.read())  #不用再b.close了

#使用with语句进行文件复制
with open('CgKCS-1.png','rb') as x:
    with open('1.png','wb') as y:
        y.write(x.read())  #把read读取到x的数据写入y中




