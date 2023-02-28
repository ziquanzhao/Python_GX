# 编写人：赵子权
# 编写时间：2022/4/26 21:21
# 邮箱:2939818719@qq.com

for i in range(1,4):
    user_name = input('请输入您的用户名：')
    user_pwd = input('请输入您的密码：')
    if user_name=='admin' and user_pwd=='123':
        print('登录成功')
        break
    else:
        print('账号或者密码不正确，请重新输入')
        if i<3:
            print(f'你还有{3-i}次机会输入')  #if语句未必要有else，可以没有
else:   #这个else是针对for循环的，如果for循环执行完了，则执行else，否则不执行
    print('请联系管理员解决')
