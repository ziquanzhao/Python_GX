# 编写人：赵子权
# 编写时间：2022/4/24 20:49
# 邮箱:2939818719@qq.com
#编码
s='海内存知己，天涯若比邻'
a=s.encode(encoding='GBK')   #使用GBK进行编码，GBK中一个中文字占两个字节
print(a)
b=s.encode(encoding='UTF-8')   #使用UTF-8进行编码，UTF-8中一个中文字站三个字节
print(b)


#解码
print(a.decode(encoding='GBK'))   #使用GBK进行解码
print(b.decode(encoding='UTF-8'))   #使用UTF-8进行解码

#查重时用