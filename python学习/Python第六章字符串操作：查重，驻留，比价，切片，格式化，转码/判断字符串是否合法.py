# 编写人：赵子权
# 编写时间：2022/4/24 17:07
# 邮箱:2939818719@qq.com

print('hello'.isidentifier())  #判断hello是不是合法字符串
print('\t'.isspace())  #判断\t是不是空白字符串（空白字符串有空格，回车，水平制表符）
print('abc'.isalpha())   #判断字符串是不是全部由字母组成
print('1234'.isdecimal())   #判断字符串是否全部由十进制数字组成
print('123'.isnumeric())    #判断字符串是否全部由数字组成，罗马数字，汉字数字也是数字，Ⅱ，二
print('123abc'.isalnum())   #判断字符串是否全部由数字和字母组成，汉字属于字母
