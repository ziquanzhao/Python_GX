# 编写人：赵子权
# 编写时间： 21:06

#1.  \n -->newline新的一行,就是要换行
print('hello\nworld')#hello和world会输出到两行

#2.   \t -->制表符Tab的意思，一个制表符有4个空位
print('hello\tworld') #打印之后发现好像制表位只有三个字符长度，这是因为制表符每4个位置为一组，hell是一个制表位，o和\t用一个制表位，o是一个制表位，所以剩下3个制表位
print('helloooo\tworld') #这个打印之后就发现制表符是4个字符长度了，因为hell一个Tab，oooo一个Tab，\t新开了一个Tab，4个长度

#3.   \r -->retrun ,\r后面的内容会把前面的内容覆盖掉
print('hello\rworld') #输出world，覆盖掉了

#4.   \b --> BackSpace,退格，退一个格，删除上一个字符
print('hello\bworld') #输出hellworld，其中的o没有了

#5. 如何输出\\,'',"",其实就是前面加一个\转义符，让后面的这个字符仅仅作为文本，不在作为特殊符号就可以了
print('http:\\\\www.baidu.com')  #输出http:\\www.baidu.com,第一个转义符\让第二转义符\失效，第三个让第四个失效
print('老师说：\'大家好\'')

#6. 原字符，不让后面的转义字符起作用，可以在前面加r或者R
print(r'hello\nworld') #输出hello\nworld
#注意最后一个字符不能是\，但可以是\\，其实\\就是让后面那个转义字符失效