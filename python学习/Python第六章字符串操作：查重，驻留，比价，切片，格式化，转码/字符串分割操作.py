# 编写人：赵子权
# 编写时间：2022/4/24 16:58
# 邮箱:2939818719@qq.com

a='python hello|world'  #使用指定的分隔符从左侧开始分割字符串，split
lst=a.split()  #默认采用空格作为分隔符,分割结果为列表
lst=a.split(seq='|')  #使用seq=指定分隔符，分割结果为列表
lst=a.split(seq=' ',maxsplit=1)    #使用seq=指定分隔符，使用maxsplite=指定最大分割次数，达到最大分割次数后，后面的字符串将作为一个整体
#使用指定分隔符从右侧开始分割字符串，rsplit,使用方法和splite完全一样，只是从右侧开始分割而已