#coding=utf-8
# 编写人：赵子权
# 编写时间：2022/7/1 16:52
# 邮箱:2939818719@qq.com
import os

if os.path.exists('3_mark_duplicates'):
    print('3_mark_duplicates目录已存在，无需创建')
else:
    os.mkdir('3_mark_duplicates')

bam_path = input('请输入所有bam文件所在路径，例如：/mnt/storage/zhaoziquan/GWAS/2_bwaaglin_sort_bam/：')
picard_sorfware_path = input('请输入picard软件里picard.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/picard/picard.jar：')
sample_num = int(input('请告知我您有多少个样本，因为我后续会根据样本量拆解shell脚本，让您多个样本同时计算，以减少时间消耗，例如：200'))
bam_filename = os.listdir(bam_path)

with open('3_mark_duplicates.sh', 'a') as mark_duplicates:
    mark_duplicates.write('#!/bin/bash\n')
    for i in bam_filename:
        name = i.replace('.bam', '')
        mark_duplicates.write(f'java -jar {picard_sorfware_path} MarkDuplicates -MAX_FILE_HANDLES_FOR_READ_ENDS_MAP 800 -REMOVE_DUPLICATES false -INPUT {bam_path}{name}.bam -OUTPUT {name}_dedup.bam -METRICS_FILE {name}_dedup.metrics -VALIDATION_STRINGENCY LENIENT\n')

os.system('mv ./3_mark_duplicates.sh ./3_mark_duplicates')
print('\033[1;36m在当前目录下，有一个叫3_mark_duplicates的文件夹，里面有一个shell脚本，执行它即可\033[m')


"""
报错和心得
1.为什么要标记重复：
在制备文库的过程中，由于PCR扩增过程中会存在一些偏差，也就是说有的序列会被过量扩增。这样，在比对的时候，这些过量扩增出来的完全相同的序列就会比对到基因组的相同位置。
而这些过量扩增的reads并不是基因组自身固有序列，不能作为变异检测的证据，因此，要尽量去除这些由PCR扩增所形成的duplicates，这一步可以使用picard-tools来完成。
去重复的过程是给这些序列设置一个flag以标志它们，方便GATK的识别。

2.
REMOVE_DUPLICATES=true 。官网是flase
来丢弃duplicated序列。对于是否选择标记或者删除，对结果应该没有什么影响，GATK官方流程里面给出的例子是仅做标记不删除。
这里定义的重复序列是这样的：如果两条reads具有相同的长度而且比对到了基因组的同一位置，那么就认为这样的reads是由PCR扩增而来，就会被GATK标记。

3.
VALIDATION_STRINGENCY=LENIENT
在BWA 比对生成SAM文件时，将没有map到基因组上的read归到了ref以外的区域，其MAPQ值不为0，而Picard认为这些read是不应该出现的，所以会报错。如果想忽略报错的话，就使用这行代码。

4.
MAX_FILE_HANDLES_FOR_READ_ENDS_MAP=800
将读取结束溢出到磁盘时保持打开状态的最大文件句柄数。将此数字设置为略低于每个进程可能打开的文件的最大数目。这个数字可以通过在Unix系统上执行“ulimit -n”命令找到。
咱们的服务器查的是1024.



"""






