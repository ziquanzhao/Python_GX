# 编写人：赵子权
# 编写时间：2022/4/25 20:28
# 邮箱:2939818719@qq.com

#os模块与操作系统相关的一个模块
import os
'''
os.system('notepad.exe')   #打开系统记事本
os.system('calc.exe')    #打开系统计算机

#os打开可执行文件，脚本或者exe程序
os.startfile('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe') #打开浏览器的程序，注意路径分割是双\\


#返回当前工作目录
print(os.getwd())  #os.getwd()返回当前工作目录
'''

#返回指定路径下所有文件和目录信息
print(os.listdir('C:\\Program Files (x86)\\Microsoft\\Edge\\Application'))  #注意最好是绝对路径

#创建目录
os.mkdir('newdir')  #在当前目录下创建一个nemdir的新目录

#创建多级目录
os.makedirs('newdir1/newdir2/newdir3')

#删除目录
os.rmdir('newdir')

#删除多级目录
os.removedirs('newdir1/newdir2/newdir3')

#设置当前目录
os.chdir('E:\\python')

#获取文件后者目录的绝对路径
import os.path
print(os.path.abspath('a.txt'))

#判断文件或者目录是否存在
print(os.path.exists('1.png'))   #如果存在返回True，否则为False

#将目录与目录或者目录与文件拼接起来
print(os.path.join('E:\\python','b.txt'))   #返回E：/python/b.txt

#分裂文件名和扩展名
print(os.path.splitext('a.txt'))   #把目录与文件名拆分开

#拆分目录与文件名
print(os.path.split('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'))

#从路径中提取文件名
print(os.path.basename('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'))  #msedge.exe

#从路径中提取不包含文件名的剩下的路径
print(os.path.dirname('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'))   #C:/Program Files (x86)/Microsoft/Edge/Application

#案例-----列出指定目录下所有.py文件
import os
cd=os.getcwd()  #获取目录
lst=os.listdir(cd)  #获取目录下所有文件及其目录信息
for filename in lst:
    if filename.endswith('.py'):  #如果以.py结尾则打印输出（.endswith指定以什么结尾）
        print(filename)


if not os.path.exists('C:\\Download'):
    os.mkdir('C:\\Download')

