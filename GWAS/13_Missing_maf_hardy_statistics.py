# 编写人：赵子权
# 编写时间：2022/9/13 14:30
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('13_Missing_rate_filtering'):
    print('已经存在13_Missing_rate_filtering目录，无需创建了')
else:
    os.mkdir('13_Missing_rate_filtering')

plink2_software_path = input('请输入plink2软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/plink/plink2：')
imputation_file_path = input('请输入已经完成基因型填补的vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/11_hebing_snp_indel/：')
imputation_filename = os.listdir(imputation_file_path)

with open('13_Missing_rate_statistics.sh', 'a') as missing_statistics:
    missing_statistics.write('#!/bin/bash\n')
    for filename in imputation_filename:
        if '.idx' not in filename:
            filename = re.sub('_final_164.vcf', '', filename)
            missing_statistics.write(f'{plink2_software_path} --vcf {imputation_file_path}{filename}_final_164.vcf --allow-extra-chr --make-bed --max-alleles 2 --out {filename} --threads 50\n')   #vcf转plink二进制格式
            missing_statistics.write(f'{plink2_software_path} -bfile {filename} --missing --out {filename} --allow-extra-chr --threads 50\n')  #统计缺失率
            missing_statistics.write(f'{plink2_software_path} -bfile {filename} --freq --out {filename}_maf --allow-extra-chr --threads 50\n')  #统计maf
            missing_statistics.write(f'{plink2_software_path} -bfile {filename} --hardy --out {filename} --allow-extra-chr --threads 50\n')  #统计哈温
            missing_statistics.write(f'Rscript plink_miss_maf_hardy_{filename}.R\n')
            with open(f'plink_miss_maf_hardy_{filename}.R', 'a') as plink_miss:   #写R脚本绘图
                plink_miss.write(f'vmiss <- read.table(\'{filename}.vmiss\', header = T)\n')
                plink_miss.write(f'smiss <- read.table(\'{filename}.smiss\', header = T)\n')
                plink_miss.write(f'maf <- read.table(\'{filename}_maf.afreq\', header = T, as.is = T)\n')
                plink_miss.write(f'hardy <- read.table(\'{filename}.hardy\', header = T)\n')
                plink_miss.write(f'pdf(\'hist_{filename}_smiss.pdf\')\n')
                plink_miss.write(f'hist(smiss[,5], main = \'{filename}_individual_missingness\', xlab = \'missing\', font.lab = 2, font.axis = 1.5, lwd = 2, col = \'red\')\n')
                plink_miss.write(f'pdf(\'hist_{filename}_vmiss.pdf\')\n')
                plink_miss.write(f'hist(vmiss[,5], main = \'{filename}_SNP_missingness\', xlab = \'missing\', font.lab = 2, font.axis = 1.5, lwd = 2, col = \'red\')\n')
                plink_miss.write(f'pdf(\'hist_{filename}_maf.pdf\')\n')
                plink_miss.write(f'hist(maf[,5], main = \'{filename}_maf\', xlab = \'maf\', font.lab = 2, font.axis = 1.5, lwd = 2, col = \'red\')\n')
                plink_miss.write(f'pdf(\'hist_{filename}_hardy.pdf\')\n')
                plink_miss.write(f'hist(hardy[,10], main = \'{filename}_hardy\', xlab = \'hardy\', font.lab = 2, font.axis = 1.5, lwd = 2, col = \'red\')\n')
                plink_miss.write('dev.off()')

os.system('mv ./13_Missing_rate_statistics.sh ./13_Missing_rate_filtering/')
os.system('mv ./*.R ./13_Missing_rate_filtering')
print('\033[1;36m在当前目录下，有一个叫13_Missing_rate_filtering的文件夹，里面有一个shell脚本，执行它即可\033[m')

#--max-alleles 2
# 不加会报错chr10.bim cannot contain multiallelic variants