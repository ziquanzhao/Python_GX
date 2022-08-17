#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/4 9:42
# 邮箱:2939818719@qq.com
import os
bam_dedup_path = input('请输入所有bam文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/KCS/基因组文件/xso-gene.fa：')
knownsites_path = input('请输入已知indel区域的vcf文件的绝对路径：')
bam_filename = os.listdir(bam_dedup_path)
if os.path.exists('5_BQSR_bam'):
    with open('5_BQSR_bam.sh', 'a') as BQSR_bam:
        BQSR_bam.write('#!/bin/bash\n')
    for i in bam_filename:
        if i.find('bai') == '-1' and i.find('metrics') == '-1':
            name = i.replace('.bam', '')
            with open('5_BQSR_bam.sh', 'a') as file:
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar BaseRecalibrator -R {ref_path} -I {bam_dedup_path}{name}.bam -knownSites {knownsites_path} -O {name}_recal.table\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar PrintReads -R {ref_path} -I {bam_dedup_path}{name}.bam -BQSR ./{name}_recal.table -O {name}_recal.bam\n')
else:
    os.mkdir('5_BQSR_bam')
    with open('5_BQSR_bam.sh', 'a') as BQSR_bam:
        BQSR_bam.write('#!/bin/bash\n')
    for i in bam_filename:
        if i.find('bai') == '-1' and i.find('metrics') == '-1':
            name = i.replace('.bam', '')
            with open('5_BQSR_bam.sh', 'a') as file:
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar BaseRecalibrator -R {ref_path} -I {bam_dedup_path}{name}.bam -knownSites {knownsites_path} -O {name}_recal.table\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar PrintReads -R {ref_path} -I {bam_dedup_path}{name}.bam -BQSR ./{name}_recal.table -O {name}_recal.bam\n')




os.system('mv ./5_BQSR_bam.sh ./5_BQSR_bam')
print('\033[1;36m在当前目录下，有一个叫5_BQSR_bam的文件夹，里面有一个shell脚本，执行它即可\033[m')
