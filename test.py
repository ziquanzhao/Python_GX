#! /usr/bin/python3
# coding=utf-8
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import sys

inFile = open(sys.argv[1], 'r')

for line in inFile:
    if line[0] != '#':
        data = line.strip().split('\t')
        transcriptID = data[-1].split('transcript_id')[-1].split(';')[0].strip()[1:-1]
        geneID = data[-1].split('gene_id')[-1].split(';')[0].strip()[1:-1]
        data[-1] = f'"ID="{geneID}; "GID="{transcriptID}'
        print('\t'.join(data))


