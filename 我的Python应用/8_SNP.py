# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
vcf_path = input('请输入最初vcf文件的路径，例如：/mnt/storage/zhaoziquan/GWAS/7_gvcf-vcf/')
vcf_filename = os.listdir(vcf_path)
if os.path.exists('8_SNP'):
    with open('8_SNP.sh', 'a') as select_snp:
        select_snp.write('#!/bin/bash\n')
    for i in vcf_filename:
        if '.vcf' in i:
            name = i.replace('.vcf', '')
            with open('8_SNP.sh', 'a') as file:
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar SelectVariants -R {ref_path} -V {name}.vcf -O {name}_snp.vcf --select-type-to-include SNP\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar VariantFiltration -V {name}_snp.vcf -O {name}_filt_snp.vcf'
                           f'--missing-values-evaluate-as-failing ' #--missing-values-evaluate-as-failing 当筛选标准比较多的时候，可能有一些位点没有筛选条件当中的一条或几条，例如下面的这个表达式；QUAL < 30.0 || QD < 2.0 || FS > 60.0 || MQ < 40.0 || HaplotypeScore > 13.0 并不一定所有位点都有这些信息，这种情况下GATK运行的时候会报很多WARNING信息，用这个参数可以把这些缺少某些FLAG的位点也给标记成没有通过筛选的。
                           f'--cluster-window-size 10 '       #无争议 --cluster-window-size 以10个碱基为一个窗口
                           f'--cluster-size 3'             #无争议 --cluster-size 10个碱基为窗口，若存在3以上个则过滤
                           f'--filter-name "FS60" -filter "FS > 60.0" '  # FisherStrand (FS): Fisher精确检验评估当前变异是strand bias的可能性，这个值在0-60间
                           f'--filter-name "MQ40" -filter "MQ < 40.0 " '     # RMSMappingQuality (MQ): 所有样本中比对质量的平方根
                           f'--filter-name "QUAL30" -filter "QUAL < 30.0 " '  #无争议
                           f'--filter-name "QD2" -filter "QD < 2" '               #有争议，有1.5的  # QualByDepth(QD): 变异位点可信度除以未过滤的非参考read数
                           f'--filter-name "MQRankSum-12.5" -filter "MQRankSum < -12.5"' # MappingQualityRankSumTest (MQRankSum): 根据REF和ALT的read的比对质量来评估可信度
                           f'--filter-name "ReadPosRankSum-8" -filter "ReadPosRankSum < -8.0"\n') # ReadPosRankSumTest (ReadPosRankSum) : 通过变异在read的位置来评估变异可信度，通常在read的两端的错误率比较高
