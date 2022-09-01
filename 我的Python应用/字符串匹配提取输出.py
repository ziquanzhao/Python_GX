
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
'''
学会两个字符处理命令：re.findall;re.sub
变量.replace(不支持正则)
'''

'''
str='-'
lis=['a','b','c']
print(str.join(lis))  #a-b-c
'''
'''
import re
filepath = "E:\\Python\\我的Python应用\\music.txt"
txt = open(filepath,'r').read()
test_text = re.findall(r'url.*m4a',txt)#取出每行含有url.....m4a的文本  r是不让转义字符起作用
result = '\n'.join(test_text)#换行输出
print(result)
with open('test.txt','a') as file:  #写入文件中
    file.write(result)
#a=re.findall(r'字符串或正则',读取文本的变量,re.S)  最后的re.S参数是允许跨行匹配，一般不会用它
'''
'''
#python的特殊字符正则
str = 'aabbabaabbaa'

1. 符号 . 就 是匹配除 \n (换行符)以外的任意一个字符
print(re.findall(r'a.b',str)) #['aab', 'aab']

2.符号 * 前面的字符出现0次或以上
print(re.findall(r'a*b',str)) #['aab', 'b', 'ab', 'aab', 'b']

3.符号 .* 匹配从.*前面为开始到后面为结束的所有内容
print(re.findall(r'a.*b',str))  #['aabbabaabb']

4.符号.*? 遇到开始和结束就进行截取，因此截取多次符合的结果，中间没有字符也会被截取
print(re.findall(r'a.*?b',str)) #['aab', 'ab', 'aab']

str = 'He123/45_? 6'  #特别注意下面的字符需要用到转义字符，因此不能加r
result1 = re.findall('\d',str)      #\d匹配任何十进制数  ['1','2','3','4','5','6']
result2 = re.findall('\d+',str)     #\d+可匹配一位或多位数字使用  ['123','45','6']
result3 = re.findall('\D',str)      #\D匹配非数字的任何字符，包含空格  ['H','e','/','_','?',' ']注意这个空格
result4 = re.findall('\w',str)      #\w匹配任何字母数字字符，包括下划线，但不包含空格  ['H','e','/','_','?','1','2','3','4','5','6']
result5 = re.findall('\W',str)      #\W匹配非字母非数字，包括下划线空格，一般就是只匹配特殊字符的意思 ['/','?',' ']
result6 = re.findall('\s',str)      #\s匹配任何空白字符 只匹配空格    [' ']
result7 = re.findall('\S',str)      #\S匹配非任何空白字符,只不匹配空格，其他都匹配
result8 = re.findall('\AHello',str)     #\A仅匹配字符串开头 匹配开头的一串字符串  ['He']
result9 = re.findall('bye\Z',str)       #\Z仅匹配字符串结尾 匹配末尾的一串字符串  ['He']
'''

'''
# 02:“[]”匹配[]中列举的字符
# 字符串第一个字符只要存在于[]中就能成功匹配，
# [a-zA-Z0-9_]表示可以匹配"a-z","A-Z","0-9"和"_"区间内的所有元素
result=re.match("[Aa]","Aaaaaaabbba")
a=result.group()
print(a)
结果：A
'''

'''
del_num = re.sub("\d+ ", "", result)#去掉每行行首的数字  #'\d+'
del_awake = del_num.replace("awake", "")#去掉awake
del_commd = del_awake.replace("commd", "")#去掉commd
del_string1 = re.sub("-a+\d\d\d\d-\d.wav", "", del_commd)#去掉-a0023-1.wav类型的字符串
del_string2 = re.sub("-a+\d\d\d\d.wav", "", del_string1)#去掉-a0016.wav类型的字符串
print(del_string2)

re.sub('老字符串','新字符串'，变量)  #字符串支持正则
变量.replace（'老字符串','新字符串'）  #字符串不支持正则
'''
a = range(1,5,1)
print(a)