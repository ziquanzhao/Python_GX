#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/5 20:32
# 邮箱:2939818719@qq.com
import os
if os.path.isdir('7_gvcf-vcf'):
    print('已经存在7_gvcf-vcf目录，无需创建了')
else:
    os.mkdir('7_gvcf-vcf')

all_gvcf = input('请输入所有gvcf文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/6_HaplotypeCaller/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
filename = os.listdir(all_gvcf)
for i in filename:
    if '.idx' not in i:
        with open('gvcflist.txt', 'a') as gvcflist:
            gvcflist.write(i+'\n')

with open('gvcflist.txt', 'r') as gvcf_list:
    for i in gvcf_list.readlines():
        for y in range(1,16,1):
            gcvf = f'_sort_dedup_chr{y}.gvcf'
            if gcvf in i and 'idx' not in i:
                with open(f'chr{y}.txt', 'a') as chr:
                    chr.write(f'-V {all_gvcf}{i} ')

for x in range(1,16,1):
    with open(f'chr{x}.txt', 'r') as file:
        V = file.read().replace('\n', '')
        with open(f'7_gvcf-vcf_{x}.sh', 'a') as file2:
            file2.write('#!/bin/bash\n')
            file2.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CombineGVCFs -R {ref_path} {V} -O all_chr{x}.g.vcf\n')
            file2.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar GenotypeGVCFs -R {ref_path} -V all_chr{x}.g.vcf -O chr{x}.vcf\n')

os.system('rm ./gvcflist.txt')
os.system('mv ./7_gvcf-vcf_*.sh ./7_gvcf-vcf')
os.system('mv ./chr*.txt ./7_gvcf-vcf')
print('\033[1;36m在当前目录下，有一个叫7_gvcf-vcf的文件夹，里面有一个shell脚本，执行它即可\033[m')
