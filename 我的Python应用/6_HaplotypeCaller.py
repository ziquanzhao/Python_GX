#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/5 17:00
# 邮箱:2939818719@qq.com
import os
bam_dedup_path = input('请输入所有bam文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
bam_filename = os.listdir(bam_dedup_path)
if os.path.exists('6_HaplotypeCaller'):
    with open('6_HaplotypeCaller.sh', 'a') as HaplotypeCaller:
        HaplotypeCaller.write('#!/bin/bash\n')
    for i in bam_filename:
        if i.find('bai') == -1 and i.find('metrics') == -1:
            name = i.replace('.bam', '')
            with open('6_HaplotypeCaller.sh', 'a') as file:
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group1 -O {name}_chr1.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group2 -O {name}_chr2.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group3 -O {name}_chr3.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group4 -O {name}_chr4.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group5 -O {name}_chr5.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group6 -O {name}_chr6.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group7 -O {name}_chr7.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group8 -O {name}_chr8.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group9 -O {name}_chr9.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group10 -O {name}_chr10.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group11 -O {name}_chr11.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group12 -O {name}_chr12.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group13 -O {name}_chr13.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group14 -O {name}_chr14.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group15 -O {name}_chr15.gvcf\n')
else:
    os.mkdir('6_HaplotypeCaller')
    with open('6_HaplotypeCaller.sh', 'a') as BQSR_bam:
        BQSR_bam.write('#!/bin/bash\n')
    for i in bam_filename:
        if i.find('bai') == -1 and i.find('metrics') == -1:
            name = i.replace('.bam', '')
            with open('6_HaplotypeCaller.sh', 'a') as file:
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group1 -O {name}_chr1.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group2 -O {name}_chr2.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group3 -O {name}_chr3.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group4 -O {name}_chr4.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group5 -O {name}_chr5.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group6 -O {name}_chr6.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group7 -O {name}_chr7.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group8 -O {name}_chr8.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group9 -O {name}_chr9.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group10 -O {name}_chr10.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group11 -O {name}_chr11.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group12 -O {name}_chr12.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group13 -O {name}_chr13.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group14 -O {name}_chr14.gvcf\n')
                file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group15 -O {name}_chr15.gvcf\n')

os.system('mv ./6_HaplotypeCaller.sh ./6_HaplotypeCaller')
print('\033[1;36m在当前目录下，有一个叫6_HaplotypeCaller的文件夹，里面有一个shell脚本，执行它即可\033[m')
