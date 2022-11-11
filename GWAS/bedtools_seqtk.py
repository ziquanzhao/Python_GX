# 编写人：赵子权
# 编写时间：2022/11/7 19:10
# 邮箱:2939818719@qq.com
import os

def main():
    while True:
        print('1.需要bedtools软件')
        print('2.需要参考基因组序列文件')
        print('3.序列位置文件。格式形如：染色体ID  起始位置    终止位置，每个一行。')
        answer = input('输入Y/y开始使用，输入N/n结束使用:')
        if answer == 'y' or answer == 'Y':
            reseq = input('请输入参考基因组所在绝对路径，如果不输入内容，默认为：/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa：')
            bedtools_path = input('请输入bedtools软件所在绝对路径，如果不输入内容，默认为：/mnt/storage/zhaoziquan/GWAS/software/bedtools2/bin/bedtools：')
            myseq = input('请输入一个输出文件的前缀名和位置，如果不输入，默认为当前目录下，叫myseq：')
            seq_postition = input('请输入索要提取序列的位置文件的绝对路径：')
            bedtools(seq_postition)
        else:
            print('\033[0;36m===========================\033[m')
            print('         欢迎下次使用!        ')
            print('\033[0;36m===========================\033[m')
            break

def bedtools(seq_postition, myseq='myseq', reseq='/mnt/storage/zhaoziquan/GWAS/1_bwaindex/xso-gene.fa', bedtools_path='/mnt/storage/zhaoziquan/GWAS/software/bedtools2/bin/bedtools'):
    os.system(f'{bedtools_path} getfasta -fi {reseq} -bed {seq_postition} -fo {myseq}.fasta')
    print(f'\033[0;36m您的结果已完成，保存在{myseq}\033[m')



if __name__ == '__main__':
    main()