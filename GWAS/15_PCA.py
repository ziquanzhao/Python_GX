# 编写人：赵子权
# 编写时间：2022/9/20 21:23
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('15_PCA'):
    print('已经存在15_PCA目录，无需创建了')
else:
    os.mkdir('15_PCA')

ldak5_2_software_path = input('请输入ldak5.2软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/ldak5_2/ldak5.2.linux：')
plink_ld_filtering_path = input('请输入已经完成LD筛选合并后的plink的二进制文件所在绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/14_LD_view_filter/chr_noctg_admixture：')
sample_account = int(input('请输入你的样本的个数，例如：164：'))
section_account = int(input('请输入你的样本被切割成多少个section，如果第一次执行本脚本，可以忽略这个输入，直接回车即可。：'))

with open('15_PCA.sh', 'a') as PCA:
    PCA.write('#!/bin/bash\n')
    PCA.write(f'{ldak5_2_software_path} --cut-weights snp.sections --bfile {plink_ld_filtering_path}\n')
    PCA.write('echo \'执行完上一步，当前目录下会有一个叫做snp_sections的文件夹，打开里面的section.number文件，会告诉你有多少个section。\'\n')
    section_account = section_account + 1
    for section in range(1, section_account, 1):     #看有几个section就设置几个,计算权重
        PCA.write(f'{ldak5_2_software_path} --calc-weights snp.sections --bfile {plink_ld_filtering_path} --section {section}\n')
    PCA.write(f'{ldak5_2_software_path} --join-weights snp.sections --bfile {plink_ld_filtering_path}\n')   #合并权重，给snp赋权
    PCA.write(f'{ldak5_2_software_path} --calc-kins-direct snp.ldak.weight --bfile {plink_ld_filtering_path} --weights ./snp.sections/weights.all --kinship-gz YES --power -0.25\n') #输出grm阵列(snp.ldak.weight)
    PCA.write(f'{ldak5_2_software_path} --pca snp.ldak.weight --grm snp.ldak.weight --axes {sample_account}\n')  #考虑权重计算PCA。特征值结果储存在snp.ldak.weight.values中，特征向量储存在snp.ldak.weight.vect中

os.system('mv ./15_PCA.sh ./15_PCA/')
print('\033[1;36m在当前目录下，有一个叫15_PCA的文件夹，里面有一个shell脚本，执行它即可\033[m')
