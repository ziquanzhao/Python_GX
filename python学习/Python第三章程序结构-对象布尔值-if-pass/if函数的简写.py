# 编写人：赵子权
# 编写时间：2022/4/22 9:43
# 邮箱:2939818719@qq.com
num1=int(input('请输入第一个整数：'))
num2=int(input('请输入第二个整数：'))
'''if num1>=num2:
        print(num1,'大于等于',num2)
    else:
        print(num1,'小于',num2)'''

print(str(num1)+'大于等于'+str(num2)  if num1>=num2 else  str(num1)+'小于'+str(num2))
#                             <---------True False------------>
#         条件为真的表达式写在前面                           条件为假的表达式写在后面