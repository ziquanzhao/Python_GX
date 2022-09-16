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
plink_LD_filtering_path = input('请输入已经完成缺失率，最小等位基因频率，哈温平衡后的plink的二进制文件所在目录，例如：/mnt/storage/zhaoziquan/GWAS/14_LD_view_filter/：')
plink_LD_filtering_bfilename = os.listdir(plink_LD_filtering_path)

with open('15_admixture.sh', 'a') as admixture:
    admixture.write('#!/bin/bash\n')
    for K in range(1, 30, 1):
        for ped_filename in plink_LD_filtering_bfilename:
            if '_admixture.ped' in ped_filename:
                ped_filename = re.sub('_admixture.ped', '', ped_filename)
                admixture.write(f'{admixtrue_software_path} --cv {plink_LD_filtering_path}{ped_filename}_admixture.ped {K} -j 50 >> admixture_{ped_filename}.txt\n')

os.system('mv ./15_admixture.sh ./15_admixture/')
print('\033[1;36m在当前目录下，有一个叫15_admixture的文件夹，里面有一个shell脚本，执行它即可\033[m')

#-j,线程
