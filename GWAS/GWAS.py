# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

import os
import re
import time

def main():
    while True:
        print('\033[0;36m所需软件如下：\033[m')
        print('BWA、Samtools、Picard')
        answer = input('输入Y/y开始使用，输入N/n结束使用:\n')
        if answer == 'Y' or answer == 'y':
            menu()
            step = int(input('\033[0;36m选择所要进行的步骤\n\033[m'))
            if step == 1:
                cankaopath = input('请输入参考基因组文件的绝对路径，默认为：/mnt/storage/zhaoziquan/KCS/基因组文件/：')
                cankaoname = input('请输入参考基因组的文件名，默认为：xso-gene.fa:')
                index_name = input('为您的参考基因组索引起一个前缀名，注意是前缀名。默认为：xsoindex：')
                bwa_software_path = input('请输入bwa软件的绝对路径，默认为：/mnt/storage/zhaoziquan/GWAS/software/Bwa/bwa：')
                samtools_software_path = input('请输入samtools软件的绝对路径，默认为：/mnt/storage/zhaoziquan/GWAS/software/samtools-1.15.1/bin/samtools：')
                GATK_sorfware_path = input('请输入GATK软件中gatk-package-4.2.6.1-local.jar这个java包的绝对路径，默认为：/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar：')
                GWAS1_genome_index(cankaopath='/mnt/storage/zhaoziquan/KCS/基因组文件/', cankaoname='xso-gene.fa', index_name='xsoindex',
                                   bwa_software_path='/mnt/storage/zhaoziquan/GWAS/software/Bwa/bwa',
                                   samtools_software_path='/mnt/storage/zhaoziquan/GWAS/software/samtools-1.15.1/bin/samtools',
                                   GATK_sorfware_path='/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar')
            elif step == 2:
                pass

        else:
            print('\033[0;36m===========================\033[m')
            print('         欢迎下次使用!        ')
            print('\033[0;36m===========================\033[m')
            break




def menu():
    print('\033[0;36m==========GWAS检测SNP步骤如下============\033[m')
    print('1、建立参考基因组索引')



def GWAS1_genome_index(cankaopath='/mnt/storage/zhaoziquan/KCS/基因组文件/',cankaoname='xso-gene.fa',index_name='xsoindex',
                       bwa_software_path='/mnt/storage/zhaoziquan/GWAS/software/Bwa/bwa',
                       samtools_software_path='/mnt/storage/zhaoziquan/GWAS/software/samtools-1.15.1/bin/samtools',
                       GATK_sorfware_path='/mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar'):
    if os.path.exists('GWAS1_genome_index'):
        print('GWAS1_genome_index目录已存在，无需创建')
    else:
        os.mkdir('GWAS1_genome_index')
    with open('GWAS1_genome_index.sh', 'a') as bwa_index:
        bwa_index.write('#!/bin/bash\n')
        bwa_index.write(f'{bwa_software_path} index -a bwtsw -p {index_name} {cankaopath}{cankaoname}\n')
        bwa_index.write(f'{samtools_software_path} faidx {cankaopath}{cankaoname}\n')
        bwa_index.write(f'java -jar {GATK_sorfware_path} CreateSequenceDictionary -REFERENCE {cankaopath}{cankaoname} -OUTPUT {cankaoname}.dict')
    os.system('mv ./GWAS1_genome_index.sh ./GWAS1_genome_index')

def GWAS2_bam_to_sam_sort():
    pass






if __name__ == '__main__':
    main()
