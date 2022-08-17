# 编写人：赵子权
# 编写时间：2022/4/26 19:21
# 邮箱:2939818719@qq.com

#任务一是：向文件中输出‘奋斗成就更好的你’

#方法一：使用print
fi=open('E:\\Python\\案例\\案例一：文件输出\\test.txt','a',encoding='utf-8')
print('奋斗成就更好的你\n','你需要更加努力',file=fi)
print('python','\t','python',file=fi)
fi.close()

#方法二：
with open('E:\\Python\\案例\\案例一：文件输出\\test.txt','a',encoding='utf-8') as fi:
    fi.write('奋斗成就更好的你\n你需要更加努力\n')
    fi.write('python\tpython')