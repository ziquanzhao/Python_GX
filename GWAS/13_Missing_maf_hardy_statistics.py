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
imputation_file_path = input('请输入已经完成基因型填补的vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/12_imputation_beagle/：')
imputation_filename = os.listdir(imputation_file_path)

with open('13_Missing_rate_statistics.sh', 'a') as missing_statistics:
    missing_statistics.write('#!/bin/bash\n')
    for filename in imputation_filename:
        if '.log' not in filename:
            filename = re.sub('_imputation.vcf.gz', '', filename)
            missing_statistics.write(f'{plink2_software_path} --vcf {imputation_file_path}{filename}_imputation.vcf.gz --out {filename} --threads 50\n')   #vcf转plink二进制格式
            missing_statistics.write(f'{plink2_software_path} -bfile {filename} --missing --threads 50\n')  #统计缺失率
            missing_statistics.write(f'{plink2_software_path} -bfile {filename} --freq --out {filename}_maf --threads 50\n')  #统计maf
            missing_statistics.write(f'{plink2_software_path} -bfile {filename} --hardy --threads 50\n')  #统计哈温
            missing_statistics.write(f'mv ./plink.imiss ./plink{filename}.imiss\n')
            missing_statistics.write(f'mv ./plink.lmiss ./plink{filename}.lmiss\n')
            missing_statistics.write(f'mv ./plink.hwe ./plink{filename}.hwe\n')
            missing_statistics.write(f'Rscript plink_miss_maf_hardy_{filename}.R')
            with open(f'plink_miss_maf_hardy_{filename}.R', 'a') as plink_miss:   #写R脚本绘图
                plink_miss.write(f'imiss <- read.table(\'plink{filename}.imiss\', header = T)\n')
                plink_miss.write(f'lmiss <- read.table(\'plink{filename}.lmiss\', header = T)\n')
                plink_miss.write(f'maf <- read.table(\'{filename}_maf\', header = T, as.is = T)\n')
                plink_miss.write(f'hardy <- read.table(\'plink{filename}_hwe\', header = T)\n')
                plink_miss.write(f'pdf(\'hist_{filename}_imiss.pdf\'\n')
                plink_miss.write(f'hist(imiss[,6], main = \'{filename}_individual_missingness\', xlab = \'missing\', font.lab = 2, font.axis = 1.5, lwd = 2, col = \'red\')')
                plink_miss.write(f'pdf(\'hist_{filename}_lmiss.pdf\'\n')
                plink_miss.write(f'hist(lmiss[,5], main = \'{filename}_SNP_missingness\', xlab = \'missing\', font.lab = 2, font.axis = 1.5, lwd = 2, col = \'red\')')
                plink_miss.write(f'pdf(\'hist_{filename}_maf.pdf\'\n')
                plink_miss.write(f'hist(maf[,5], main = \'{filename}_maf\', xlab = \'maf\', font.lab = 2, font.axis = 1.5, lwd = 2, col = \'red\')')
                plink_miss.write(f'pdf(\'hist_{filename}_hardy.pdf\'\n')
                plink_miss.write(f'hist(hardy[,9], main = \'{filename}_hardy\', xlab = \'hardy\', font.lab = 2, font.axis = 1.5, lwd = 2, col = \'red\')')
                plink_miss.write('dev.off()')

os.system('mv ./13_Missing_rate_statistics.sh ./13_Missing_rate_filtering/')
print('\033[1;36m在当前目录下，有一个叫13_Missing_rate_filtering的文件夹，里面有一个shell脚本，执行它即可\033[m')