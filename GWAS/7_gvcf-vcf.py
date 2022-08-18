#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/5 20:32
# 邮箱:2939818719@qq.com
import os
bam_dedup_path = input('请输入所有gvcf文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/KCS/基因组文件/xso-gene.fa：')
bam_filename = os.listdir(bam_dedup_path)
if os.path.exists('7_gvcf-vcf'):
    with open('7_gvcf-vcf.sh', 'a') as gvcf_vcf:
        gvcf_vcf.write('#!/bin/bash\n')
    for i in bam_filename:
        if 'chr1' in i and 'idx' not in i:
            with open('chr1.txt', 'a') as chr1:
                chr1.write('-V i\0')
        elif 'chr2' in i and 'idx' not in i:
            with open('chr2.txt', 'a') as chr2:
                chr2.write('-V i\0')
        elif 'chr3' in i and 'idx' not in i:
            with open('chr3.txt', 'a') as chr3:
                chr3.write('-V i\0')
        elif 'chr4' in i and 'idx' not in i:
            with open('chr4.txt', 'a') as chr4:
                chr4.write('-V i\0')
        elif 'chr5' in i and 'idx' not in i:
            with open('chr5.txt', 'a') as chr5:
                chr5.write('-V i\0')
        elif 'chr6' in i and 'idx' not in i:
            with open('chr6.txt', 'a') as chr6:
                chr6.write('-V i\0')
        elif 'chr7' in i and 'idx' not in i:
            with open('chr7.txt', 'a') as chr7:
                chr7.write('-V i\0')
        elif 'chr8' in i and 'idx' not in i:
            with open('chr8.txt', 'a') as chr8:
                chr8.write('-V i\0')
        elif 'chr9' in i and 'idx' not in i:
            with open('chr9.txt', 'a') as chr9:
                chr9.write('-V i\0')
        elif 'chr10' in i and 'idx' not in i:
            with open('chr10.txt', 'a') as chr10:
                chr10.write('-V i\0')
        elif 'chr11' in i and 'idx' not in i:
            with open('chr11.txt', 'a') as chr11:
                chr11.write('-V i\0')
        elif 'chr12' in i and 'idx' not in i:
            with open('chr12.txt', 'a') as chr12:
                chr2.write('-V i\0')
        elif 'chr13' in i and 'idx' not in i:
            with open('chr13.txt', 'a') as chr13:
                chr13.write('-V i\0')
        elif 'chr14' in i and 'idx' not in i:
            with open('chr14.txt', 'a') as chr14:
                chr14.write('-V i\0')
        elif 'chr15' in i and 'idx' not in i:
            with open('chr15.txt', 'a') as chr15:
                chr15.write('-V i\0')

    chr1_1 = open('chr1.txt', 'r')
    chr1_2 = chr1_1.readline()
    chr1_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr1_2} -O all_chr1.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr1.gvcf -O chr1.vcf\n')
        file.write('rm ./all_chr1.gvcf\n')

    chr2_1 = open('chr2.txt', 'r')
    chr2_2 = chr2_1.readline()
    chr2_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr2_2} -O all_chr2.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr2.gvcf -O chr2.vcf\n')
        file.write('rm ./all_chr2.gvcf\n')

    chr3_1 = open('chr3.txt', 'r')
    chr3_2 = chr3_1.readline()
    chr3_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr3_2} -O all_chr3.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr3.gvcf -O chr3.vcf\n')
        file.write('rm ./all_chr3.gvcf\n')

    chr4_1 = open('chr4.txt', 'r')
    chr4_2 = chr4_1.readline()
    chr4_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr4_2} -O all_chr4.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr4.gvcf -O chr4.vcf\n')
        file.write('rm ./all_chr4.gvcf\n')

    chr5_1 = open('chr5.txt', 'r')
    chr5_2 = chr5_1.readline()
    chr5_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr5_2} -O all_chr5.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr5.gvcf -O chr5.vcf\n')
        file.write('rm ./all_chr5.gvcf\n')

    chr6_1 = open('chr6.txt', 'r')
    chr6_2 = chr6_1.readline()
    chr6_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr6_2} -O all_chr6.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr6.gvcf -O chr6.vcf\n')
        file.write('rm ./all_chr6.gvcf\n')

    chr7_1 = open('chr7.txt', 'r')
    chr7_2 = chr7_1.readline()
    chr7_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr7_2} -O all_chr7.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr7.gvcf -O chr7.vcf\n')
        file.write('rm ./all_chr7.gvcf\n')

    chr8_1 = open('chr8.txt', 'r')
    chr8_2 = chr8_1.readline()
    chr8_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr8_2} -O all_chr8.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr8.gvcf -O chr8.vcf\n')
        file.write('rm ./all_chr8.gvcf\n')

    chr9_1 = open('chr9.txt', 'r')
    chr9_2 = chr9_1.readline()
    chr9_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr9_2} -O all_chr9.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr9.gvcf -O chr9.vcf\n')
        file.write('rm ./all_chr9.gvcf\n')

    chr10_1 = open('chr10.txt', 'r')
    chr10_2 = chr10_1.readline()
    chr10_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr10_2} -O all_chr10.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr10.gvcf -O chr10.vcf\n')
        file.write('rm ./all_chr10.gvcf\n')

    chr11_1 = open('chr11.txt', 'r')
    chr11_2 = chr11_1.readline()
    chr11_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr11_2} -O all_chr11.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr11.gvcf -O chr11.vcf\n')
        file.write('rm ./all_chr11.gvcf\n')

    chr12_1 = open('chr12.txt', 'r')
    chr12_2 = chr12_1.readline()
    chr12_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr12_2} -O all_chr12.gvcf \n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr12.gvcf -O chr12.vcf\n')
        file.write('rm ./all_chr13.gvcf\n')

    chr13_1 = open('chr13.txt', 'r')
    chr13_2 = chr13_1.readline()
    chr13_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr13_2} -O all_chr13.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr13.gvcf -O chr13.vcf\n')
        file.write('rm ./all_chr14.gvcf\n')

    chr14_1 = open('chr14.txt', 'r')
    chr14_2 = chr14_1.readline()
    chr14_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr14_2} -O all_chr14.gvcf \n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr14.gvcf -O chr14.vcf\n')
        file.write('rm ./all_chr15.gvcf\n')

    chr15_1 = open('chr15.txt', 'r')
    chr15_2 = chr15_1.readline()
    chr15_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr15_2} -O all_chr15.gvcf \n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr15.gvcf -O chr15.vcf\n')
        file.write('rm ./all_chr15.gvcf\n')

else:
    os.mkdir('7_gvcf-vcf')
    with open('7_gvcf-vcf.sh', 'a') as gvcf_vcf:
        gvcf_vcf.write('#!/bin/bash\n')
    for i in bam_filename:
        if 'chr1' in i and 'idx' not in i:
            with open('chr1.txt', 'a') as chr1:
                chr1.write('-V i\0')
        elif 'chr2' in i and 'idx' not in i:
            with open('chr2.txt', 'a') as chr2:
                chr2.write('-V i\0')
        elif 'chr3' in i and 'idx' not in i:
            with open('chr3.txt', 'a') as chr3:
                chr3.write('-V i\0')
        elif 'chr4' in i and 'idx' not in i:
            with open('chr4.txt', 'a') as chr4:
                chr4.write('-V i\0')
        elif 'chr5' in i and 'idx' not in i:
            with open('chr5.txt', 'a') as chr5:
                chr5.write('-V i\0')
        elif 'chr6' in i and 'idx' not in i:
            with open('chr6.txt', 'a') as chr6:
                chr6.write('-V i\0')
        elif 'chr7' in i and 'idx' not in i:
            with open('chr7.txt', 'a') as chr7:
                chr7.write('-V i\0')
        elif 'chr8' in i and 'idx' not in i:
            with open('chr8.txt', 'a') as chr8:
                chr8.write('-V i\0')
        elif 'chr9' in i and 'idx' not in i:
            with open('chr9.txt', 'a') as chr9:
                chr9.write('-V i\0')
        elif 'chr10' in i and 'idx' not in i:
            with open('chr10.txt', 'a') as chr10:
                chr10.write('-V i\0')
        elif 'chr11' in i and 'idx' not in i:
            with open('chr11.txt', 'a') as chr11:
                chr11.write('-V i\0')
        elif 'chr12' in i and 'idx' not in i:
            with open('chr12.txt', 'a') as chr12:
                chr2.write('-V i\0')
        elif 'chr13' in i and 'idx' not in i:
            with open('chr13.txt', 'a') as chr13:
                chr13.write('-V i\0')
        elif 'chr14' in i and 'idx' not in i:
            with open('chr14.txt', 'a') as chr14:
                chr14.write('-V i\0')
        elif 'chr15' in i and 'idx' not in i:
            with open('chr15.txt', 'a') as chr15:
                chr15.write('-V i\0')

    chr1_1 = open('chr1.txt', 'r')
    chr1_2 = chr1_1.readline()
    chr1_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr1_2} -O all_chr1.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr1.gvcf -O chr1.vcf\n')
        file.write('rm ./all_chr1.gvcf\n')

    chr2_1 = open('chr2.txt', 'r')
    chr2_2 = chr2_1.readline()
    chr2_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr2_2} -O all_chr2.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr2.gvcf -O chr2.vcf\n')
        file.write('rm ./all_chr2.gvcf\n')

    chr3_1 = open('chr3.txt', 'r')
    chr3_2 = chr3_1.readline()
    chr3_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr3_2} -O all_chr3.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr3.gvcf -O chr3.vcf\n')
        file.write('rm ./all_chr3.gvcf\n')

    chr4_1 = open('chr4.txt', 'r')
    chr4_2 = chr4_1.readline()
    chr4_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr4_2} -O all_chr4.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr4.gvcf -O chr4.vcf\n')
        file.write('rm ./all_chr4.gvcf\n')

    chr5_1 = open('chr5.txt', 'r')
    chr5_2 = chr5_1.readline()
    chr5_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr5_2} -O all_chr5.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr5.gvcf -O chr5.vcf\n')
        file.write('rm ./all_chr5.gvcf\n')

    chr6_1 = open('chr6.txt', 'r')
    chr6_2 = chr6_1.readline()
    chr6_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr6_2} -O all_chr6.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr6.gvcf -O chr6.vcf\n')
        file.write('rm ./all_chr6.gvcf\n')

    chr7_1 = open('chr7.txt', 'r')
    chr7_2 = chr7_1.readline()
    chr7_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr7_2} -O all_chr7.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr7.gvcf -O chr7.vcf\n')
        file.write('rm ./all_chr7.gvcf\n')

    chr8_1 = open('chr8.txt', 'r')
    chr8_2 = chr8_1.readline()
    chr8_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr8_2} -O all_chr8.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr8.gvcf -O chr8.vcf\n')
        file.write('rm ./all_chr8.gvcf\n')

    chr9_1 = open('chr9.txt', 'r')
    chr9_2 = chr9_1.readline()
    chr9_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr9_2} -O all_chr9.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr9.gvcf -O chr9.vcf\n')
        file.write('rm ./all_chr9.gvcf\n')

    chr10_1 = open('chr10.txt', 'r')
    chr10_2 = chr10_1.readline()
    chr10_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr10_2} -O all_chr10.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr10.gvcf -O chr10.vcf\n')
        file.write('rm ./all_chr10.gvcf\n')

    chr11_1 = open('chr11.txt', 'r')
    chr11_2 = chr11_1.readline()
    chr11_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr11_2} -O all_chr11.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr11.gvcf -O chr11.vcf\n')
        file.write('rm ./all_chr11.gvcf\n')

    chr12_1 = open('chr12.txt', 'r')
    chr12_2 = chr12_1.readline()
    chr12_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr12_2} -O all_chr12.gvcf \n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr12.gvcf -O chr12.vcf\n')
        file.write('rm ./all_chr13.gvcf\n')

    chr13_1 = open('chr13.txt', 'r')
    chr13_2 = chr13_1.readline()
    chr13_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr13_2} -O all_chr13.gvcf\n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr13.gvcf -O chr13.vcf\n')
        file.write('rm ./all_chr14.gvcf\n')

    chr14_1 = open('chr14.txt', 'r')
    chr14_2 = chr14_1.readline()
    chr14_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr14_2} -O all_chr14.gvcf \n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr14.gvcf -O chr14.vcf\n')
        file.write('rm ./all_chr15.gvcf\n')

    chr15_1 = open('chr15.txt', 'r')
    chr15_2 = chr15_1.readline()
    chr15_1.close()
    with open('7_gvcf-vcf.sh', 'a') as file:
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {chr15_2} -O all_chr15.gvcf \n')
        file.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr15.gvcf -O chr15.vcf\n')
        file.write('rm ./all_chr15.gvcf\n')

os.system('mv ./7_gvcf-vcf.sh ./7_gvcf-vcf')
os.system('mv ./chr*.txt ./7_gvcf-vcf')
print('\033[1;36m在当前目录下，有一个叫7_gvcf-vcf的文件夹，里面有一个shell脚本，执行它即可\033[m')
