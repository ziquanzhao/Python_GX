#coding=utf-8
# 编写人：赵子�?
# 编写时间�?022/7/1 10:04
# 邮箱:2939818719@qq.com
import os

if os.path.exists('2_bwaaglin_sort_bam'):
    print('2_bwaaglin_sort_bam目录已存在，无需创建')
else:
    os.mkdir('2_bwaaglin_sort_bam')

chongcexupath = input('请输入重测序文件的绝对路径，只输入到文件夹即可，例如：/mnt/data/project/unknown/reseq/bypy/cleandata/：')
chongcexu_filename = os.listdir(chongcexupath)
cankao_index = input('请输入参考基因组bwa索引的绝对路径，需要输入到文件级别，但是不要后缀，例如：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xsoindex：')
bwa_software_path = input('请输入bwa软件的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/Bwa/：')
picard_sorfware_path = input('请输入picard软件里picard.jar这个java包的绝对路径，例如：/mnt/storage/zhaoziquan/GWAS/software/picard/picard.jar：')

with open('2_bwaaglin_sort_bam.sh', 'a') as bwaaglin_sort_bam:
    bwaaglin_sort_bam.write('#!/bin/bash\n')
    for i in chongcexu_filename:
        if "R1" in i:
            num = i.replace('_R1.fq.gz', '')
            bwaaglin_sort_bam.write(fr'{bwa_software_path}bwa mem -t 100 -M -R "@RG\tID:{num}\tLB:{num}\tPL:illumina\tPU:{num}\tSM:{num}\" {cankao_index} {chongcexupath}{num}_R1.fq.gz {chongcexupath}{num}_R2.fq.gz > {num}.sam' + '\n')   #非双端测序修改此代码
            bwaaglin_sort_bam.write(fr'{bwa_software_path}bwa mem -t 100 -M -R "@RG\tID:{num}\tLB:{num}\tPL:illumina\tPU:{num}\tSM:{num}\" {cankao_index} {chongcexupath}{num}_R1.fq.gz {chongcexupath}{num}_R2.fq.gz > {num}.sam' + '\n')
            bwaaglin_sort_bam.write(f'sed -i "2326d;2328d" {num}.sam\n')
            bwaaglin_sort_bam.write(f'java -jar {picard_sorfware_path} SortSam -TMP_DIR ./ -VALIDATION_STRINGENCY SILENT -INPUT ./{num}.sam -OUTPUT ./{num}_sort.bam -SORT_ORDER coordinate\n')
            bwaaglin_sort_bam.write(f'rm {num}.sam\n')


os.system('mv ./2_bwaaglin_sort_bam.sh ./2_bwaaglin_sort_bam')
print('\033[1;36m在当前目录下，有一个叫2_bwaaglin_sort_bam的文件夹，里面有一个shell脚本，执行它即可\033[m')

'''
报错和心得：
1.注意bwa men -R "@RG\tID:{num}\tLB:{num}\tPL:illumina\tPU:{num}\tSM:{num}\"
这个设置说实在话我并未明白每一个具体怎么设置。PL应设置为你的测序平台，这个好说。SM设置为你的样本号，就是我们的哪株树对应的编号。但是ID,LB,PU究竟该怎么设置我并不明白。我上网查道德资料说的时ID包括你测序时上机的read goups编号
，但实际上我们并没有这个号。我最开始以为这个如果设置的不对，后面就没法继续。但后来我运行sam转bam时，发现我们的read goups其实已经记录在我们最初的重测序文件里了（WF201_R1_fq.gz文件里），因此我就随便写这个ID，目前没有发现问题。

2.-t 100.设置多少个线程。

3.
AAAA：bwa mem -t 100 -M -R "@RG\tID:{num}\tLB:{num}\tPL:illumina\tPU:{num}\tSM:{num}\" {cankao_index} {chongcexupath}{num}_R1.fq.gz {chongcexupath}{num}_R2.fq.gz > {num}.sam
我上面之所以让 AAAA 这条命令运行两边。我认为这是一个BUG，而且是我不明白哪里出错的BUG。我发现我把 AAAA 打在命令行并enter后，他不会运行，然后我按了键盘向上箭头，再次调出这个命令，再次运行后，我就发现它可以运行了。
我实在不知道问题出在哪了，因此我只能让 AAAA 命令运行2次来解决这个问题。

4.
关于"sed -i "2326d;2328d" {num}.sam"命令的解释
这个命令就是删除sam文件的2326和2328行内容，为啥要删除呐，我猜测和我让bwa mem命令运行2此有一半关系。因为经过 AAAA 命令运行过后，得到的sam文件里，在注释部分和比对部分之间，被插入了2次脚本命令，导致picard不能正常识别sam文件了。
其实按理说正常运行的sam文件里也会有1次脚本命令，但这个脚本命令会处于注释行，但是不知道怎么地，我运行完脚本命令另起一行了，这就是问题所在。我并不清楚哪个犄角旮旯的出错了，因此直接把错误的部分删掉一了百了。




'''

