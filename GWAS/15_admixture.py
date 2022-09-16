# 编写人：赵子权
# 编写时间：2022/9/13 21:19
# 邮箱:2939818719@qq.com

import os
import re

if os.path.isdir('15_admixture'):
    print('已经存在15_admixture目录，无需创建了')
else:
    os.mkdir('15_admixture')

admixtrue_software_path = input('请输入admixtrue软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/admixture/admixtrue：')
plink_LD_filtering_path = input('请输入已经完成LD筛选后文件所在目录，例如：/mnt/storage/zhaoziquan/GWAS/14_LD_view_filter/：')
plink_LD_filtering_bfilename = os.listdir(plink_LD_filtering_path)

'''
for ped_filename in plink_LD_filtering_bfilename:
    if '_admixture.ped' in ped_filename and 'ctg' not in ped_filename and 'chr1_admixture' not in ped_filename:
        ped_filename = re.sub('.ped', '', ped_filename)
        with open('list.txt', 'a') as pedlist:
            pedlist.write(f'{ped_filename}.ped {ped_filename}.map\n')
'''

with open('15_admixture.sh', 'a') as admixture:
    admixture.write('#!/bin/bash\n')
    #admixture.write(f'/mnt/storage/zhaoziquan/GWAS/software/plink/plink -file {plink_LD_filtering_path}chr1_admixture --merge-list list.txt --recode 12 --out chr_noctg_admixture --allow-extra-chr\n')
    #admixture.write('sed -i \'s/Lachesis_group//g\' chr_noctg_admixture.bim\n')
    for K in range(1, 21, 1):
        cycles = 1
        while True:
            if cycles <= 30:
                admixture.write(f'admixtrue -B50 --cv chr_noctg_admixture.bed {K} -j50 >> admixture_{K}.txt\n')
                cycles = cycles + 1
                continue
            else:
                break
        admixture.write(f'grep \'CV error\' admixture_{K}.txt > cv_error_{K}.txt\n')

os.system('mv ./15_admixture.sh ./15_admixture/')
#os.system('mv ./list.txt ./15_admixture/')
print('\033[1;36m在当前目录下，有一个叫15_admixture的文件夹，里面有一个shell脚本，执行它即可\033[m')

#-j50,50个线程
#-B，计算标准误差
