# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com



'''
利用hisats2将转录组数据比对到参考基因组上，并转换为bam文件后排序

第一步：建索引
hisat2-build -p <threads> <refseq.fa> <refseq_index_name>
#建立索引文件

第二步：比对
hisat2 -p <threads> -x <path to refseq.fa> -1 <trimmomatic_R1_1P> -2 <trimmomatic_R2_2P> -S <outputfilename.sam> --new-summary hista2.log
-x Ref/Chr #参考基因组文件路径
-1 01_trimmomaticFiltering/PR1_1P #输入文件
-2 01_trimmomaticFiltering/PR1_2P #输入文件
-S 02_hisat2Mapping/PR1.sam       #输出文件sam格式
--new-summary 1>02_hisat2Mapping/PR1_hisat2Mapping.log 2>&1 #输出日志

第三步：格式转换和排序
samtools view -@ <threads> -bhS 02_hisat2Mapping/PR1.sam -o 02_hisat2Mapping/PR1.bam
-b 默认下输出是 SAM 格式文件，该参数设置输出 BAM 格式
-h 默认下输出的 sam 格式文件不带 header，该参数设定输出sam文件时带 header 信息
-S 默认下输入是 BAM 文件，若是输入是 SAM 文件，则最好加该参数，否则有时候会报错
-@ 线程数
-o 输出文件名

samtools sort -m 5G -@ 10 02_hisat2Mapping/PR1.bam -o 02_hisat2Mapping/PR1.sort
-m 5G 设置每个线程运行时的内存大小，可以使用K，M和G表示内存大小。默认下是 500,000,000 即500M。对于处理大数据时，如果内存够用，则设置大点的值，以节约时间。
-o FILE 设置最终排序后的输出文件名,不用包含后缀名
-O FORMAT 设置最终输出的文件格式，可以是bam，sam或者cram，默认为bam
-@ INT 设置排序和压缩是的线程数量，默认是单线程

'''



'''
samtools其他功能：
index索引：
smatools index -b test_2.sorted.bam
-b 创建bai索引文件，未指定输出格式时，此参数为默认参数；
-c 创建csi索引文件，默认情况下，索引的最小间隔值为2^14，与bai格式一致；
-m INT 创建csi索引文件，最小间隔值2^INT

faidx索引（重测序常用）
samtools faidx genome.fasta
'''