# 编写人：赵子权
# 编写时间：2022/4/25 9:27
# 邮箱:2939818719@qq.com
try:
    a=int(input('请输入第一个数字：'))
    b=int(input('请输入第二个数字：'))
    print('结果为：',a/b)
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字')
print('程序结束')  #try     except可以用于排错警告，异常处理机制


try:
    a = int(input('请输入第一个数字：'))
    b = int(input('请输入第二个数字：'))
    res=a/b
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字')
else:
    print('结果为：',res)
#try-except-else,try块中没有一场则执行else块。如果try块有一场则去执行expect块


try:
    a = int(input('请输入第一个数字：'))
    b = int(input('请输入第二个数字：'))
    res=a/b
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字')
else:
    print('结果为：',res)
finally:
    print('无论是否产生异常，都会去执行的代码')  #文件处理时可以用于关闭文件管理器
    print('感谢您的使用')
print('程序结束')
#try-except-else-finally，try块有问题走except-finally，try块没有错误走else-finally。无论咋样，finally都会执行


