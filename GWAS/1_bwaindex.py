#coding=utf-8
# 编写人：赵子�?
# 编写时间�?022/7/1 10:41
# 邮箱:2939818719@qq.com
import os
cankaopath = input('请输入参考基因组文件的绝对路径：')
cankaoname = input('请输入参考基因组的文件名，例如：xso-gene.fa:')
index_name = input('为您的参考基因组索引起一个前缀名，注意是前缀名。例如：xsoindex：')
if os.path.exists('1_bwaindex'):
    with open('1_bwaindex.sh', 'a') as bwa_index:
        bwa_index.write('#!/bin/bash\n')
        bwa_index.write(f'bwa index -a bwtsw -p {index_name} {cankaopath}\n')
        bwa_index.write(f'samtools faidx {cankaopath}\n')
        bwa_index.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CreateSequenceDictionary -REFERENCE {cankaopath} -OUTPUT {cankaoname}.dict')
else:
    os.mkdir('1_bwaindex')
    with open('1_bwaindex.sh', 'a') as bwa_index:
        bwa_index.write('#!/bin/bash\n')
        bwa_index.write(f'bwa index -a bwtsw -p {index_name} {cankaopath}\n')
        bwa_index.write(f'samtools faidx {cankaopath}\n')
        bwa_index.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar CreateSequenceDictionary -REFERENCE {cankaopath} -OUTPUT {cankaoname}.dict')

os.system('mv ./1_bwaindex.sh ./1_bwaindex')
print('\033[m在当前目录下有一个叫1_bwaindex的文件夹，里面有一个shell脚本，执行它即可\033[m')



'''
报错和心得
没啥好说的，这个简单。强调一下bwtsw参数，这个在序列大于10MB时需要，一般我们的基因组都大于10MB，因此无脑选就对了
'''