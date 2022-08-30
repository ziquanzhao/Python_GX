# 编写人：赵子权
# 编写时间：2022/8/31 9:53
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('7_gvcf-vcf_ctg'):
    print('已经存在7_gvcf-vcf_ctg目录，无需创建了')
else:
    os.mkdir('7_gvcf-vcf_ctg')

all_gvcf = input('请输入所有gvcf文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
filename = os.listdir(all_gvcf)


with open('ctgid.txt', 'r') as ctgid:
    for ctg in ctgid:
        ctg = ctg.replace('\n', '')
        ctg = ctg.replace('>', '')
        with open(f'{ctg}.sh', 'a') as ctg_vcf:
            ctg_vcf.write('#!/bin/bash\n')
            sample_list = []
            for sample in filename:
                if '.idx' not in sample:
                    sample = re.sub('_sort_dedup_chr\d*.gvcf', '', sample)
                    sample_list = sample_list.append(f'-V {sample}_sort_dedup_{ctg}.gvcf ')
            ctg_vcf.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {sample_list} -O all_{ctg}.g.vcf\n')
            ctg_vcf.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_{ctg}.g.vcf -O {ctg}.vcf\n')


os.system('mv ./ctg*.sh ./7_gvcf-vcf_ctg')
print('\033[1;36m在当前目录下，有一个叫7_gvcf-vcf_ctg的文件夹，里面的shell脚本，执行它即可\033[m')
