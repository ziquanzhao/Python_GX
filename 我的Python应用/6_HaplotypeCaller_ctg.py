#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/5 17:00
# 邮箱:2939818719@qq.com
import os
bam_dedup_path = input('请输入所有bam文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
bam_filename = os.listdir(bam_dedup_path)
if os.path.exists('6_HaplotypeCaller'):
    with open('6_HaplotypeCaller.sh', 'a') as HaplotypeCaller:
        HaplotypeCaller.write('#!/bin/bash\n')
    for i in bam_filename:
        if i.find('bai') == -1 and i.find('metrics') == -1:
            name = i.replace('.bam', '')
            with open('6_HaplotypeCaller.sh', 'a') as file:
                with open('chrid.txt', 'r') as chrid:
                    chrid_list = chrid.readlines()
                    for x in chrid_list:
                        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L {x} -O {name}_chr1.gvcf\n')

