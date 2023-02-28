# 编写人：赵子权
# 编写时间： 0:16


# > < >= <= == !=
# 这些比较运算符比较的都是vlaue
# 一个数据是由识别符id、类型type、值vlaue三部分组成的，比较运算符只比较值
a = 10;
b = 20
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
print('--------------------------------------------')

# is is not，它比较的是ID,识别符
print(id(a), id(b))
print(a is b)  # False
print(a is not b)  # True
print('--------------------------------------------')

ls1 = [11, 22, 33, 44]
ls2 = [11, 22, 33, 44]
print(id(ls1), id(ls2))
print(ls1 is ls2)
