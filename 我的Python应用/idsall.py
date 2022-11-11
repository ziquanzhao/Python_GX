# 缂栧啓浜猴細璧靛瓙鏉?
# 缂栧啓鏃堕棿锛?022/4/30 19:55
# 閭:2939818719@qq.com

import os
import time

ids1 = input('id1s=:')
'''
ids2 = input('ids2=:')
ids3 = input('ids3=:')
ids4 = input('ids4=:')
ids5 = input('ids5=:')
ids6 = input('ids6=:')
ids7 = input('ids7=:')
ids8 = input('ids8=:')
ids9 = input('ids9=:')
ids10 = input('ids10=:')
ids11 = input('ids11=:')
ids12 = input('ids12=:')
ids13 = input('ids13=:')
ids14 = input('ids14=:')
ids15 = input('ids15=:')
'''

for a in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids1}_sort_dedup.bam -ERC GVCF -L Lachesis_group{a} -O {ids1}_sort_dedup_chr{a}.g.vcf >> nohup.log 2>&1 &')
'''
time.sleep(60)
for b in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids2}_sort_dedup.bam -ERC GVCF -L Lachesis_group{b} -O {ids2}_sort_dedup_chr{b}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for c in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids3}_sort_dedup.bam -ERC GVCF -L Lachesis_group{c} -O {ids3}_sort_dedup_chr{c}.g.vcf >> nohup.log 2>&1 &')
time.sleep(10000)
for d in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids4}_sort_dedup.bam -ERC GVCF -L Lachesis_group{d} -O {ids4}_sort_dedup_chr{d}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for e in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids5}_sort_dedup.bam -ERC GVCF -L Lachesis_group{e} -O {ids5}_sort_dedup_chr{e}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for f in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids6}_sort_dedup.bam -ERC GVCF -L Lachesis_group{f} -O {ids6}_sort_dedup_chr{f}.g.vcf >> nohup.log 2>&1 &')
time.sleep(10000)
for g in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids7}_sort_dedup.bam -ERC GVCF -L Lachesis_group{g} -O {ids7}_sort_dedup_chr{g}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for h in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids8}_sort_dedup.bam -ERC GVCF -L Lachesis_group{h} -O {ids8}_sort_dedup_chr{h}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for i in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids9}_sort_dedup.bam -ERC GVCF -L Lachesis_group{i} -O {ids9}_sort_dedup_chr{i}.g.vcf >> nohup.log 2>&1 &')
time.sleep(10000)
for j in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids10}_sort_dedup.bam -ERC GVCF -L Lachesis_group{j} -O {ids10}_sort_dedup_chr{j}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for k in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids11}_sort_dedup.bam -ERC GVCF -L Lachesis_group{k} -O {ids11}_sort_dedup_chr{k}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for l in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids12}_sort_dedup.bam -ERC GVCF -L Lachesis_group{l} -O {ids12}_sort_dedup_chr{l}.g.vcf >> nohup.log 2>&1 &')
time.sleep(10000)
for m in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids13}_sort_dedup.bam -ERC GVCF -L Lachesis_group{m} -O {ids13}_sort_dedup_chr{m}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for n in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids14}_sort_dedup.bam -ERC GVCF -L Lachesis_group{n} -O {ids14}_sort_dedup_chr{n}.g.vcf >> nohup.log 2>&1 &')
time.sleep(60)
for o in range(1,16,1):
    os.system(f'nohup java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R /mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa -I /mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/{ids15}_sort_dedup.bam -ERC GVCF -L Lachesis_group{o} -O {ids15}_sort_dedup_chr{o}.g.vcf >> nohup.log 2>&1 &')
'''