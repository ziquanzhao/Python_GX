# 编写人：赵子权
# 编写时间：2022/8/31 20:07
# 邮箱:2939818719@qq.com
import os

if os.path.isdir('7_gvcf-vcf_ctg_zhb'):
    print('已经存在7_gvcf-vcf_ctg_zhb目录，无需创建了')
else:
    os.mkdir('7_gvcf-vcf_ctg_zhb')

ctg_vcf_path = input('请输入ctg*.vcf文件所在绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/7_gvcf-vcf_ctg/：')

with open('ctgid.txt', 'r') as ctgid:
    ctg_list = []
    for ctg in ctgid:
        ctg = ctg.replace('\n', '')
        ctg = ctg.replace('>', '')
        ctg_list.append(f'-I {ctg_vcf_path}{ctg}.vcf')
    ctg_list2 = ' '.join(ctg_list)
with open('7_gvcf-vcf_ctg_zhb.sh', 'a') as ctg_zhb:
    ctg_zhb.write('#!/bin/bash\n')
    ctg_zhb.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar MergeVcfs {ctg_list2} -O ctg.vcf')

os.system('mv ./7_gvcf-vcf_ctg_zhb.sh ./7_gvcf-vcf_ctg_zhb/')
print('\033[1;36m在当前目录下，有一个叫7_gvcf-vcf_ctg_zhb的文件夹，里面有一个shell脚本，执行它即可\033[m')
