# coding=utf-8
# 编写人：赵子�?
# 编写时间�?022/7/1 10:41
# 邮箱:2939818719@qq.com
import os


if os.path.exists('1_bwaindex'):
    print('1_bwaindex目录已存在，无需创建')
else:
    os.mkdir('1_bwaindex')

cankaopath = input('请输入参考基因组文件的绝对路径，例如：/mnt/storage/zhaoziquan/KCS/基因组文件/：')
cankaoname = input('请输入参考基因组的文件名，例如：xso-gene.fa:')
index_name = input('为您的参考基因组索引起一个前缀名，注意是前缀名。例如：xsoindex：')
bwa_software_path = input('请输入bwa软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/Bwa/：')
samtools_software_path = input('请输入samtools软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/samtools-1.15.1/bin/：')
GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')

with open('1_bwaindex.sh', 'a') as bwa_index:
    bwa_index.write('#!/bin/bash\n')
    bwa_index.write(f'{bwa_software_path}bwa index -a bwtsw -p {index_name} {cankaopath}\n')
    bwa_index.write(f'{samtools_software_path}samtools faidx {cankaopath}\n')
    bwa_index.write(f'java -jar {GATK_sorfware_path} CreateSequenceDictionary -REFERENCE {cankaopath} -OUTPUT {cankaoname}.dict')

os.system('mv ./1_bwaindex.sh ./1_bwaindex')
print('\033[m在当前目录下有一个叫1_bwaindex的文件夹，里面有一个shell脚本，执行它即可\033[m')
