# 编写人：赵子权
# 编写时间：2022/8/28 11:43
# 邮箱:2939818719@qq.com
with open('gvcflist2.txt', 'r') as gvcf:
    list = gvcf.readlines()

with open('rename.sh', 'a') as rename:
    rename.write('#!/bin/bash\n')
    for i in list:
        i = i.replace('\n', '')
        for y in range(1, 16, 1):
            a = f'\'{i}_sort_dedup_chr{y}.gvcf\'$\'\\r\''
            b = f'\'{i}_sort_dedup_chr{y}.gvcf.idx\'$\'\\r\''
            c = f'\'{i}_sort_dedup_chr{y}.gvcf\'$\'\\r\'\'.idx\''
            rename.write(f'mv /mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/{a} /mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/{i}_sort_dedup_chr{y}.gvcf\n')
            rename.write(f'mv /mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/{b} /mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/{i}_sort_dedup_chr{y}.gvcf.idx\n')
            rename.write(f'mv /mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/{c} /mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/{i}_sort_dedup_chr{y}.gvcf.idx\n')

