#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/5 17:00
# 邮箱:2939818719@qq.com
import os
import re

if os.path.exists('6_HaplotypeCaller_ctg'):
    print('已存在6_HaplotypeCaller_ctg目录，无需创建')
else:
    os.mkdir('6_HaplotypeCaller_ctg')

if os.path.exists('6_HaplotypeCaller_ctg_sh'):
    print('已存在6_HaplotypeCaller_ctg_sh目录，无需创建')
else:
    os.mkdir('6_HaplotypeCaller_ctg_sh')

bam_dedup_path = input('请输入所有bam文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')

bam_name = os.listdir(bam_dedup_path)

with open('ctgid.txt', 'r') as ctgid:
    ctg_name = ctgid.readlines()

for i in bam_name:
    if 'bai' not in i and 'metrics' not in i:
        bam_new_name= re.sub('_sort_dedup.bam', '', i)
        with open(f'6_HC_{bam_new_name}.sh', 'a') as hc_ctg:
            hc_ctg.write('#!/bin/bash\n')
            for ctg in ctg_name:
                ctg = ctg.replace('\n', '')
                ctg = ctg.replace('>', '')
                hc_ctg.write(f'java -jar {GATK_sorfware_path} HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{bam_new_name}_sort_dedup.bam -ERC GVCF -L {ctg} -O {bam_new_name}_sort_dedup_{ctg}.g.vcf\n')


os.system('mv ./6_HC_*.sh ./6_HaplotypeCaller_ctg_sh')
print('请去6_HaplotypeCaller_ctg_sh目录寻找shell脚本，执行它们，注意把结果输出到6_HaplotypeCaller_ctg文件夹里')