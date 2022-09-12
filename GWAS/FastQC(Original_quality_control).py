# coding=utf-8
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os
import re

print('\033[0;36m请确保重测序原始的文件命名规则符合：样本ID_R1(R2).fq.gz,如不符合，请在utf-8格式下修改python脚本代码\033[m')

if os.path.exists('FastQC'):
    print('已存在FastQC目录，无需创建')
else:
    os.mkdir('FastQC')


fastaqc_software_path = input('请输入FastaQC软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/FastQC/fastqc：')
original_fq_data_path = input('请输入重测序的原始fq.gz文件的绝对路径，例如：/mnt/data/project/unknown/reseq/bypy/cleandata/：')

original_fq_data_filename = os.listdir(original_fq_data_path)
with open('fastqc.sh', 'a') as fastaqc:
    fastaqc.write('#!/bin/bash\n')
    for filename in original_fq_data_filename:
        if 'R1' in filename:
            filename = re.sub('_R1.fq.gz', '', filename)
            fastaqc.write(f'/mnt/storage/zhaoziquan/GWAS/software/FastQC/fastqc  /mnt/data/project/unknown/reseq/bypy/cleandata/{filename}_R1.fq.gz -o ./\n')
            fastaqc.write(f'/mnt/storage/zhaoziquan/GWAS/software/FastQC/fastqc  /mnt/data/project/unknown/reseq/bypy/cleandata/{filename}_R2.fq.gz -o ./\n')

os.system('mv ./fastqc.sh ./FastQC')
print('\033[1;36m在当前目录下，有一个叫FastQC的文件夹，里面有一个shell脚本，执行它即可\033[m')


