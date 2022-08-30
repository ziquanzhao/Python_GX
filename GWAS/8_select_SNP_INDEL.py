# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os

if os.path.exists('8_select_SNP_INDEL'):
    print('已存在8_select_SNP_INDEL目录，无需创建')
else:
    os.mkdir('8_select_SNP_INDEL')

ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
vcf_path = input('请输入最初vcf文件的路径，例如：/mnt/storage/zhaoziquan/GWAS/7_gvcf-vcf/')
GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')

vcf_filename = os.listdir(vcf_path)

with open('8_select_SNP.sh', 'a') as select_snp:
    select_snp.write('#!/bin/bash\n')
    for i in vcf_filename:
        if '.vcf' in i:
            vcf_new_name = i.replace('.vcf\n', '')
            vcf_id_name = vcf_new_name.replace('chr', '')
            select_snp.write(f'java -jar {GATK_sorfware_path} SelectVariants -R {ref_path} -V {vcf_path}{vcf_new_name}.vcf -O {vcf_new_name}_snp.vcf -L Lachesis_group{vcf_id_name} --select-type-to-include SNP\n')

with open('8_select_INDEL.sh', 'a') as select_INDEL:
    select_INDEL.write('#!/bin/bash\n')
    for i in vcf_filename:
        if '.vcf' in i:
            vcf_new_name = i.replace('.vcf\n', '')
            vcf_id_name = vcf_new_name.replace('chr', '')
            select_snp.write(f'java -jar {GATK_sorfware_path} SelectVariants -R {ref_path} -V {vcf_path}{vcf_new_name}.vcf -O {vcf_new_name}_indel.vcf -L Lachesis_group{vcf_id_name} --select-type-to-include INDEL\n')
