# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
'''
sratoolkit（Ubuntu22）

安装：
sudo apt install sra-toolkit

下载SRA文件（下载出来的是sra格式文件，需要格式转换）：
prefetch SRR13624884 -O ./
-O 输出文件路径及文件名，建议不要指定文件名，就直接用SRR号即可
-h 查看帮助
-option-file file.txt 多个SRR同时下载时，指定一个下载列表。每行一个。

SRA转fastq格式：
fastq-dump SRR13624884.sra --gzip --split-3 -O ./
--gzip 输出文件以.fq.gz格式保存
--split-3 将双端分开，编程A_R1.fq.gz和A_R2.fq.gz的形式
-O 输出文件路径

'''