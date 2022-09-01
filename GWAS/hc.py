# 编写人：赵子权
# 编写时间：2022/8/28 16:25
# 邮箱:2939818719@qq.com
import os
id = input('输入id：')
os.system(f'rm {id}_sort*')

with open(f'{id}.sh', 'a') as file:
    file.write('#!/bin/bash\n')
    for i in range(1, 16, 1):
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{id}_sort_dedup.bam -ERC GVCF -L Lachesis_group{i} -O {id}_sort_dedup_chr{i}.gvcf\n')