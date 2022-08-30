# 编写人：赵子权
# 编写时间：2022/8/31 11:19
# 邮箱:2939818719@qq.com
import os

if os.path.exists('8_select_SNP_INDEL_ctg'):
    print('已存在8_select_SNP_INDEL_ctg目录，无需创建')
else:
    os.mkdir('8_select_SNP_INDEL_ctg')

ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
ctgvcf_path = input('请输入最初vcf文件的路径，例如：/mnt/storage/zhaoziquan/GWAS/7_gvcf-vcf_ctg/')
GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')

vcf_filename = os.listdir(ctgvcf_path)

with open('8_select_SNP_ctg.sh', 'a') as select_snp:
    select_snp.write('#!/bin/bash\n')
    for ctgsnp_vcf in vcf_filename:
        if '.vcf' in ctgsnp_vcf:
            ctgsnp_vcf_rename = ctgsnp_vcf.replace('.vcf\n', '')
            select_snp.write(f'java -jar {GATK_sorfware_path} SelectVariants -R {ref_path} -V {ctgvcf_path}{ctgsnp_vcf_rename}.vcf -O {ctgsnp_vcf_rename}_snp.vcf -L {ctgsnp_vcf_rename} --select-type-to-include SNP\n')

with open('8_select_INDEL_ctg.sh', 'a') as select_INDEL:
    select_INDEL.write('#!/bin/bash\n')
    for ctgindel_vcf in vcf_filename:
        if '.vcf' in ctgindel_vcf:
            ctgsindel_vcf_rename = ctgindel_vcf.replace('.vcf\n', '')
            select_snp.write(f'java -jar {GATK_sorfware_path} SelectVariants -R {ref_path} -V {ctgvcf_path}{ctgsindel_vcf_rename}.vcf -O {ctgsindel_vcf_rename}_indel.vcf -L {ctgsindel_vcf_rename} --select-type-to-include INDEL\n')

os.system('mv ./8_select_*_ctg.sh ./8_select_SNP_INDEL_ctg')
print('\033[1;36m在当前目录下，有一个叫8_select_SNP_INDEL_ctg的文件夹，里面有shell脚本，执行它即可\033[m')
