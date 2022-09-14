# 编写人：赵子权
# 编写时间：2022/9/14 8:58
# 邮箱:2939818719@qq.com
import os
import re

'''
with open('ctgid.txt', 'r') as grep:     #这部分用于查看snp个数
    with open('grep.sh', 'a') as ctg:
        ctg.write('#!/bin/bash\n')
        for ctgname in grep:
            ctgname = re.sub('>', '', ctgname)
            ctgname = re.sub('\n', '', ctgname)
            ctg.write(f'echo \'{ctgname}\'\n')
            ctg.write(f'grep -o \'{ctgname}\' /mnt/storage/zhaoziquan/GWAS/11_hebing_snp_indel/ctg_final_164.vcf | wc -l\n')
'''
a = open('nohup.out', 'r')    #这部分用于修改nohup.out文件，让他变成两列，方便筛选
list = a.readlines()
with open('nohup2.txt', 'a') as nohup2:
    for i in range(0, 4618, 2):
        x = list[i].replace('\n', '')
        b = i + 1
        y = list[b].replace('\n', '')
        nohup2.write(f'{x}\t{y}\n')

os.system('awk \'$2<5{print$1}\' ./nohup2.txt > nohup3.txt') #这一部分是根据ctg的snp个数，把个数小于4（设置$2<5是因为注释文件中还有一个ctgid的）的ctg从vcf文件中删除掉。
with open('sed.sh', 'a') as sed:
    sed.write('#!/bin/bash\n')
    with open('nohup3.txt', 'r') as nohup5:
        for i in nohup5:
            i = i.replace('\n', '')
            sed.write(f'sed -i \'/{i}/d\' /mnt/storage/zhaoziquan/GWAS/11_hebing_snp_indel/ctg_final_164.vcf\n')


#基因型填补时，ctg部分有很多ctg太短了，只有很少的snp位点（小于4个），这导致利用beagle填补时会报错，这个程序就是为了查看每个ctg有多少个snp位点。
#注意，请务必把命令放置后台运行，日志文件名必须是nohup.out
#注意这三部分不能同时运行，先运行第一部分，把二三部分注释掉，然后再反过来运行。
'''
sort  -n  -k  3  -t  \  file.txt
-r 降序
-u 删除重复值，就是uniq
-n  按照数字大小
-k  按照第3列
-t  分隔符按照 \

grep
-o 把匹配的字符串输出，每个一行，配合wc -l，就可以知道文件中有多少个字符串了。
'''