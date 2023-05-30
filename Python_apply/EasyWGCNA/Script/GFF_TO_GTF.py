#! /usr/bin/python
# _*_ coding: utf-8 _*_
# Author: 29398(赵子权)
# FileName: GFF_TO_GTF.py
# Time: 2023/5/31 12:11   
# Email: zzq@caf.ac.cn
# Software: PyCharm
import sys

inFile = open(sys.argv[1], 'r')

for line in inFile:
    if line[0] != '#':
        data = line.strip().split('\t')
        ID = ''
        if data[2] == "gene":
            ID = data[-1].split('ID=')[-1].split(';')[0]
        else:
            ID = data[-1].split('Parent=')[-1].split(';')[0]
        data[-1] = f'gene_id "{ID}"; transcript_id "{ID}"'
        print('\t'.join(data))