#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/4 9:22
# 邮箱:2939818719@qq.com
import os

if os.path.exists('3_mark_duplicates'):
    print('3_mark_duplicates目录已存在，无需创建')
else:
    os.mkdir('3_mark_duplicates')

bam_path = input('请输入所有标记过重复的bam文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/：')
samtools_software_path = input('请输入samtools软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/samtools-1.15.1/bin/：')
bam_filename = os.listdir(bam_path)

with open('4_bam_index.sh', 'a') as bam_index:
    bam_index.write('#!/bin/bash\n')
    for i in bam_filename:
        name = i.replace('.bam', '')
        bam_index.write(f'{samtools_software_path}samtools index {bam_path}{name}.bam\n')


os.system('mv ./4_bam_index.sh ./3_mark_duplicates')
print('\033[1;36m在当前目录下，有一个叫3_mark_duplicates的文件夹，里面有一个shell脚本，执行它即可\033[m')
