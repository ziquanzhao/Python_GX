# 编写人：赵子权
# 编写时间：2022/4/24 16:12
# 邮箱:2939818719@qq.com

#仅保留一个相同的字符串，当出现相同字符串时，不会新建字符串
a='python'
b="python"
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))
