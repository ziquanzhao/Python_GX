# 编写人：赵子权
# 编写时间：2022/4/25 8:58
# 邮箱:2939818719@qq.com

'''常见BUG类型
1.粗心导致的语法错误
    漏了末尾的冒号，在if，循环，else
    缩进错误，该缩进的不缩进
    中英文字符错误
    字符串拼接时，把数字和字母拼接在一起
    没有定义变量
    等于和赋值，==，=
'''

'''常见BUG类型
2.知识点不熟练导致的错误
    a.索引越界问题indexError
      lst=[1,2,3,4]
      print(lst[4])  #最大只能是3
      
    b.类似于append（）使用不熟练
      #lst=append（’1‘，’2‘，’3’）  #报错，lst.append(),并且append一次只能增加一个元素
'''
'''
ZeroDivisionError   数学计算出错，除0
indxError    没有索引
KeyError   没有key出错
NameError   没有初始化变量
SyntaxError  语法错误
ValueError  参数值错误，无效
'''

