# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

import os

with open('E:\\Myfile\\基因组文件\\xso基因组文件\\xso-gene.fa') as file:
    list = file.readlines()


with open('chrid.txt', 'a') as chr:
    for i in list:
        if '>ctg' in i:
            chr.write(i)
'''          
file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group1 -O {name}_chr1.gvcf\n')

'''
