# 编写人：赵子权
# 编写时间：2022/4/24 22:09
# 邮箱:2939818719@qq.com

#计算6的阶乘：
def fac(n):
     if n==1:
         return 1
     else:
        x=n*fac(n-1)
        return x
print(fac(6))

#计算第六个斐波那契数
def fab(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        x=fab(n-1)+fab(n-2)
    return x

print(fab(6))  #输入第六个斐波那契数

for i in range(1,7,1):   #输出前六个斐波那契数
    print(fab(i),end='\t')
