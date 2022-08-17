# 编写人：赵子权
# 编写时间：2022/4/25 21:39
# 邮箱:2939818719@qq.com
'''
学生信息管理系统具备那些功能：
1.添加学生及成绩
2.保存学生信息到文件
3.修改和删除学生信息
4.查询学生信息
5.根据成绩排序
6.统计学生总成绩
'''
from typing import Dict, Any

filename='studentinformation.txt'
import os
def main():
    while True:
        menm()
        chse = int(input('请选择您想要进行的项目编号（例如：1）：'))
        if chse in [0,1,2,3,4,5,6,7]:
            if chse==0:
                answer=input('您确定要退出系统吗？y/n：')
                if answer=='y' or answer=='Y':
                    print('感谢您的使用！')
                    break
                else:
                    continue
            elif chse==1:
                insert()  #录入学生信息
            elif chse==2:
                search()  #查询学生信息
            elif chse==3:
                delete()  #删除学生信息
            elif chse==4:
                modify()
            elif chse==5:
                sort()
            elif chse==6:
                total()
            elif chse==7:
                show()
        else:
            print('您输入的项目编号有误')  #如果选择的不在范围内，他会重新进入系统一次
            print('请重新输入您的编号')

def menm():
    print('====================学生信息管理系统=========================')
    print('-----------------------功能菜单-----------------------------')
    print('1.录入学生信息')
    print('2.查找学生信息')
    print('3.删除学生信息')
    print('4.修改学生信息')
    print('5.根据选择对学生成绩排序')
    print('6.统计学生总人数')
    print('7.显示所有学生信息')
    print('0.退出学生信息管理系统')
    print('------------------------------------------------------------')

def insert():
    print('欢迎进入学生信息录入模式，该模式可以录入学生的ID，姓名，英语成绩，python成绩，java成绩')
    student_list=[]
    while True:
        id=input('请输入ID，例如1001：')
        if bool(id)==False:
            break
        name=input('请输入姓名：')
        if bool(name)==False:
            break
        try:
            english=int(input(f'请输入{name}的英语成绩：'))
            python1=int(input(f'请输入{name}的python成绩：'))
            java1=int(input(f'请输入{name}的java成绩：'))
        except:
            print('请您输入数字，不要输入其他内容，请重新输入')
            continue          #这个contiune是重复try中的内容
        dic={'id':id,'name':name,'english':english,'python':python1,'java':java1}
        student_list.append(dic)
        answer=input('您是否继续添加学生y/n\n')
        if answer=='y':
            continue           #这个cintinue是重复while True下所有内容
        else:
            break
    save(student_list)
    print('您所输入的学生信息已经全部录入完毕')

def save(student_list):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for i in student_list:
        stu_txt.write(str(i)+'\n')
    stu_txt.close()

def search():
    pass

def delete():
    while True:
        student_name=input('请输入您所要删除的同学的名字：')
        if student_name!='':
            if os.path.exists(filename):              #判断文件是否存在
                with open(filename,'r',encoding='utf-8') as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False     #标记是否删除
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for i in student_old:
                        d=dict(eval(i))   #把从文件中读取的字符串转变为字典
                        if d['name']==student_name:
                            flag=True
                        else:
                            wfile.write(str(d)+'\n')
                    if flag==True:
                        print(f'姓名为 {student_name} 的学生信息已经删除')
                    else:
                        print(f'对不起，没有找到 {student_name} 的学生信息，可能是您从来没有录入 {student_name} 的学生信息')
            else:
                print('磁盘上根本没有储存学生信息的文件，检查文件是否完整，也可能是记录学生信息的文件根本没有数据')
                break
        else:
            print('您输入学生姓名有问题，请重新输入一次')
            break
        print('-----------------现在还剩下的学生信息如下-----------------')
        show()
        answer=input('请问您是否需要继续删除y/n：')
        if answer=='y' or answer=='Y':
            continue
        else:
            break

def modify():
    show()
    if os.path.exists(filename):              #判断文件是否存在
        with open(filename,'r',encoding='utf-8') as file:
            student_old=file.readlines()
    else:
        return
    restudent_name=input('请输入您所要修改学生姓名：')
    with open(filename,'a',encoding='utf-8') as wfile:
        for i in student_old:
            d=dict(eval(i))  #把从文件中读取的字符串转变为字典
            if d['name']==restudent_name:
                print('找到该学生信息了！')
                while True:
                    try:
                        d['name']=input('请输入姓名：')
                        d['english']=input('需要把的英语成绩改成：')
                        d['answerpython']=input('需要把的python成绩改成：')
                        d['answerjava']=input('需要把的java成绩改成：')
                    except:
                        print('您的输入有问题，可能不是数字，请重新输入：')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功！')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改y/n：\n')
        if answer=='y' or answer=='Y':
            modify()


def sort():
    pass

def total():
    pass

def show():
    pass

if __name__ == '__main__':  #最后以主程序的方式结束，调用main
    main()

