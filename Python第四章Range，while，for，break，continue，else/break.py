# 编写人：赵子权
# 编写时间：2022/4/22 11:26
# 邮箱:2939818719@qq.com


#break提前终止循环
# if
#
#    break




#银行输入密码，最多输入三次，如果正确就结束循环
for i in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
