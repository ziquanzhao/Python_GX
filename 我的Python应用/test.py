#coding=utf-8
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

import os
'''
with open('list', 'r') as a :
    bam_filename = a.readlines()
for i in bam_filename:
    for y in range(1,16,1):
        y = str(y)
        a = f'_sort_dedup_chr{y}.gvcf'
        if a in i and 'idx' not in i:
            with open(f'chr{y}.txt', 'a') as chr:
                chr.write(f'-V {i} \n')
'''
print(os.path.isdir('7_snp'))
