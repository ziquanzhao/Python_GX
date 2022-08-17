# 编写人：赵子权
# 编写时间：2022/4/26 20:54
# 邮箱:2939818719@qq.com
def numbers():
    num=int(input('请输入一个十进制的整数：'))
    print(num,'转换到二进制是',bin(num))   #逗号的话不是紧密相连的，会有一个空格
    print(str(num)+'转换到二进制是',bin(num))  #转换字符串类型
    print('%s转换到二进制是%s' % (num,bin(num)))   #%s作为字符串占位符，格式化字符串
    print('{0}转换到二进制是{1}'.format(num,bin(num)))   #.format()  格式化字符串
    print(f'{num}转换到二进制是{bin(num)}')


if __name__ == '__main__':  #以主程序的方式去调用
    while True:    #程序永远执行
        try:
            numbers()   #正确时执行定义numbers函数
            answer=input('你想继续转换吗y/n：')
            if answer=='y' or answer=='Y':
                numbers()
            else:
                break
        except:
            print('输入有误')   #不正确时显示输入有误
            break         #并且跳出程序，否则的话它又回去执行，循环执行，死循环，因为while true是永远执行





