# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os

if os.path.exists('9_View_SNP_INDEL_distribution'):
    print('已存在9_View_SNP_INDEL_distribution目录，无需创建')
else:
    os.mkdir('9_View_SNP_INDEL_distribution')

snpvcf_path = input('请输入未过滤的snp的vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/8_select_SNP_INDEL/:')
snp_filename = os.listdir(snpvcf_path)

with open('9_View_SNP_INDEL_distribution.sh', 'a') as snp_indel:
    snp_indel.write('#!/bin/bash\n')
    for i in snp_filename:
        if '_snp.vcf' in i and '.idx' not in i:
            snpvcf_filename = i.replace('_snp.vcf\n', '')
            snp_indel.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar VariantsToTable -V {snpvcf_path}{snpvcf_filename}_snp.vcf -F CHROM -F POS -F QD -F QUAL -F SOR -F FS -F MQ -F MQRankSum -F ReadPosRankSum -O {snpvcf_filename}_snp.recode.table')
            snp_indel.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar VariantsToTable -V {snpvcf_path}{snpvcf_filename}_indel.vcf -F CHROM -F POS -F QD -F QUAL -F SOR -F FS -F MQ -F MQRankSum -F ReadPosRankSum -O {snpvcf_filename}_indel.recode.table')

os.system('mv ./9_View_SNP_INDEL_distribution.sh ./9_View_SNP_INDEL_distribution/')
print('\033[1;36m在当前目录下，有一个叫9_View_SNP_INDEL_distribution的文件夹，里面有shell脚本，执行它即可\033[m')
