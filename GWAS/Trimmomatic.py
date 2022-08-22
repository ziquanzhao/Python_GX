# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os
import shutil

with open('sample.txt', 'r') as sample:
    list = sample.readlines()

with open('trimmomatic.sh', 'a') as trim:
    trim.write('#!/bin/bash\n')
    for i in list:
        x = i.replace('\n', '')
        trim.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/Trimmomatic-0.39/trimmomatic-0.39.jar PE -threads 60 -phred33 /mnt/data/project/unknown/reseq/bypy/cleandata/{x}_R1.fq.gz /mnt/data/project/unknown/reseq/bypy/cleandata/{x}_R2.fq.gz -baseout {x}.fq.gz ILLUMINACLIP:/mnt/storage/zhaoziquan/GWAS/software/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10:2:true SLIDINGWINDOW:4:15 LEADING:3 TRAILING:3 MINLEN:36 HEADCROP:5\n')

os.mkdir('zzq_chean_data')
os.system('mv trimmomatic.sh ./zzq_clean_data/')
print('当前目录下有一个zzq_clean_data目录，运行其文件夹下的shell脚本即可')


