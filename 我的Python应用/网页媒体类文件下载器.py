# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

import os


if not os.path.exists('.\\download'):
    os.mkdir('.\\download')

if not os.path.exists('url.txt'):
    open('url.txt','a')

def main():
    while True:
        title()
        print('')
        list=int(input('\033[1;36m请输入您想使用的功能(例如：1)：\033[m'))
        if list in [0,1,2,3,4]:
            if list==1:
                meun1()
            elif list==2:
                meun2()
            elif list==3:
                meun1()
            elif list==4:
                meun1()
            else:
                answer=input('\033[1;36m你想要结束程序吗？y/n：\033[m')
                if answer=='y' or answer=='Y':
                    print('\033[1;36m感谢您的使用，再会！\033[m')
                    break
                else:
                    continue
        else:
            print('\033[1;36m对不起，您输入的功能编号有误！\033[m')
            print('\033[1;36m请重新输入\033[m')

def meun1():
    while True:
        print('')
        print('\033[1;36m在下载之前，您需要把您的网址放入当前目录下的url.txt文件中，注意每个网址为一行\033[m')
        answer1=input('\033[1;36m您的网址放好了吧，我们现在可以下载了吗？y/s：\033[m')
        if answer1=='y' or answer1=='Y':
            download1()
            print('')
            answer3=input('\033[1;36m还想继续下载吗？想的话把新的网址保存在url.txt文件中。y/n：\033[m')
            print('\033[1;36m--------------------------------------------------------------------------\033[m')
            if answer3=='y' or answer3=='Y':
                continue
            else:
                print('\033[1;36m========================好吧，欢迎下次使用========================\033[m')
                print('')
                break
        else:
            print('\033[1;36m请放好网址\033[m')
            continue

def meun2():
    while True:
        print('')
        print('\033[1;36m在下载之前，您需要把您的网址放入当前目录下的url.txt文件中，注意每个网址为一行\033[m')
        answer1=input('\033[1;36m您的网址放好了吧，我们现在可以下载了吗？y/s：\033[m')
        if answer1=='y' or answer1=='Y':
            download2()
            answer3=input('\033[1;36m还想继续下载吗？想的话把新的网址保存在url.txt文件中。y/n：\033[m')
            if answer3=='y' or answer3=='Y':
                continue
            else:
                print('\033[1;36m========================好吧，欢迎下次使用========================\033[m')
                break
        else:
            print('\033[1;36m请放好网址\033[m')
            continue


def title():
    print('\033[1;32m=============================Python下载网页视频文件===============================\033[m')
    print('== \033[1;34m**功能菜单**\033[m')
    print('== 1.单网址单视频')
    print('== 2.单网址多视频')
    print('== 3.音乐下载')
    print('== 4.图片下载')
    print('== 0.关闭程序')
    print('==')
    print('== \033[1;34m**使用说明**\033[m')
    print('== 2.在下载前,你需要准备好文件下载地址.')
    print('== 3.部分网站可能需要你先登录完成后,在复制下载地址.')
    print('==                                                       Email:2939818719@qq.com')
    print('\033[1;32m================================================================================\033[m')

def download1():
    with open('url.txt', 'r') as URL:
        for i in URL.readlines():
            print('\033[1;36m请耐心等待一小段时间，链接需要加载\033[m')
            os.system(f'you-get -o ./download {i}')
            print('')
    print('\033[1;36m已经全部下载在当前目录下的download文件夹中\033[m')

def download2():
    with open('url.txt', 'r') as URL:
        for i in URL.readlines():
            print('\033[1;36m请耐心等待一小段时间，链接需要加载\033[m')
            os.system(f'you-get --playlist -o ./download {i}')
            print('')
    print('\033[1;36m已经全部下载在当前目录下的download文件夹中\033[m')


if __name__ == '__main__':
    main()

