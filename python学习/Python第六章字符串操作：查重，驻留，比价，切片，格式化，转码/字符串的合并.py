# 编写人：赵子权
# 编写时间：2022/4/24 17:22
# 邮箱:2939818719@qq.com
#join（）将列表或者元组中的字符串合并成一个新字符串
#注意必须是列表或者元组
a=['hello','python']
b={'world'}
print('|'.join(a))  #使用|作为连接符，把a列表中的字符串连接起来，注意‘|’.join，是一个点
print(' '.join(a))  #使用空格作为连接符，把a列表中的字符串连接起来
print('*'.join('python'))   #p*y*t*h*o*n

'''如何连接两个列表或者两个元组呢'''
#我的想法是利用列表的添加操作extend，变成一个列表，然后在连接
d=list(b)
print(d)
a.extend(d)
print(a)
print(' '.join(a))

