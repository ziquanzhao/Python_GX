# 编写人：赵子权
# 编写时间：2022/8/31 20:39
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('11_hebing_snp_indel'):
    print('已经存在11_hebing_snp_indel目录，无需创建了')
else:
    os.mkdir('11_hebing_snp_indel')

GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')
Filtration_vcf_path = input('请输入过滤后但snp和indel分开的vcf文件所在绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/10_Hard_Filtration/：')
filtration_vcf_filename = os.listdir(Filtration_vcf_path)


with open('11_hebing_snp_indel.sh', 'a') as snpindel:
    snpindel.write('#!/bin/bash\n')
    for filename in filtration_vcf_filename:
        if 'filter' not in filename and '.idx' not in filename and 'snp' in filename:
            filename = re.sub('_snp.vcf', '', filename)
            snpindel.write(f'java -jar {GATK_sorfware_path} MergeVcfs -I {Filtration_vcf_path}{filename}_snp.vcf -I {Filtration_vcf_path}{filename}_indel.vcf -O {filename}_final_164.vcf\n')

os.system('mv ./11_hebing_snp_indel.sh ./11_hebing_snp_indel/')
print('\033[1;36m在当前目录下，有一个叫11_hebing_snp_indel的文件夹，里面有一个shell脚本，执行它即可\033[m')