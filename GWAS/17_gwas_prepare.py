# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import os
import re

if os.path.isdir('17_gwas'):
    print('已经存在17_gwas目录，无需创建了')
else:
    os.mkdir('17_gwas')

filter_vcf_filepath = input('请输入经过maf,hardy等过滤后的vcf文件的绝对路径：例如：/mnt/storage/zhaoziquan/GWAS/13_Missing_rate_filtering/allchr_gene01_filtering.vcf：')
tassel5_software_path = input('请输入tassel软件中run_pipeline.pl脚本所在绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/tassel5.2.82/run_pipeline.pl：')
hapmap_filename = input('请给转换的hapmap去一个名字（只用给前缀即可），例如：allchr：')


with open('17_gwas_prepare.sh', 'a') as prepare:
    prepare.write('#!/bin/bash\n')
    prepare.write(f'{tassel5_software_path} -Xms100g -Xmx200g -vcf {filter_vcf_filepath} -sortPositions -export {hapmap_filename} -exportType HapmapDiploid')


os.system('mv ./17_gwas_prepare.sh ./17_gwas')
print('\033[1;36m在当前目录下，有一个叫17_gwas的文件夹，里面有一个shell脚本，执行它即可\033[m')