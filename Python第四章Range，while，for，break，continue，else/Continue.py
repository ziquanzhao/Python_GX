# 编写人：赵子权
# 编写时间：2022/4/22 11:36
# 邮箱:2939818719@qq.com

#continue可以结束本次循环而进入下一次循环，break是直接跳出循环。
for i in range(1,51):
    if i%5!=0:
        continue
    print(i)