# 编写人：赵子权
# 编写时间：2022/4/22 8:51
# 邮箱:2939818719@qq.com


#单分支结构
#if 条件判断
#   执行操作(仅仅是条件判断为True时才执行，False不执行)
print('------------单分支结构举个例子，取钱------------------------')
money=1000
s=int(input('请输入您的取款金额：'))
if money>=s:
    money=money-s
    print('取款成功，您的余额为：',money)



#双分支结构
#if 条件表达式：
#    条件执行体1
#else：
#   条件表达式2
print('-------双分支举个例子，判断奇偶数-------------')
a=int(input('请输入您所要判断的整数：'))
if a%2==0:
    print('这个数为偶数')
else:
    print('这个数为奇数')


#多分支结构 用于解决连续区间段问题
print('------------判断成绩在哪个区间段------------------------')
num=int(input('请输入您的成绩：'))
if num>=90:
    print('您的成绩大于等于90分')
elif 80<num<90:
    print('您的成绩在80到90之间')
elif 70<num<=80:
    print('您的成绩在70到80之间')
else:
    print('您的成绩在70分以下')


#嵌套if
print('--------------超市买东西用会员卡----------------')
answer=input('你有会员卡吗：')
money=int(input('请输入您的购物金额：'))
if answer=='y':
    if money>=200:
        print('请付款：',money*0.8,'元')
    elif 100<=money<200:
        print('请付款：',money*0.9,'元')
    else:
        print('请付款：',money,'元')
else:
    if money>=200:
        print('请付款：',money*0.9,'元')
    else:
        print('请付款：',money,'元')



