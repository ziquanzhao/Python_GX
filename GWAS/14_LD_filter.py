# 编写人：赵子权
# 编写时间：2022/9/13 19:20
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('14_LD_view_filter'):
    print('已经存在14_LD_view_filter目录，无需创建了')
else:
    os.mkdir('14_LD_view_filter')

plink2_software_path = input('请输入plink2软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/plink/plink2：')
plink_software_path = input('请输入plink1.9软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/plink/plink：')
plink_mmh_filtering_path = input('请输入已经完成缺失率，最小等位基因频率，哈温平衡后的plink的二进制文件所在目录，例如：/mnt/storage/zhaoziquan/GWAS/13_Missing_rate_filtering/：')
plink_mmh_filtering_bfilename = os.listdir(plink_mmh_filtering_path)

with open('14_LD_filter.sh', 'a') as LD:
    LD.write('#!/bin/bash\n')
    for filename in plink_mmh_filtering_bfilename:
        if '.vcf' in filename:
            filename = re.sub('_plink_filtering.vcf', '', filename)
            LD.write(f'{plink2_software_path} --vcf {plink_mmh_filtering_path}{filename}_plink_filtering.vcf --export vcf --set-all-var-ids \'@_#\' --allow-extra-chr --allow-no-sex --indep-pairwise 100 100 0.2 --out {filename}_LD_filter --threads 50\n')
            LD.write(f'{plink_software_path} --vcf {filename}_LD_filter.vcf --extract {filename}_LD_filter.prune.in --out {filename}_admixture --recode 12 --allow-extra-chr --threads 50\n')

os.system('mv ./14_LD_filter.sh ./14_LD_view_filter/')
print('\033[1;36m在当前目录下，有一个叫14_LD_view_filter的文件夹，里面有一个shell脚本，执行它即可\033[m')

#--geno 0.1 --mind 0.02 --maf 0.05 --hwe 1e-4,这根据13_Missing_rate_statistics.py绘图结果设置
#--const-fid,对vcf文件中的标记ID进行编号
#--allow-extra-chr,如果染色体是非数字，加上这个参数。
#--allow-no-sex，允许没有性别信息。
#--make-bed,输出二进制文件
#--bfile，输入二进制文件。--file，输入正常plink文件，就是.ped和.map文件。--vcf，输入vcf文件
#--recode，输出正常plink文件。
#--ld-window 表示计算LD的区间，表示距离小于这个值的标记对都要进行LD的计算。
#--ld-window-kb 默认为1Mb，表示只对距离在1Mb之内的SNP位点进行分析。
#--ld-window-r2 0.2 这个参数只能和 --r2参数搭配使用，默认值为0.2对输出结果进行过滤，只输出r2大于该参数的r2值
#--indep-pairwise 300000 1000 0.2 300kb,1000个SNP，r方=0.2