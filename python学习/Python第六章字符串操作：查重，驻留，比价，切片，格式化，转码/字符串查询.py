# 编写人：赵子权
# 编写时间：2022/4/24 16:23
# 邮箱:2939818719@qq.com
s='hello,hello'
print(s.index('lo'))  #查找lo第一次出现的位置，找不到报错
print(s.rindex('lo'))   #查找lo最后一次出现的位置，找不到报错
print(s.find('lo'))    #查找lo第一次出现的位置，找不到返回-1
print(s.rfind('lo'))    #查找lo最后一次出现的位置，找不到返回-1

'''
建议使用find，rfind
'''
