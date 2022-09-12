# 编写人：赵子权
# 编写时间：2022/9/13 9:21
# 邮箱:2939818719@qq.com

import os
import re

if os.path.isdir('12_imputation_beagle'):
    print('已经存在12_imputation_beagle目录，无需创建了')
else:
    os.mkdir('12_imputation_beagle')

beagle_software_path = input('请输入beagle5.4软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/beagle5_4/beagle.22Jul22.46e.jar：')
ccx_final_file_path = input('请输入重测序数据最后完成snp和indel合并后的vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/11_hebing_snp_indel/：')
vcf_filename = os.listdir(ccx_final_file_path)

with open('12_imputation_beagle.sh', 'a') as impute:
    impute.write('#!/bin/bash\n')
    for filename in vcf_filename:
        if '.idx' not in filename:
            filename = re.sub('_final_164.vcf', '', filename)
            impute.write(f'java -Xmx200g -jar {beagle_software_path} gt={ccx_final_file_path}{filename}_final_164.vcf out={filename}_imputation iterations=50 nthreads=60\n')

os.system('mv ./12_imputation_beagle.sh ./12_imputation_beagle/')
print('\033[1;36m在当前目录下，有一个叫12_imputation_beagle的文件夹，里面有一个shell脚本，执行它即可\033[m')