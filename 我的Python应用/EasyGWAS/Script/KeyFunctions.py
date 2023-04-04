#! /usr/bin/python
# _*_ coding: utf-8 _*_
# Author: 29398(赵子权)
# FileName: KeyFunctions.py
# Time: 2023/4/4 18:18   
# Email: zzq@caf.ac.cn
# Software: PyCharm


import os
import wget


def folder_exist_setup(folder):
    if os.path.exists(f'../WorkFile/{folder}'):
        pass
    else:
        os.mkdir(f'../WorkFile/{folder}')


def download_software(url, software_name):
    if os.path.exists(f'../Software'):
        pass
    else:
        os.mkdir(f'../Software')
    wget.download(url, f"./Software/{software_name}")


def assistant_menu():
    pass


def original_quality_control_01():
    download_software()
    folder_exist_setup(folder='original_quality_control_01')


def build_refseq_index_02():
    pass


def sam_to_bam_sort_03():
    pass


def mark_duplications_04():
    pass


def build_bam_index_05():
    pass


def haplotypecaller_06():
    pass


def gvcf_to_vcf_07():
    pass


def split_snp_indel_08():
    pass


def hard_filtration_09():
    pass


def merge_snp_indel_10():
    pass


def miss_maf_hardy_filtering_11():
    pass