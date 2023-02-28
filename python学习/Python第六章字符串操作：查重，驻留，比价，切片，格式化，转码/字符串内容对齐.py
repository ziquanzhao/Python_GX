# 编写人：赵子权
# 编写时间：2022/4/24 16:52
# 邮箱:2939818719@qq.com

a='python'
#居中对齐,center
print(a.center(8,'*'))  #*python*,第一参数指定宽度，第二个参数指定填充符号，默认空格

#左对齐,ljust
print(a.ljust(8,'*'))   #python**,第一参数指定宽度，第二个参数指定填充符号，默认空格

#右对齐,rjust
print(a.rjust(8,'*'))   #**python,第一参数指定宽度，第二个参数指定填充符号，默认空格

