# 编写人：赵子权
# 编写时间：2022/4/25 18:45
# 邮箱:2939818719@qq.com

#中文编码用UTF-8
#在文件的开头写上encodings=UTF-8

#文件的读写
'''语法规则
file=open(filename [mode,encoding])
file:变量
open：内置函数，用于打开或者创建文件的函数
filename：打开或创建的文件的文件名
mode：打开模式，默认是只读
encoding：文本文件字符编码格式，默认gbk
'''

#读取a.txt文件的内容  ‘r’只读模式
b=open('a.txt','r')  #打开a.txt，r只读方式打开
#print(b.read())  #读取b中的内容
b.close()             #关闭文件b，关闭系统资源

#创建并修改b.txt文件   ‘w’只写模式
file=open('b.txt','w')  #打开b.txt文件，如果没有则创建，w为写入模式
file.write('python') #向b.txt文件中写入python，如果b文件原来有内容，则全部替换掉
file.close()

#创建或者追加文本   ‘a’  追加模式
file2=open('c.txt','a')   #a为追加模式，有内容的话会在末尾追加新内容
file2.write('python\n')   #向c文件中追加python，并且要换行
file2.close()

#图片，视频，音频文件的复制操作  ‘rb’二进制文件的只读模式，‘wb’二进制文件的写入模式
file3=open('CgKCS-1.png','rb')  #只读打开logo.png图片
file4=open('logo2.png','wb')  #读写创建logo2.png文件
file4.write(file3.read())   #向file4文件中写入file3的二进制数据的读取内容，这个过程相当于复制
file3.close()
file4.close()

#‘+’读写方式打开，‘a+’


