# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os

with open('sample.txt', 'r') as sample:
    list = sample.readlines()

with open('fastqc.sh', 'a') as fastaqc:
    fastaqc.write('#!/bin/bash\n')
    for i in list:
        x = i.replace('\n', '')
        fastaqc.write(f'/mnt/storage/zhaoziquan/GWAS/software/FastQC/fastqc  /mnt/data/project/unknown/reseq/bypy/cleandata/{x}_R1.fq.gz -o /mnt/storage4/zzq/FastQC_result/fastqc_result/\n')
        fastaqc.write(f'/mnt/storage/zhaoziquan/GWAS/software/FastQC/fastqc  /mnt/data/project/unknown/reseq/bypy/cleandata/{x}_R2.fq.gz -o /mnt/storage4/zzq/FastQC_result/fastqc_result/\n')


