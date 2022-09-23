# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('15_phytree'):
    print('已经存在15_phytree目录，无需创建了')
else:
    os.mkdir('15_phytree')

VCF2Dis = input('请输入VCF2Dis软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/VCF2Dis-1.47/bin/VCF2Dis：')
allchr_file_path = input('请输入用于构建进化树的vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/14_LD_view_filter/chr_noctg_admixture.vcf：')

with open('15_phytree.sh', 'a') as tree:
    tree.write('#!/bin/bash\n')
    tree.write(f'{VCF2Dis} -InPut {allchr_file_path} -OutPut pyhtree.mat\n')
    tree.write('echo \'你可以看到工作目录下有一个叫做phttree.mat的文件，把它提交给在线网站http://www.atgc-montpellier.fr/fastme/，Data Type选择Distance matrix；Algorithm选择NJ。留下邮箱后提交。结果是nwk格式的树文件，提交给iTOL美化即可\'')

os.system('mv ./15_phytree.sh ./15_phytree')
print('\033[1;36m在当前目录下，有一个叫15_phytree的文件夹，里面有一个shell脚本，执行它即可,运行速度很快，不必放到后台\033[m')
