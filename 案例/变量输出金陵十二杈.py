# 编写人：赵子权
# 编写时间：2022/4/26 19:58
# 邮箱:2939818719@qq.com
#方法一：
name1='林黛玉'
name2='薛宝钗'
name3='史湘云'
with open('E:\\Python\\案例\\test.txt','a',encoding='utf-8') as fi:
    print('①',name1,file=fi)
    print('②',name2,file=fi)
    print('③',name3,file=fi)


#方法二：
lst1=['林黛玉','薛宝钗','史湘云']
lst2=['①','②','③']
with open('E:\\Python\\案例\\test.txt','a',encoding='utf-8') as fi:
    for i in range(0,3,1):
        fi.write('\n')
        fi.write(lst2[i])
        fi.write('\t')
        fi.write(lst1[i])
    print('\n', file=fi)

lst1 = ['林黛玉', '薛宝钗', '史湘云']
lst2 = ['①', '②', '③']
with open('E:\\Python\\案例\\test.txt', 'a', encoding='utf-8') as fi:
    for i in range(0, 3, 1):
        print(lst2[i],lst1[i],file=fi)


#方法三：
dic={'①':'林黛玉','②':'薛宝钗','③':'史湘云'}
with open('E:\\Python\\案例\\test.txt', 'a', encoding='utf-8') as fi:
    for key in dic:
        print(key,dic[key],file=fi)

#方法四：
lst1 = ['林黛玉', '薛宝钗', '史湘云']
lst2 = ['①', '②', '③']
with open('E:\\Python\\案例\\test.txt', 'a', encoding='utf-8') as fi:
    for sing,name in zip(lst2,lst1):
        print(sing,name,file=fi)




