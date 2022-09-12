# 编写人：赵子权
# 编写时间：2022/9/13 21:19
# 邮箱:2939818719@qq.com

import os
import re

if os.path.isdir('15_admixture'):
    print('已经存在15_admixture目录，无需创建了')
else:
    os.mkdir('15_admixture')

plink2_software_path = input('请输入plink2软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/plink/plink2：')
admixtrue_software_path = input('请输入admixtrue软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/admixture/admixtrue：')
plink_LD_filtering_path = input('请输入已经完成缺失率，最小等位基因频率，哈温平衡后的plink的二进制文件所在目录，例如：/mnt/storage/zhaoziquan/GWAS/14_plink_LD/：')
plink_LD_filtering_bfilename = os.listdir(plink_LD_filtering_path)

with open('LD_prunein.txt', 'a') as LD_prunein:
    for filename in plink_LD_filtering_bfilename:
        if '_LD.prune.in.bed' in filename:
            filename = re.sub('_LD.prune.in.bed', '', filename)
            LD_prunein.write(f'{filename}_LD.prune.in.bed {filename}_LD.prune.in.bim {filename}_LD.prune.in.fam\n')
with open('15_admixture.sh', 'a') as admixture:
    admixture.write('#!/bin/bash\n')
    admixture.write(f'{plink2_software_path} --bfile {plink_LD_filtering_path}{filename}_LD.prune.in --noweb --bfile file --merge-list LD_prunein.txt --make-bed --out batch--recode 12 --out {filename}_LD_prune_in --threads 50\n')


os.system('mv ./15_admixture.sh ./15_admixture/')
print('\033[1;36m在当前目录下，有一个叫15_admixture的文件夹，里面有一个shell脚本，执行它即可\033[m')

