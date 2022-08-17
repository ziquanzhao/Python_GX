# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os
snpvcf_path = input('请输入未过滤的snp的vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/8_SNP/')
snp_filname = os.listdir(snpvcf_path)
with open('8_查看过滤参数分布情况.sh', 'a') as snp:
    snp.write('#!/bin/bash\n')
for i in snp_filname:
    if '_snp.vcf' in i:
        name = i.replace('_snp.vcf', '')
        with open('8_查看过滤参数分布情况.sh', 'a') as file:
            file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar VariantsToTable -V {name}_snp.vcf -F CHROM -F POS -F QD -F QUAL -F SOR -F FS -F MQ -F MQRankSum -F ReadPosRankSum -O {name}_snp.table')

