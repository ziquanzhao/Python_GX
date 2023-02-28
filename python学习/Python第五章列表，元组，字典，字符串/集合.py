# 编写人：赵子权
# 编写时间：2022/4/24 15:35
# 邮箱:2939818719@qq.com

'''
1.可变序列
2.集合是没有value的字典，也是通过哈希函数计算key
3.集合是无序的，不允许重复
'''

#集合的创建---方法一：
s={2,3,5,6,6}  #集合元素不许重复
print(s)

#集合的创建---方法二：
s=set(range(5))
print(s)
print(set([1,2,3]))   #把列表转换为集合
print(set((1,2,3)))   #把元组转换为集合
print(set({1:2,2:2,3:2}))  #把字典的key转换为集合，集合本身就是没有value的字典

#定义一个空集合
a=set()   #不能使用a={}，这样会被认为是字典

#集合元素的判断
print(2 in s)
print(3 not in s)

#集合元素的增加
s.add(5)  #一次增加一个元素
print(s)
s.update({200,300})
s.update([2,5])
s.update((5,9))
print(s)    #update可以一次增加多个元素

#s.update(10,20)  #会报错，元素变成【】，（），{}再去添加
#print(s)

#集合元素的删除
s.remove(1)   #删除元素1
print(s)
s.pop()   #删除任意一个元素，pop不能添加参数
print(s)
s.clear()  #清空集合元素
print(s)

#集合之间的关系判断
s1={1,2,3}
s2={2,3,4}
print(s1==s2)  #判断两个集合是否相等，集合是无序的，元素相等即可，无需顺序一样
print(s1.issubset(s2))   #s1是s2的子集吗？
print(s1.issuperset(s2))   #s1是s2的超集吗？
print(s1.isdisjoint(s2))   #s1与s2有交集吗？

#集合的数学操作
print(s1.intersection(s2))  #求s1与s2的交集
print(s1 & s2)   #求s1与s2的交集

print(s1.union(s2))  #求s1与s2的并集
print(s1 | s2)    #求s1与s2的并集

print(s1.difference(s2))   #求s1与s2的差集
print(s1-s2)    #求s1与s2的差集

#集合生成式
a={i for i in range(6)}
print(a)
#集合生成式和列表生成式基本一样，只是把【】变成{}而已