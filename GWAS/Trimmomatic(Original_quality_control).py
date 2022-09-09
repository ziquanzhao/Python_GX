# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os
import re

print('\033[0;36m请确保重测序原始的文件命名规则符合：样本ID_R1(R2).fq.gz,如不符合，请在utf-8格式下修改python脚本代码\033[m')

if os.path.exists('trimmomatic'):
    print('已存在trimmomatic目录，无需创建')
else:
    os.mkdir('trimmomatic')

trimmomatic_path = input('请输入trimmomatic软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/Trimmomatic-0.39/trimmomatic-0.39.jar：')
original_fq_data_path = input('请输入重测序的原始fq.gz文件的绝对路径，例如：/mnt/data/project/unknown/reseq/bypy/cleandata/：')
original_fq_data_filename = os.listdir(original_fq_data_path)

with open('trimmomatic.sh', 'a') as trim:
    trim.write('#!/bin/bash\n')
    for filename in original_fq_data_filename:
        if 'R1' in filename:
            filename = re.sub('_R1.fq.gz\n', '', filename)
            trim.write(f'java -jar {trimmomatic_path} PE -threads 60 -phred33 {original_fq_data_path}{filename}_R1.fq.gz {original_fq_data_path}{filename}_R2.fq.gz -baseout {filename}.fq.gz ILLUMINACLIP:/mnt/storage/zhaoziquan/GWAS/software/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10:2:true SLIDINGWINDOW:4:15 LEADING:3 TRAILING:3 MINLEN:36 HEADCROP:5\n')

os.system('mv ./trimmomatic.sh ./trimmomatic')
print('\033[1;36m在当前目录下，有一个叫trimmomatic的文件夹，里面有一个shell脚本，执行它即可\033[m')