# 编写人：赵子权
# 编写时间：2022/9/26 11:54
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('16_kingship'):
    print('已经存在16_kingship目录，无需创建了')
else:
    os.mkdir('16_kingship')

King_software = input('请输入King软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/king/king：')
allchr_file_path = input('请输入经过缺失过滤，maf后vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/13_Missing_rate_filtering/allchr_plink_filtering.vcf：')

with open('16_kingship.sh', 'a') as king:
    king.write('#!/bin/bash\n')
    king.write(f'{King_software} -b {allchr_file_path} --kinship --ibdseg --ibs --cpus 50 --prefix allchr_king\n')

os.system('mv ./16_kingship.sh ./16_kingship')
print('\033[1;36m在当前目录下，有一个叫16_kingship的文件夹，里面有一个shell脚本，执行它即可,运行速度很快，不必放到后台\033[m')

'''
Additional Options
         Close Relative Inference : --related, --duplicate
   Pairwise Relatedness Inference : --kinship, --ibdseg, --ibs, --homog   #--ibdseg和--homog不能同时出现
              Inference Parameter : --degree, --seglength
         Relationship Application : --unrelated, --cluster, --build
                        QC Report : --bysample, --bySNP, --roh, --autoQC
                     QC Parameter : --callrateN, --callrateM
             Population Structure : --pca, --mds
              Structure Parameter : --projection, --pcs
              Disease Association : --tdt
   Quantitative Trait Association : --mtscore
                Association Model : --trait [], --covariate []
            Association Parameter : --invnorm, --maxP
               Genetic Risk Score : --risk, --model [], --prevalence, --noflip
              Computing Parameter : --cpus
                   Optional Input : --fam [], --bim [], --sexchr [23]
                           Output : --rplot, --pngplot, --plink
                 Output Parameter : --prefix [king], --rpath []
'''