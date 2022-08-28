#coding = utf-8
# 编写人：赵子权
# 编写时间：2022/7/5 17:00
# 邮箱:2939818719@qq.com
import os

if os.path.exists('6_HaplotypeCaller'):
    print('6_HaplotypeCaller目录已存在，无需创建')
else:
    os.mkdir('6_HaplotypeCaller')

bam_dedup_path = input('请输入所有bam文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/3_mark_duplicates/：')
ref_path = input('请输入参考基因组所在路径，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')

bam_filename = os.listdir(bam_dedup_path)

with open('6_HaplotypeCaller.sh', 'a') as HaplotypeCaller:
    HaplotypeCaller.write('#!/bin/bash\n')
    for i in bam_filename:
        if i.find('bai') == -1 and i.find('metrics') == -1:
            name = i.replace('.bam', '')
            for x in range(1, 16, 1):
                HaplotypeCaller.write(f'java -jar /mnt/storage/zhaoziquan/GWAS/software/gatk-4.2.6.1/gatk-package-4.2.6.1-local.jar HaplotypeCaller -R {ref_path} -I {bam_dedup_path}{name}.bam -ERC GVCF -L Lachesis_group{x} -O {name}_chr1.gvcf\n')

os.system('mv ./6_HaplotypeCaller.sh ./6_HaplotypeCaller')
print('\033[1;36m在当前目录下，有一个叫6_HaplotypeCaller的文件夹，里面有一个shell脚本，执行它即可\033[m')
