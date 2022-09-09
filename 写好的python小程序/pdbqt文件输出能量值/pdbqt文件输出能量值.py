# 编写人：赵子权
# 编写时间：2022/5/6 19:13
# 邮箱:2939818719@qq.com

import os
import fnmatch
import re
import shutil
import xlwt

if os.path.exists('.\\pdbqt-here'):
    shutil.rmtree('.\\pdbqt-here')

if os.path.exists('energy.txt'):
    os.remove('energy.txt')
if os.path.exists('Energy.xls'):
    os.remove('Energy.xls')
   
print('此程序适用对象：Autodock vina v1.2.3版本的对接结果文件')
print('此程序作用：提取对接结果的结合能数值')
os.mkdir('.\\pdbqt-here')
print('请把对接结果文件（即pdbqt文件放入当前目录下的pdbqy-here文件夹中）')


answer=input('您把对接结果文件放好了吗？y/n：')
if answer=='y' or answer=='Y':
    for i in os.listdir('.\\pdbqt-here\\'):
        if fnmatch.fnmatch(i,'*.pdbqt'):
           with open('filename.txt','a') as filename:
               filename.write(i+'\n')
    with open('filename.txt','r') as a:
        name=a.readlines()
        name=[line.strip('\n') for line in name]  #strip()方法去除字符串开头和结尾处的指定字符
    os.chdir('.\\pdbqt-here')
    for o in name:
        with open(o,'r') as b:
           result=b.read()
           txt=re.findall('REMARK VINA RESULT:.*',result)
           file=[]
           for q in txt:
               file.append(q[22:29])
        with open('energy.txt','a') as x:
            x.write(o)
            x.write('\t')
            x.write('\t'.join(file))
            x.write('\n')
    os.chdir('..\\')
    os.remove('filename.txt')
    shutil.move('.\\pdbqt-here\\energy.txt','.\\')

    with open('energy.txt', 'r', encoding='utf-8') as f:
        new_excel = xlwt.Workbook(encoding='utf-8')
        new_excel_sheet = new_excel.add_sheet('Mysheet')
        row = 0
        col = 0
        for i in f:
            txt_row = i.split('\t')
            for q in range(len(txt_row)):
                new_excel_sheet.write(row, col, txt_row[q])
                col = col + 1
            row = row + 1
            col = 0
        new_excel.save('Energy.xls')
    print('对接结合能已经被输出到Energy.xls文件中')
else:
    print('请把对接结果文件放入pdbqt-here文件夹中，然后重新执行该程序即可')





