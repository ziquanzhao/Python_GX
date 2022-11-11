# 编写人：赵子权
# 编写时间：2022/9/13 16:00
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('13_Missing_rate_filtering'):
    print('已经存在13_Missing_rate_filtering目录，无需创建了')
else:
    os.mkdir('13_Missing_rate_filtering')

plink2_software_path = input('请输入plink2软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/plink/plink2：')
plink_bfile_path = input('请输入已经完成基因型填补的vcf文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/11_hebing_snp_indel/：')
plink_bfilename = os.listdir(plink_bfile_path)

with open('13_Missing_rate_filtering.sh', 'a') as filtering:
    filtering.write('#!/bin/bash\n')
    for filename in plink_bfilename:
        if '.idx' not in filename:
            filename = re.sub('_final_164.vcf', '', filename)
            filtering.write(f'{plink2_software_path} --vcf {plink_bfile_path}{filename}_final_164.vcf --export vcf --allow-extra-chr '
                            f'--geno 0.2 --maf 0.05 --hwe 1e-6 '
                            f'--vcf-max-dp 50 --vcf-min-dp 4 --vcf-min-gq 10 '
                            f'--min-alleles 2 --max-alleles 2 --var-min-qual 30 --out {filename}_plink_filtering --threads 50\n')

os.system('mv ./13_Missing_rate_filtering.sh ./13_Missing_rate_filtering/')
print('\033[1;36m在当前目录下，有一个叫13_Missing_rate_filtering的文件夹，里面有一个shell脚本，执行它即可\033[m')

#--geno 0.1 --mind 0.1 --maf 0.01 --hwe 1e-4,这根据13_Missing_rate_statistics.py绘图结果设置。GWAS项目采用的MAF阈值在0.01-0.05之间，取决于样本大小.
#我们的数据缺失率很严重，所以--geno，--mind要尽量宽松一些
#--const-fid,对vcf文件中的标记ID进行编号
#--allow-extra-chr,如果染色体是非数字，加上这个参数。
#--make-bed,输出二进制文件
#--bfile，输入二进制文件。--file，输入正常plink文件，就是.ped和.map文件。--vcf，输入vcf文件
#--recode，输出正常plink文件。
#--vcf-max-dp 50 --vcf-min-dp 4.位点最大深度50，最小深度4.一般来说，最下深度是平均深度的三分之一到四分之一。最大深度是平均深度的3到5倍。
#--min-alleles 2 --max-alleles 2。只要双等位基因的情况，多等位基因不要，单等位基因也不要。
#--var-min-qual 30。过滤掉QUAL小于30的。GATK时也可以做
#--vcf-min-gq 10。QG也是一个衡量质量的指标，看情况设置吧。
