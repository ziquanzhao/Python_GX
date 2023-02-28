# 编写人：赵子权
# 编写时间：2022/4/24 16:28
# 邮箱:2939818719@qq.com

a='PYTHON'
b='python'
c='PYThon'

#upper,把所有字母全部转换为大写
b1=b.upper()   #转成大写后产生一个新字符串
print(b1)

#lower,把所有字母全部转换为小写
a1=a.lower()    #转成大写后产生一个新字符串
print(a1)

#swapcase,把大写转小写，把小写转大写
print(c.swapcase())

#capitalize,把第一个祖父转换为大写，其余字符全部小写
print(c.capitalize())

#title,把每个单词的第一个字符转换位大写，把每个单词剩余字符转换为小写
print(c.title())