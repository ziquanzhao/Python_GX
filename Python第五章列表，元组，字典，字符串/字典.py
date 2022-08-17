# 编写人：赵子权
# 编写时间：2022/4/22 18:10
# 邮箱:2939818719@qq.com

'''
1.字典是一个可变序列，和列表一样，可以执行增删改
2.字典就是键值对，是一个无序序列。列表是有序的，有索引。
3.字典是根据key来找value的
'''

#如何创建字典---方法一：
a={'张三':100,'李四':98,'王五':45}  #花括号创建字典时，遵循key：value，
print(type(a),a)
#如何创建字典---方法二：
b=dict(name='张三',age=20)  #内置函数创建字典时，value加不加’‘取决于数据类型，字符串要加，整型浮点型不加
print(type(b),b)

#如何获取字典中的值---方法一
print(b['name'])  #b['key'],中括号中要加引号
#如何获取字典中的值---方法二
print(b.get('name'))  #b.get('key'),中括号中要加引号

#判断指定的key在字典中是否存在
print('name' in b)
print('张三' not in a)

#字典元素的删除
del a['张三']  #删除张三的键值对
print(a)
a.clear()  #清空字典元素
print(a)

#字典元素的增加
a['陈六']=98
print(a)

#修改字典元素的修改
a['陈六']=100  #把陈六改成100
print(a)

#获取字典元素的key
x=a.keys()  #把a字典中所有key找出来赋值给x
print(x)
print(type(x))
print(list(x))  #把a字典的key转换为列表

#获取字典元素的value
y=a.values()  #把a字典中所有value找出来赋值给y
print(y)
print(type(y))
print(list(y))  #把a字典的value转换为列表

#获取字典所有的key-value
z=a.items()  #把a字典中所有的键值对找出来赋值给z
print(z)
print(type(z))
print(list(z))  #把a字典中所有的键值的转换为列表，转换之后的列表元素是以元组方式组成的

#字典元素的遍历
for i in b:
    print(i)  #遍历字典的key
    print(i,b[i])  #遍历字典的key，value
    print(i,b.get(i))  #遍历字典的key，value

#字典的特点
d={'name':'张三','name':'李四'}  #会输出李四，张三被替代。字典的value可以重复，但是key不允许重复

#字典生成式
items=['friuts','books','others']
prices=[10,20,30]
a={ item:price  for item,price in zip(items,prices)}
#zip()可以打包两个列表为一个字典
#首先线建一个作为key的列表，然后建一个作为value的列表，a={key:value for key,value in zip(key列表，value列表)}
print(a)
#如果key列表和value列表元素个数不一样多，会以元素少的列表为基准去创建字典
