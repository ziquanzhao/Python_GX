# 编写人：赵子权
# 编写时间：2022/11/16 21:13
# 邮箱:2939818719@qq.com
import os
print('gemma_path = /mnt/storage/zhaoziquan/GWAS/software/gemma/gemma-0.98.5-linux-static-AMD64')
print('genetype = /mnt/storage/zhaoziquan/GWAS/olddata/17_gwas/TLsample231_gene01')
gemma_path = '/mnt/storage/zhaoziquan/GWAS/software/gemma/gemma-0.98.5-linux-static-AMD64'
genetype = '/mnt/storage/zhaoziquan/GWAS/olddata/17_gwas/TLsample231_gene01'
pheotype = input('请输入表型数据文件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/olddata/GEMMA/FM.txt:')
output_filename = 'TLsample231_gene01'

pheotype_filename = os.path.splitext(os.path.basename(pheotype))[0]

with open(f'gemma_{pheotype_filename}.sh', 'a') as gemma:
    gemma.write('#!/bin/bash\n')
    gemma.write(f'{gemma_path} -bfile {genetype} -gk 2 -p {pheotype} -o {output_filename}_{pheotype_filename}_kingship\n')
    gemma.write(f'{gemma_path} -bfile {genetype} -lm 1 -p {pheotype} -o {output_filename}_{pheotype_filename}_lm\n')
    gemma.write(f'sort -k 11 -g ./output/{output_filename}_{pheotype_filename}_lm.assoc.txt -o ./output/{output_filename}_{pheotype_filename}_lm.assoc.txt\n')
    gemma.write(f'{gemma_path} -bfile {genetype} -lmm 1 -k ./output/{output_filename}_{pheotype_filename}_kingship.sXX.txt -p {pheotype} -o {output_filename}_{pheotype_filename}_lmm\n')
    gemma.write(f'sort -k 12 -g ./output/{output_filename}_{pheotype_filename}_lmm.assoc.txt -o ./output/{output_filename}_{pheotype_filename}_lmm.assoc.txt\n')
    gemma.write(f'mv ./output ./{output_filename}_{pheotype_filename}')

print(f'\033[m在当前目录下有一个叫gemma_{pheotype_filename}.sh的shell脚本，执行它即可\033[m')