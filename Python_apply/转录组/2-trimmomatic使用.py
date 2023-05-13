# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

'''
1.安装
直接官网下载二进制文件，解压之后就是一个.jar文件，需要java环境。
'''

'''
2.使用
java -jar <path to trimmomatic_0.39.jar> 
PE 
-threads <threads> 
-phred33|-phred64 
-trimlog <trim.log> 
-basein <inputfile_R1.fq.gz> <inputfile_R2.fq.gz> #使用-basein标志命名正向文件，这样可以自动确定反向文件名称
-baseout <outputfile_R1_paired.fq.gz> <outputfile_R1_unpaired.fq.gz> <outputfile_R2_paired.fq.gz> <outputfile_R2_unpaired.fq.gz> #使用-baseout标志提供基本文件名，从中派生四个输出文件

ILLUMINACLIP:<fastaWithAdaptersEtc>:<seed mismatches>:<palindrome clip threshold>:<simple clip threshold>:<minAdapterLength>:<keepBothReads> 
    该步骤用于寻找并去除Illumina接头。
    a)fastaWithAdaptersEtc1: 指定包含所有接头、PCR序列等的fasta文件的路径。此文件中各种序列的命名决定了它们的使用方式；
    b)seed mismatches：指定仍允许执行完全匹配的最大不匹配数；
    c)palindrome clip threshold：指定两个成对接头reads之间的匹配对于双端回文read对齐的精度；
    d)Simple clip threshold：指定任何接头等序列与read之间的匹配精度；
    e)minAdapterLength：除了对齐分数之外，回文模式还可以验证检测到接头的最小长度。如果未指定，出于历史原因，默认为8个bp。但是，由于回文模式的假阳性率非常低，因此可以安全地减少，甚至减少到1，以允许删除较短的接头片段；
    f)keepBothReads：在回文模式检测到read测穿并删除接头序列后，反向读取包含与正向读取相同的序列信息。因此，默认行为是完全删除反向读取。通过为该参数指定true，反向读取也将被保留，这可能是有用的，例如，如果下游工具无法处理成对和非成对reads的组合。
    一般设置ILLUMINACLIP:/mnt/storage/zhaoziquan/GWAS/software/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10:2:true

SLIDINGWINDOW:<windowSize>:<requiredQuality> 
    当窗口内的平均质量低于阈值时，执行滑动窗口剔除。通过考虑多个碱基，单个质量差的碱基不会导致删除了在read后期高质量的数据。
    a)windowSize: 设定窗口涵盖碱基数量；
    b)requiredQuality: 设定需要的平均质量。
    一般设置SLIDINGWINDOW:4:15，较为严格，宽松一点可以设置5：20。5个碱基平均每个碱基质量数为20

MAXINFO:<targetLength>:<strictness>
    该步骤进行自适应质量微调，它平衡读取长度和错误率，根据需求获取长读取或者高质量，最大化节约成本。
    a)targetLength: 指定目标位置的读取长度；
    b)strictness: 这个值应该设置在0和1之间，它制定了保持尽可能多的读取长度与删除不正确的碱基之间的平衡。此参数值设置偏低<0.2有利于较长的读取，而偏高>0.8有利于读取正确性。
    一般不考虑这个参数

LEADING:<quality>
    从起始端开始去除低质量的碱基。只要一个碱基的质量值低于阈值，就会切除该碱基，并调查下一个碱基。
    quality: 指定保留碱基所需的最低质量。
    一般设置LEADING:3

TRAILING:<quality>
    从末端移除低质量的碱基。只要碱基的质量值低于阈值，则切除该碱基，并调查下一个碱基（因为Trimmomatic从3'prime end开始，将是位于刚切除碱基之前的碱基）。此方法可用于去除Illumina低质量段区域（质量分数标记为2），但官方建议使用SLIDINGWINDOW或MAXINFO代替。
    quality: 指定保留碱基所需的最低质量。
    一般设置TRAILING:3

CROP:<length>
    不管质量如何，从read末端删除碱基，指定read最大长度。
    length: 从read起始端开始要保留的长度。
    一般不考虑这个参数

HEADCROP:<length>
    不管质量如何，从read起始端端删除碱基。
    length: 从read起始端开始要切除的长度。
    看FastQC碱基质量图考虑切多少。HEADCROP:5
    
MINLEN:<length>
    此模块删除低于指定最小长度的读取。通常应该在所有其他处理步骤之后。此步骤删除的read将被计数，并包含在Trimmomatic摘要中显示的dropped reads计数中。
    length: 设置保留reads的最小长度。
    一般设置MINLEN:36

TOPHRED33/TOPHRED64
    质量分数的编码转换。该指令没有其他参数
    一般不用

-summary <statsSummaryFile>
过滤的摘要文件
'''

'''
示例：
java -jar {trimmomatic_path} PE -threads 60 -phred33 
{original_fq_data_path}{filename}_R1.fq.gz {original_fq_data_path}{filename}_R2.fq.gz 
-baseout {filename}.fq.gz 
-summary statssummaryfile.log
ILLUMINACLIP:/mnt/storage/zhaoziquan/GWAS/software/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10:2:true 
SLIDINGWINDOW:4:15 LEADING:3 TRAILING:3 MINLEN:36 HEADCROP:5
'''


