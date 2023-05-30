#! /usr/bin/python
# _*_ coding: utf-8 _*_
# Author: 29398(赵子权)
# FileName: GTF_TO_GFF.py
# Time: 2023/5/31 12:18   
# Email: zzq@caf.ac.cn
# Software: PyCharm
import sys

inFile = open(sys.argv[1], 'r')

for line in inFile:
    if line[0] != '#':
        data = line.strip().split('\t')
        transcriptID = data[-1].split('transcript_id')[-1].split(';')[0].strip()[1:-1]
        geneID = data[-1].split('gene_id')[-1].split(';')[0].strip()[1:-1]
        data[-1] = f'"ID="{geneID}; "GID="{transcriptID}'
        print('\t'.join(data))