# 编写人：赵子权
# 编写时间：2022/8/31 11:19
# 邮箱:2939818719@qq.com
import os

if os.path.exists('8_select_SNP_INDEL'):
    print('已存在8_select_SNP_INDEL目录，无需创建')
else:
    os.mkdir('8_select_SNP_INDEL')

ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
ctgvcf_filepath = input('请输入ctg_zhb文件的路径，例如：/mnt/storage/zhaoziquan/GWAS/7_gvcf-vcf_ctg_zhb/ctg.vcf')
GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')

with open('8_select_SNP_ctg.sh', 'a') as select_snp:
    select_snp.write('#!/bin/bash\n')
    select_snp.write(f'java -jar {GATK_sorfware_path} SelectVariants -R {ref_path} -V {ctgvcf_filepath} -O ctg_snp.vcf --select-type-to-include SNP\n')

with open('8_select_INDEL_ctg.sh', 'a') as select_INDEL:
    select_INDEL.write('#!/bin/bash\n')
    select_snp.write(f'java -jar {GATK_sorfware_path} SelectVariants -R {ref_path} -V {ctgvcf_filepath} -O ctg_indel.vcf --select-type-to-include INDEL\n')

os.system('mv ./8_select_*_ctg.sh ./8_select_SNP_INDEL')
print('\033[1;36m在当前目录下，有一个叫8_select_SNP_INDEL的文件夹，里面有shell脚本，执行它即可\033[m')
