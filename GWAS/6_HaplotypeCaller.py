#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/5 17:00
# 邮箱:2939818719@qq.com
import os
import re

if os.path.exists('6_HaplotypeCaller'):
    print('6_HaplotypeCaller目录已存在，无需创建')
else:
    os.mkdir('6_HaplotypeCaller')

bam_dedup_path = input('请输入所有bam文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')

bam_filename = os.listdir(bam_dedup_path)

with open('6_HaplotypeCaller.sh', 'a') as HaplotypeCaller:
    HaplotypeCaller.write('#!/bin/bash\n')
    for i in bam_filename:
        if 'bai' not in i and 'metrics' not in i:
            name = re.sub('.bam', '', i)
            for Lachesis_group in range(1, 16, 1):
                HaplotypeCaller.write(f'java -jar {GATK_sorfware_path} HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group{Lachesis_group} -O {name}_chr{Lachesis_group}.g.vcf\n')

os.system('mv ./6_HaplotypeCaller.sh ./6_HaplotypeCaller')
print('\033[1;36m在当前目录下，有一个叫6_HaplotypeCaller的文件夹，里面有一个shell脚本，执行它即可\033[m')
