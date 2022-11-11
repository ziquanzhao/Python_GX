#coding=utf-8
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

import os
'''
sample_num = int(input('请告知我您有多少个样本，因为我后续会根据样本量拆解shell脚本，让您多个样本同时计算，以减少时间消耗，例如：200'))
for num in range(2, sample_num, 2):
    os.system(f'sed -i \'{num}a #!/bin/bash\ ./11_hebing_snp_indel.sh')
for head in range(3, sample_num+2, 2):
    os.system(f'head -{head} ./11_hebing_snp_indel.sh > ./11_hebing_snp_indel{head}.sh')


a = '/mnt/storage/zhaoziquan/GWAS/olddata/GEMMA/FM.txt'

print(os.path.splitext(os.path.basename(a))[0])
print(os.path.splitext(os.path.basename(a))[0])
'''
'''
with open('新建文本文档.txt','r') as evm:
    data = evm.readlines()

with open('xso-genegff.gff3','r') as xso:
    gene = xso.readlines()

with open('result.txt','a') as myres:
    for i in gene:
        for x in data:
            if x in i and 'gene' in gene:
                myres.write(i)
'''

with open('E:/Myfile/转录组/11C-1.sam', 'r') as xso:
    data = xso.readlines()