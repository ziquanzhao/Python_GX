# 编写人：赵子权
# 编写时间：2022/8/31 21:09
# 邮箱:2939818719@qq.com
import os

if os.path.exists('10_Hard_Filtration'):
    print('已存在10_Hard_Filtration目录，无需创建')
else:
    os.mkdir('10_Hard_Filtration')

ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
snpvcf_path = input('请输入未过滤的snp的vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/8_select_SNP_INDEL/')
GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')
snp_filename = os.listdir(snpvcf_path)

with open('10_Hard_Filtration.sh', '') as hard_filter:
    hard_filter.write('#!/bin/bash\n')
    for snpfile in snp_filename:
        snpfile = snpfile.replace('.vcf\n', '')
        if 'snp' in snpfile:
            hard_filter.write(f'java -jar {GATK_sorfware_path} VariantFiltration -V {snpvcf_path}{snpfile}.vcf -R {ref_path} -filter "QD < 2.0" --filter-name "QD2" -filter "POS < 2.0" --filter-name "POS" -filter "QUAL < 2.0" --filter-name "QUAL" -filter "SOR < 2.0" --filter-name "SOR" -filter "FS < 2.0" --filter-name "FS" -filter "MQ < 2.0" --filter-name "MQ" -filter "MQRankSum < 2.0" --filter-name "MQRankSum" -filter "ReadPosRankSum < 2.0" --filter-name "ReadPosRankSum" -O {snpfile}_filter.vcf')
        else:
            hard_filter.write(f'java -jar {GATK_sorfware_path} VariantFiltration -V {snpvcf_path}{snpfile}.vcf -R {ref_path} -filter "QD < 2.0" --filter-name "QD2" -filter "POS < 2.0" --filter-name "POS" -filter "QUAL < 2.0" --filter-name "QUAL" -filter "SOR < 2.0" --filter-name "SOR" -filter "FS < 2.0" --filter-name "FS" -filter "MQ < 2.0" --filter-name "MQ" -filter "MQRankSum < 2.0" --filter-name "MQRankSum" -filter "ReadPosRankSum < 2.0" --filter-name "ReadPosRankSum" -O {snpfile}_filter.vcf')

os.system('mv ./10_Hard_Filtration.sh ./10_Hard_Filtration/')
print('\033[1;36m在当前目录下，有一个叫10_Hard_Filtration的文件夹，里面有shell脚本，执行它即可\033[m')


