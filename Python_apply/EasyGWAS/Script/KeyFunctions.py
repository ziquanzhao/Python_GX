#! /usr/bin/python
# _*_ coding: utf-8 _*_
# Author: 29398(赵子权)
# FileName: KeyFunctions.py
# Time: 2023/4/4 18:18   
# Email: zzq@caf.ac.cn
# Software: PyCharm


import os
import wget
import re


os.system('pwd > ./workpath.txt')
with open('./workpath.txt', 'r') as file:
    WorkPath = re.sub('/Script\n', '', str(file.readline()))
os.system('rm ./workpath.txt')


def folder_exist_setup(folder):
    if os.path.exists(f'{WorkPath}/WorkFile/{folder}'):
        pass
    else:
        os.mkdir(f'{WorkPath}/WorkFile/{folder}')


def download_software(url, software_name):
    if os.path.exists(f'{WorkPath}/Software'):
        pass
    else:
        os.mkdir(f'{WorkPath}/Software')
    print('\033[1;36mDownloading...\033[0m')
    wget.download(url, f"{WorkPath}/Software/{software_name}.zip")
    print('\033[1;36m\nDownload completed!\033[0m')
    print('')
    print('\033[1;36mUnpacking and installing...\033[0m')
    os.system(f'unzip -d {WorkPath}/Software/ {WorkPath}/Software/{software_name}.zip')
    print('Unpacking and installation completed!')
    print('')
    print(f"\033[1;36mThe '{software_name}.zip' software was downloaded and unzipped into the '{WorkPath}/Software/{software_name}' folder.\033[0m")
    print('\033[1;36mIf you want to continue downloading, please select again.\033[0m')


def choose(shell_filepath):
    print('')
    print(f"\033[1;31m  In the 'WorkFile/{shell_filepath}/' directory, there is a shell script called '{shell_filepath}.sh', which contains all the codes to perform this step.\033[m")
    print("\033[1;31mYou can check whether it meets your requirements. Of course, you can also do it immediately without checking it.\033[m")
    print("\033[1;36mIf you don't want to execute it immediately, please enter: 1.\033[m")
    print("\033[1;36mIf you want to execute in the foreground immediately, please enter: 2.\033[m")
    answer = input("\033[1;36mIf you want to execute in the background immediately, please enter: 3.  :\033[m")
    try:
        if answer == '1':
            print('')
            print('')
            print('\033[1;36mOk, just use the "bash XXX.sh" command directly after checking.\033[m')
        elif answer == '2':
            print('')
            print('')
            print('Running...')
            print('')
            os.system(f'bash {WorkPath}/WorkFile/{shell_filepath}/{shell_filepath}.sh')
            print('')
            print('Run completed')
        elif answer == '3':
            print('')
            print('')
            print('Running in the background...')
            os.system(f'nohup bash {WorkPath}/WorkFile/{shell_filepath}/{shell_filepath}.sh >> {WorkPath}/WorkFile/{shell_filepath}/{shell_filepath}.log 2>&1 &')
        else:
            print("")
            raise Exception("\033[1;36mYou can only select one character from '1/2/3' and cannot enter other characters.\033[0m")
    except Exception as Error:
        print(Error)
        print('\033[1;36mOk, just use the "bash XXX.sh" command directly after checking.\033[m')


def software_menu():
    print("")
    print("")
    print("\033[1;31m===========================\033[0m\033[0m\033[1;36mSoftware Menu\033[0m\033[1;31m=============================\033[0m")
    print("\033[1;31m==\033[0m 0. Exit download (If not exited, please try several times!)      \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 1. Trimmomatic-0.39                                              \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 2. Bwa-0.7.17                                                    \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 3. Samtools-1.15.1                                               \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 4. Gatk-4.4.0.0                                                  \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 5. Picard-3.0.0                                                  \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 6. Plink-2                                                       \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 7. Fastqc-0.12.1                                                 \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 8. Bcftools-1.17                                                 \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 9. Tassel-5                                                      \033[1;31m==\033[0m")
    print("\033[1;31m=====================================================================\033[0m")


def software_download_menu():
    while True:
        software_menu()
        answer = input('\033[1;31mPlease select the serial number of the software you need to download:\033[0m')
        print('')
        print('')
        print('')
        print('')
        try:
            if answer == '0':
                break
            elif answer == '1':
                if os.path.exists(f'{WorkPath}/Software/Trimmomatic-0.39-main'):
                    print("\033[1;31mThe 'Trimmomatic-0.39-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Trimmomatic-0.39' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Trimmomatic-0.39' software is not installed, please delete the 'Trimmomatic-0.39-main' folder and the 'Trimmomatic-0.39.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_01 = 'https://codeload.github.com/ziquanzhao/Trimmomatic/zip/refs/heads/main'
                    download_software(url=your_url_01, software_name='Trimmomatic-0.39')
            elif answer == '2':
                if os.path.exists(f'{WorkPath}/Software/Bwa-0.7.17-main'):
                    print("\033[1;31mThe 'Bwa-0.7.17-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Bwa-0.7.17' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Bwa-0.7.17' software is not installed, please delete the 'Bwa-0.7.17-main' folder and the 'Bwa-0.7.17.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_02 = 'https://codeload.github.com/ziquanzhao/Bwa/zip/refs/heads/main'
                    download_software(url=your_url_02, software_name='Bwa-0.7.17')
            elif answer == '3':
                if os.path.exists(f'{WorkPath}/Software/Samtools-1.15.1-main'):
                    print("\033[1;31mThe 'Samtools-1.15.1-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Samtools-1.15.1' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Samtools-1.15.1' software is not installed, please delete the 'Samtools-1.15.1-main' folder and the 'Samtools-1.15.1.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_03 = 'https://codeload.github.com/ziquanzhao/Samtools-1.15.1/zip/refs/heads/main'
                    download_software(url=your_url_03, software_name='Samtools-1.15.1')
            elif answer == '4':
                if os.path.exists(f'{WorkPath}/Software/Gatk-4.4.0.0-main'):
                    print("\033[1;31mThe 'Gatk-4.4.0.0-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Gatk-4.4.0.0' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Gatk-4.4.0.0' software is not installed, please delete the 'Gatk-4.4.0.0-main' folder and perform this step again.\033[0m")
                    pass
                else:
                    os.mkdir(f'{WorkPath}/Software/Gatk-4.4.0.0-main')
                    print('')
                    print("\033[1;36mThe GATK software package is relatively large. Please download it by yourself according to the link provided below. Please put the file in the' ../software/Gatk-4.4.0.0' directory after downloading.\033[0m")
                    print('\033[1;31mhttps://drive.google.com/file/d/11mgbYHOOVsztpxgg1UUkOGbjfkNKwpm2/view\033[0m')
            elif answer == '5':
                if os.path.exists(f'{WorkPath}/Software/Picard-3.0.0-main'):
                    print("\033[1;31mThe 'Picard-3.0.0-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Picard-3.0.0' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Picard-3.0.0' software is not installed, please delete the 'Picard-3.0.0-main' folder and the 'Samtools-1.15.1.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_05 = 'https://codeload.github.com/ziquanzhao/Picard-3.0.0/zip/refs/heads/main'
                    download_software(url=your_url_05, software_name='Picard-3.0.0')
            elif answer == '6':
                if os.path.exists(f'{WorkPath}/Software/Plink-2-main'):
                    print("\033[1;31mThe 'Plink-2-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Plink-2' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Plink-2' software is not installed, please delete the 'Plink-2-main' folder and perform this step again.\033[0m")
                    pass
                else:
                    os.mkdir(f'{WorkPath}/Software/Plink-2-main')
                    print('')
                    print("\033[1;36mThe Plink2 software package is relatively large. Please download it by yourself according to the link provided below. Please put the file in the' ../software/Plink-2' directory after downloading.\033[0m")
                    print('\033[1;31mhttps://drive.google.com/file/d/1pWYVje3N5w0bIp2OiHqzlbZ_X2vLAGpM/view\033[0m')
            elif answer == '7':
                if os.path.exists(f'{WorkPath}/Software/Fastqc-0.12.1-main'):
                    print("\033[1;31mThe 'Fastqc-0.12.1-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Fastqc-0.12.1' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Fastqc-0.12.1' software is not installed, please delete the 'Fastqc-0.12.1-main' folder and the 'Fastqc-0.12.1.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_07 = 'https://codeload.github.com/ziquanzhao/Fastqc-0.12.1/zip/refs/heads/main'
                    download_software(url=your_url_07, software_name='Fastqc-0.12.1')
            elif answer == '8':
                if os.path.exists(''):
                    print("\033[1;31mThe 'Bcftool-1.17-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Bcftool-1.17' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Bcftool-1.17' software is not installed, please delete the 'Fastqc-0.12.1-main' folder and the 'Bcftool-1.17.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_08 = 'https://codeload.github.com/ziquanzhao/Bcftools-1.17/zip/refs/heads/main'
                    download_software(url=your_url_08, software_name='Bcftool-1.17')
            elif answer == '9':
                if os.path.exists(''):
                    print("\033[1;31mThe 'Tassel-5-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Tassel-5' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Tassel-5' software is not installed, please delete the 'Fastqc-0.12.1-main' folder and the 'Tassel-5.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_09 = 'https://codeload.github.com/ziquanzhao/Tassel-5/zip/refs/heads/main'
                    download_software(url=your_url_09, software_name='Tassel-5')
            else:
                print("")
                raise Exception("\033[1;36mYou can only select one character from '0/1/2/3/4/5/6/7/8/9' and cannot enter other characters.\033[0m")
        except Exception as Error:
            print(Error)
            print('\033[1;36mAn unknown error has occurred, please contact the author to solve it!\033[m')
        else:
            software_download_menu()


def check_resequencing_quality_13(fq_data_filename, threads=4):
    """

    :param threads: 线程数
    :param fq_data_filename:重测序数据的绝对路径，注意符合命名规范。XXX_R1.fq.gz和XXX_R2.fq.gz
    -o --outdir FastQC生成的报告文件的储存路径
    --extract 结果文件解压缩
    --noextract 结果文件压缩
    -t --threads 选择程序运行的线程数，每个线程会占用250MB内存，越多越快咯
    -c --contaminants 污染物选项，输入的是一个文件，格式是Name [Tab] Sequence，里面是可能的污染序列，如果有这个选项，FastQC会在计算时候评估污染的情况，并在统计的时候进行分析，一般用不到
    -a --adapters 也是输入一个文件，文件的格式Name [Tab] Sequence，储存的是测序的adpater序列信息，如果不输入，目前版本的FastQC就按照通用引物来评估序列时候有adapter的残留
    -q --quiet 安静运行模式，一般不选这个选项的时候，程序会实时报告运行的状况。
    """
    folder_exist_setup(folder='CheckResequencingQuality13')
    with open(f'{WorkPath}/WorkFile/CheckResequencingQuality13/CheckResequencingQuality13.sh', 'w') as check_reseq_quality:
        check_reseq_quality.write('#!/bin/bash\n')
        for filename in os.listdir(fq_data_filename):
            if '_R1.fq.gz' in filename:
                filename = re.sub('_R1.fq.gz', '', filename)
                check_reseq_quality.write(f'{WorkPath}/Software/Fastqc-0.12.1-main/fastqc  -t {threads} {fq_data_filename}{filename}_R1.fq.gz {fq_data_filename}{filename}_R2.fq.gz -o {WorkPath}/WorkFile/CheckResequencingQuality13/\n')
    choose(shell_filepath='CheckResequencingQuality13')
    print('\033[1;31mPlease carefully review the results, which will be an important basis for parameter setting of raw data filtering in the next step!\033[m')
    print("\033[1;31mIt's very important, please take it seriously!\033[m")


def original_quality_control_01(fq_data_filename, sequencing_mode='PE', threads=4, base_quality_coding_format='-phred33', illuminaclip='TruSeq3-PE.fa:2:30:10:2:true', slidingwindow='4:15', leading=3, trailing=3, minlen=36, headcrop=5):
    """

    :param fq_data_filename: "重测序数据的绝对路径，注意符合命名规范。XXX_R1.fq.gz和XXX_R2.fq.gz"
    :param sequencing_mode:"双端测序选PE，单端选SE，默认双端"
    :param threads:"线程数"
    :param base_quality_coding_format:"碱基质量编码格式，默认phred-33"
    :param illuminaclip:
        "fastaWithAdaptersEtc:seedMismatches:palindrome clip threshold:simple clip threshold:minAdapterLength:keepBothReads
        fastaWithAdaptersEtc：指定包含接头和引物序列（所有被视为污染的序列）的 fasta 文件路径，Trimmomatic 自带了一个包含 Illumina 平台接头和引物序列的 fasta 文件，可以直接用这个。
        seedMismatches：指定第一步 seed 搜索时允许的错配碱基个数，例如 2。
        palindrome clip threshold：指定针对 PE 的 palindrome clip 模式下，需要 R1 和 R2 之间至少多少比对分值（上图中 D 模式），才会进行接头切除，例如 30。
        simple clip threshold：指定切除接头序列的最低比对分值（上图 A/B 模式），通常 7-15 之间。
        minAdapterLength：只对 PE 测序的 palindrome clip 模式有效，指定 palindrome 模式下可以切除的接头序列最短长度，由于历史的原因，默认值是 8，但实际上 palindrome 模式可以切除短至 1bp 的接头污染，所以可以设置为 1。
        keepBothReads：只对 PE 测序的 palindrome clip 模式有效，这个参数很重要, R1 和 R2 在去除了接头序列之后剩余的部分是完全反向互补的，默认参数 false，意味着整条去除与 R1 完全反向互补的 R2，当做重复去除掉，但在有些情况下，例如需要用到 paired reads 的 bowtie2 流程，就要将这个参数改为 true，否则会损失一部分 paired reads。"
    :param slidingwindow:
        "SLIDINGWINDOW:<windowSize>:<requiredQuality>
        滑窗剪切，统计滑窗口中所有碱基的平均质量值，如果低于设定的阈值，则切掉窗口。
        SLIDINGWINDOW:4:15  #设置 4bp 窗口，碱基平均质量值阈值 15
        widowSize:设置窗口大小
        requiredQuality：设置窗口碱基平均质量阈值"
    :param leading:"从 reads 的起始端开始切除质量值低于设定的阈值的碱基，直到有一个碱基其质量值达到阈值"
    :param trailing:"从 reads 的末端开始切除质量值低于设定阈值的碱基，直到有一个碱基质量值达到阈值。Illumina 平台有些低质量的碱基质量值被标记为 2 ，所以设置为 3 可以过滤掉这部分低质量碱基。"
    :param minlen:"设定一个最短 read 长度，当 reads 经过前面的过滤之后，如果保留下来的长度低于这个阈值，整条 reads 被丢弃。被丢弃的 reads 数会被统计在 Trimmomatic 日志的 dropped reads 中。"
    :param headcrop:"不管碱基质量，从 reads 的起始开始直接切除部分碱基。"
    """
    folder_exist_setup(folder='OriginalQualityControl01')
    with open(f'{WorkPath}/WorkFile/OriginalQualityControl01/OriginalQualityControl01.sh', 'w') as trim:
        trim.write('#!/bin/bash\n')
        for filename in os.listdir(fq_data_filename):
            if '_R1.fq.gz' in filename:
                filename = re.sub('_R1.fq.gz', '', filename)
                trim.write(
                    f'java -jar {WorkPath}/Software/Trimmomatic-0.39-main/trimmomatic-0.39.jar {sequencing_mode} -threads {threads} {base_quality_coding_format} {fq_data_filename}{filename}_R1.fq.gz {fq_data_filename}{filename}_R2.fq.gz -baseout {WorkPath}/WorkFile/OriginalQualityControl01/{filename}.fq.gz ILLUMINACLIP:{WorkPath}/Software/Trimmomatic-0.39-main/adapters/{illuminaclip} SLIDINGWINDOW:{slidingwindow} LEADING:{leading} TRAILING:{trailing} MINLEN:{minlen} HEADCROP:{headcrop}\n')
    choose(shell_filepath='OriginalQualityControl01')


def build_refseq_index_02(reference_genome):
    """

    :param reference_genome: "参考基因组的绝对路经加文件名"
    """
    folder_exist_setup(folder='BuildRefseqIndex02')
    os.system(f'cp {reference_genome} {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta')
    os.system(f'rm {WorkPath}/WorkFile/BuildRefseqIndex02/*.dict')
    with open(f'{WorkPath}/WorkFile/BuildRefseqIndex02/BuildRefseqIndex02.sh', 'w') as refseq_index:
        refseq_index.write('#!/bin/bash\n')
        refseq_index.write(f'{WorkPath}/Software/Bwa-0.7.17-main/bwa index -a bwtsw ../WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta -p {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta\n')
        refseq_index.write(f'{WorkPath}/Software/Samtools-1.15.1-main/samtools faidx ../WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta > {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta.fai\n')
        refseq_index.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar CreateSequenceDictionary -REFERENCE {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta -OUTPUT {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.dict')
    choose(shell_filepath='BuildRefseqIndex02')


def sam_to_bam_sort_03(threads=4, tmp_dir=f'{WorkPath}/WorkFile/', validation_stringency='SILENT', sort_order='coordinate'):
    """

    :param threads: 线程数
    :param tmp_dir: 提供一个目录，用于放临时文件，完成后会自动删除
    :param validation_stringency: 检验Sam文件的格式正确与否，设置为'SILENT'可提高性能。
    :param sort_order:输出文件的排序方式，默认coordinate（坐标），意思是按照染色体上的顺序排序。
    """
    folder_exist_setup(folder='SamToBamSort03')
    with open(f'{WorkPath}/WorkFile/SamToBamSort03/SamToBamSort03.sh', 'w') as trans_sort:
        trans_sort.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/OriginalQualityControl01/'):
            if "_1P.fq.gz" in filename:
                filename = re.sub('_1P.fq.gz', '', filename)
                trans_sort.write(f'{WorkPath}/Software/Bwa-0.7.17-main/bwa mem -t {threads} -M -R "@RG\tID:{filename}\tLB:{filename}\tPL:illumina\tPU:{filename}\tSM:{filename}\" {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta {WorkPath}/WorkFile/OriginalQualityControl01/{filename}_1P.fq.gz {WorkPath}/WorkFile/OriginalQualityControl01/{filename}_2P.fq.gz > {WorkPath}/WorkFile/SamToBamSort03/{filename}.sam'+"\n")
                trans_sort.write(f"java -jar {WorkPath}/Software/Picard-3.0.0-main/picard.jar SortSam -TMP_DIR {tmp_dir} -VALIDATION_STRINGENCY {validation_stringency} -INPUT {WorkPath}/WorkFile/SamToBamSort03/{filename}.sam -OUTPUT {WorkPath}/WorkFile/SamToBamSort03/{filename}_sort.bam -SORT_ORDER {sort_order}\n")
                trans_sort.write(f'rm {WorkPath}/WorkFile/SamToBamSort03/{filename}.sam\n')
    os.system(f"sed -i 's/\\t/\\\\t/g' {WorkPath}/WorkFile/SamToBamSort03/SamToBamSort03.sh")
    choose(shell_filepath='SamToBamSort03')


def mark_duplications_04(max_file_handles_for_ends_map=800, remove_duplicates='false', validation_stringency='LENIENT'):
    """

    :param max_file_handles_for_ends_map: 将读取结束溢出到磁盘时保持打开状态的最大文件句柄数。将此数字设置为略低于每个进程可能打开的文件的最大数目。这个数字可以通过在Unix系统上执行“ulimit -n”命令找到
    :param remove_duplicates: 官网是flase。来丢弃duplicated序列。对于是否选择标记或者删除，对结果应该没有什么影响，GATK官方流程里面给出的例子是仅做标记不删除。这里定义的重复序列是这样的：如果两条reads具有相同的长度而且比对到了基因组的同一位置，那么就认为这样的reads是由PCR扩增而来，就会被GATK标记。
    :param validation_stringency: 在BWA 比对生成SAM文件时，将没有map到基因组上的read归到了ref以外的区域，其MAPQ值不为0，而Picard认为这些read是不应该出现的，所以会报错。如果想忽略报错的话，就使用这行代码。
    """
    folder_exist_setup(folder='MarkDuplications04')
    with open(f'{WorkPath}/WorkFile/MarkDuplications04/MarkDuplications04.sh', 'w') as mark_dup:
        mark_dup.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/SamToBamSort03/'):
            if '_sort.bam' in filename:
                filename = re.sub('.bam', '', filename)
                mark_dup.write(f'java -jar {WorkPath}/Software/Picard-3.0.0-main/picard.jar MarkDuplicates -MAX_FILE_HANDLES_FOR_READ_ENDS_MAP {max_file_handles_for_ends_map} -REMOVE_DUPLICATES {remove_duplicates} -INPUT {WorkPath}/WorkFile/SamToBamSort03/{filename}.bam -OUTPUT {WorkPath}/WorkFile/MarkDuplications04/{filename}_dedup.bam -METRICS_FILE {WorkPath}/WorkFile/MarkDuplications04/{filename}_dedup.metrics -VALIDATION_STRINGENCY {validation_stringency}\n')
    choose(shell_filepath='MarkDuplications04')


def build_bam_index_05():
    folder_exist_setup(folder='BuildBamIndex05')
    with open(f'{WorkPath}/WorkFile/BuildBamIndex05/BuildBamIndex05.sh', 'w') as bam_index:
        bam_index.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/MarkDuplications04/'):
            if '_sort_dedup.bam' in filename:
                bam_index.write(f'{WorkPath}/Software/Samtools-1.15.1-main/samtools index {WorkPath}/WorkFile/MarkDuplications04/{filename} > {WorkPath}/WorkFile/MarkDuplications04/{filename}.bai\n')
    choose(shell_filepath='BuildBamIndex05')


def haplotypecaller_06(lachesis_group='Lachesis_group', chr_number=15):
    folder_exist_setup(folder='Haplotypecaller06')
    with open(f'{WorkPath}/WorkFile/Haplotypecaller06/Haplotypecaller06.sh', 'w') as haplotype:
        haplotype.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/MarkDuplications04'):
            if '.bai' not in filename and '.metrics' not in filename and '_sort_dedup.bam' in filename:
                filename = re.sub('_sort_dedup.bam', '', filename)
                for Lachesis_group in range(1, chr_number+1, 1):
                    haplotype.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar HaplotypeCaller -R {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta -I {WorkPath}/WorkFile/MarkDuplications04/{filename}_sort_dedup.bam -ERC GVCF -L {lachesis_group}{Lachesis_group} -O {WorkPath}/WorkFile/Haplotypecaller06/{filename}_chr{Lachesis_group}.g.vcf\n')
    choose(shell_filepath='Haplotypecaller06')


def gvcf_to_vcf_07(chr_number=15):
    folder_exist_setup(folder='GvcfToVcf07')
    with open(f'{WorkPath}/WorkFile/GvcfToVcf07/GvcfToVcf07.sh', 'w') as gvcftovcf:
        gvcftovcf.write('#!/bin/bash\n')
        for chr_num in range(1, chr_number+1, 1):
            lachesis_group = []
            for filename in os.listdir(f'{WorkPath}/WorkFile/Haplotypecaller06'):
                if '.idx' not in filename and 'chr1.g.vcf' in filename:
                    filename = re.sub('_chr1.g.vcf', '', filename)
                    lachesis_group.append(f'-V {WorkPath}/WorkFile/Haplotypecaller06/{filename}_chr{chr_num}.g.vcf')
            lachesis_group = ' '.join(lachesis_group)
            gvcftovcf.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar CombineGVCFs -R {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta {lachesis_group} -O {WorkPath}/WorkFile/GvcfToVcf07/Chr{chr_num}.g.vcf\n')
            gvcftovcf.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar GenotypeGVCFs -R {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta -V {WorkPath}/WorkFile/GvcfToVcf07/Chr{chr_num}.g.vcf -O {WorkPath}/WorkFile/GvcfToVcf07/Chr{chr_num}.vcf\n')
    choose(shell_filepath='GvcfToVcf07')


def split_snp_indel_08():
    folder_exist_setup(folder='SplitSnpIndel08')
    with open(f'{WorkPath}/WorkFile/SplitSnpIndel08/SplitSnpIndel08.sh', 'w') as splitSnpIndel:
        splitSnpIndel.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/GvcfToVcf07'):
            if '.idx' not in filename and '.g.' not in filename and '.vcf' in filename:
                filename = re.sub('Chr', '', filename)
                filename = re.sub('.vcf', '', filename)
                splitSnpIndel.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar SelectVariants -R {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta -V {WorkPath}/WorkFile/GvcfToVcf07/Chr{filename}.vcf -O {WorkPath}/WorkFile/SplitSnpIndel08/Chr{filename}_snp.vcf -L Lachesis_group{filename} --select-type-to-include SNP\n')
                splitSnpIndel.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar SelectVariants -R {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta -V {WorkPath}/WorkFile/GvcfToVcf07/Chr{filename}.vcf -O {WorkPath}/WorkFile/SplitSnpIndel08/Chr{filename}_indel.vcf -L Lachesis_group{filename} --select-type-to-include INDEL\n')
    choose(shell_filepath='SplitSnpIndel08')


def density_plot(plotfilename):
    plotfilenameid = re.sub('.recode.table', '', plotfilename)
    with open(f'{WorkPath}/WorkFile/CheckSnpIndelQuality14/densityplot.r', 'a') as density:
        density.write(f"pdf(file = '{WorkPath}/WorkFile/CheckSnpIndelQuality14/{plotfilename}.pdf', width = 16, height = 3)\n")
        density.write("par(mfrow = c(1,5))\n")
        density.write(f"filetest <- read.table(file = '{WorkPath}/WorkFile/CheckSnpIndelQuality14/{plotfilename}', header = T)\n")
        density.write("filetest <- filetest[complete.cases(filetest),]\n")
        density.write("col_name <- colnames(filetest)\n")
        density.write("for (i in seq(1,length(colnames(filetest)))) {\n")
        density.write(f"  plot(density(filetest[,i]), col = 'red', main = paste('{plotfilenameid}', col_name[i], sep = '-'), xlab = '')\n")
        density.write("}\n")
        density.write("dev.off()\n")
        density.write("\n")


def check_snp_indel_quality_14():
    folder_exist_setup(folder='CheckSnpIndelQuality14')
    with open(f'{WorkPath}/WorkFile/CheckSnpIndelQuality14/CheckSnpIndelQuality14.sh', 'w') as check_snpindel_quality:
        check_snpindel_quality.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/SplitSnpIndel08'):
            if '_snp.vcf' in filename and '.idx' not in filename:
                filename = re.sub('_snp.vcf', '', filename)
                check_snpindel_quality.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar VariantsToTable -V {WorkPath}/WorkFile/SplitSnpIndel08/{filename}_snp.vcf -F QD -F QUAL -F SOR -F FS -F MQ -O {WorkPath}/WorkFile/CheckSnpIndelQuality14/{filename}_snp.recode.table\n')
                check_snpindel_quality.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar VariantsToTable -V {WorkPath}/WorkFile/SplitSnpIndel08/{filename}_indel.vcf -F QD -F QUAL -F SOR -F FS -F MQ -O {WorkPath}/WorkFile/CheckSnpIndelQuality14/{filename}_indel.recode.table\n')
    choose(shell_filepath='CheckSnpIndelQuality14')
    print("")
    print('\033[1;36mThe data you need is already in the corresponding folder. But simple data are obscure.\033[m')
    print('\033[1;36mI can help you display them graphically. Do you need this? \033[m')
    answer = input('\033[1;36mIf necessary, please enter: y/Y/yes/YES; If not, please enter: n/y/no/no. ：\033[m')
    print("")
    try:
        if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'YES':
            if os.path.exists(f'{WorkPath}/WorkFile/CheckSnpIndelQuality14/densityplot.r'):
                os.system(f'rm {WorkPath}/WorkFile/CheckSnpIndelQuality14/densityplot.r')
            else:
                pass
            for filename in os.listdir(f'{WorkPath}/WorkFile/CheckSnpIndelQuality14'):
                if '.recode.table' in filename and '.pdf' not in filename:
                    density_plot(plotfilename=filename)
            print("")
            print("\033[1;31mR script is written, do you want to execute it directly? \033[m")
            youranswer = input("\033[1;31mIf it needs to be executed immediately, please enter: 1; If you don't want to execute it immediately, please enter: 2. :\033[m")
            if youranswer == '1':
                print("")
                print("\033[1;36mStart drawing, please wait a moment...\033[m")
                os.system(f"Rscript {WorkPath}/WorkFile/CheckSnpIndelQuality14/densityplot.r")
                print(f"\033[1;36mThe drawing has been completed, please go to the '{WorkPath}/WorkFile/CheckSnpIndelQuality14/' directory to view it.\033[m")
            elif youranswer == '2':
                print("")
                print(f"\033[1;36mThe R script is in the '{WorkPath}/WorkFile/CheckSnpIndelQuality14/' directory. You can check it and execute it.\033[m")
        elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'NO':
            pass
        else:
            print("")
            raise Exception("\033[1;36mYou can only select one character from 'y/Y/yes/YES/n/y/no/no' and cannot enter other characters.\033[0m")
    except Exception as Error:
        print(Error)


def hard_filtration_09(snp_qd_filter=2.0, snp_qd_filtername='QD2', snp_sor_filter=3.0, snp_sor_filtername='SOR3', snp_fs_filter=30.0, snp_fs_filtername='FS30', snp_mq_filter=50.0, snp_mq_filtername='MQ50', indel_qd_filter=2.0, indel_qd_filtername='QD2', indel_sor_filter=5.0, indel_sor_filtername='SOR5', indel_fs_filter=50.0, indel_fs_filtername='FS50', indel_mq_filter=50.0, indel_mq_filtername='MQ50'):
    """

    :param snp_qd_filter:
    :param snp_qd_filtername:
    :param snp_sor_filter:
    :param snp_sor_filtername:
    :param snp_fs_filter:
    :param snp_fs_filtername:
    :param snp_mq_filter:
    :param snp_mq_filtername:
    :param indel_qd_filter:
    :param indel_qd_filtername:
    :param indel_sor_filter:
    :param indel_sor_filtername:
    :param indel_fs_filter:
    :param indel_fs_filtername:
    :param indel_mq_filter:
    :param indel_mq_filtername:
    具体参照如下解释
    https://zhuanlan.zhihu.com/p/34878471
    https://gatk.broadinstitute.org/hc/en-us/articles/360035890471-Hard-filtering-germline-short-variants
    """
    folder_exist_setup(folder='HardFiltration09')
    with open(f'{WorkPath}/WorkFile/HardFiltration09/HardFiltration09.sh', 'w') as hardFilter:
        hardFilter.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/SplitSnpIndel08'):
            if 'snp' in filename and '.vcf' in filename and '.idx' not in filename:
                filename = re.sub('.vcf', '', filename)
                hardFilter.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar VariantFiltration -V {WorkPath}/WorkFile/SplitSnpIndel08/{filename}.vcf -R {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta '
                                 f'-filter "QD < {snp_qd_filter}" --filter-name "{snp_qd_filtername}" '
                                 f'-filter "SOR > {snp_sor_filter}" --filter-name "{snp_sor_filtername}" '
                                 f'-filter "FS > {snp_fs_filter}" --filter-name "{snp_fs_filtername}" '
                                 f'-filter "MQ < {snp_mq_filter}" --filter-name "{snp_mq_filtername}" '
                                 f'--cluster-window-size 10 --cluster-size 3 -O {WorkPath}/WorkFile/HardFiltration09/{filename}_filter.vcf\n')
                hardFilter.write(f'grep -E \'#|PASS\' {WorkPath}/WorkFile/HardFiltration09/{filename}_filter.vcf > {WorkPath}/WorkFile/HardFiltration09/{filename}_pass.vcf\n')
            elif 'indel' in filename and '.vcf' in filename and '.idx' not in filename:
                filename = re.sub('.vcf', '', filename)
                hardFilter.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar VariantFiltration -V {WorkPath}/WorkFile/SplitSnpIndel08/{filename}.vcf -R {WorkPath}/WorkFile/BuildRefseqIndex02/YourReferenceGenome.fasta '
                                 f'-filter "QD < {indel_qd_filter}" --filter-name "{indel_qd_filtername}" '
                                 f'-filter "SOR > {indel_sor_filter}" --filter-name "{indel_sor_filtername}" '
                                 f'-filter "FS > {indel_fs_filter}" --filter-name "{indel_fs_filtername}" '
                                 f'-filter "MQ < {indel_mq_filter}" --filter-name "{indel_mq_filtername}" '
                                 f'-O {WorkPath}/WorkFile/HardFiltration09/{filename}_filter.vcf\n')
                hardFilter.write(f'grep -E \'#|PASS\' {WorkPath}/WorkFile/HardFiltration09/{filename}_filter.vcf > {WorkPath}/WorkFile/HardFiltration09/{filename}_pass.vcf\n')
    choose(shell_filepath='HardFiltration09')


def merge_snp_indel_10():
    folder_exist_setup(folder='MergeSnpIndel10')
    with open(f'{WorkPath}/WorkFile/MergeSnpIndel10/MergeSnpIndel10.sh', 'w') as mergeSnpIndel:
        mergeSnpIndel.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/HardFiltration09'):
            if '_snp_pass.vcf' in filename and '.idx' not in filename:
                filename = re.sub('_snp_pass.vcf', '', filename)
                mergeSnpIndel.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar MergeVcfs -I {WorkPath}/WorkFile/HardFiltration09/{filename}_snp_pass.vcf -I {WorkPath}/WorkFile/HardFiltration09/{filename}_indel_pass.vcf -O {WorkPath}/WorkFile/MergeSnpIndel10/{filename}_HardFilter.vcf.gz\n')
    choose(shell_filepath='MergeSnpIndel10')


def gvcfmerge():
    gzvcf = []
    for i in os.listdir(f'{WorkPath}/WorkFile/MergeSnpIndel10'):
        if '_HardFilter.vcf.gz' in i and '.tbi' not in i:
            gzvcf.append(f'{WorkPath}/WorkFile/MergeSnpIndel10/{i}')
    gzvcf = ' '.join(gzvcf)
    with open(f'{WorkPath}/WorkFile/MergeSnpIndel10/gvcfmerge.sh', 'w') as vcf:
        vcf.write(f'{WorkPath}/Software/Bcftools-1.17-main/bcftools concat {gzvcf} -o {WorkPath}/WorkFile/MergeSnpIndel10/AllSample.vcf.gz')
    os.system(f'bash {WorkPath}/WorkFile/MergeSnpIndel10/gvcfmerge.sh')


def miss_maf_hardy_filtering_11(geno=0.1, maf=0.05, hwe=1e-6, vcf_max_dp=50, vcf_min_dp=4, vcf_min_gq=10, min_alleles=2, max_alleles=2, var_min_qual=30):
    """
    --geno 0.1 --mind 0.1 --maf 0.01 --hwe 1e-4,这根据13_Missing_rate_statistics.py绘图结果设置。GWAS项目采用的MAF阈值在0.01-0.05之间，取决于样本大小.
    我们的数据缺失率很严重，所以--geno，--mind要尽量宽松一些
    --allow-extra-chr,如果染色体是非数字，加上这个参数。
    :param geno:
    :param maf:
    :param hwe:
    :param vcf_max_dp: --vcf-max-dp 50 --vcf-min-dp 4.位点最大深度50，最小深度4.一般来说，最下深度是平均深度的三分之一到四分之一。最大深度是平均深度的3到5倍。
    :param vcf_min_dp:
    :param vcf_min_gq: QG也是一个衡量质量的指标，看情况设置吧。
    :param min_alleles: --min-alleles 2 --max-alleles 2。只要双等位基因的情况，多等位基因不要，单等位基因也不要。
    :param max_alleles:
    :param var_min_qual:过滤掉QUAL小于30的。GATK时也可以做
    """
    folder_exist_setup(folder='MissMafHardyFiltering11')
    with open(f'{WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyFiltering11.sh', 'w') as missMafHardy:
        missMafHardy.write('#!/bin/bash\n')
        missMafHardy.write(f'{WorkPath}/Software/Plink-2-main/plink2 --vcf {WorkPath}/WorkFile/MergeSnpIndel10/AllSample.vcf.gz --export vcf --allow-extra-chr '
                           f'--geno {geno} --maf {maf} --hwe {hwe} '
                           f'--vcf-max-dp {vcf_max_dp} --vcf-min-dp {vcf_min_dp} --vcf-min-gq {vcf_min_gq} '
                           f'--min-alleles {min_alleles} --max-alleles {max_alleles} --var-min-qual {var_min_qual} --out {WorkPath}/WorkFile/MissMafHardyFiltering11/ALLSample_FinalReasult --threads 4\n')
    choose(shell_filepath='MissMafHardyFiltering11')


def miss_maf_hardy_statistics_15():
    folder_exist_setup(folder='MissMafHardyFiltering11')
    with open(f'{WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyStatistics15.sh', 'w') as mmh_statistics:
        mmh_statistics.write('#!/bin/bash\n')
        mmh_statistics.write(f'{WorkPath}/Software/Plink-2-main/plink2 --vcf {WorkPath}/WorkFile/MergeSnpIndel10/AllSample.vcf.gz --allow-extra-chr --make-bed --max-alleles 2 --out {WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics --threads 4\n')
        mmh_statistics.write(f'{WorkPath}/Software/Plink-2-main/plink2 -bfile {WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics --missing --out {WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics --allow-extra-chr --threads 4\n')
        mmh_statistics.write(f'{WorkPath}/Software/Plink-2-main/plink2 -bfile {WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics --freq --out {WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics --allow-extra-chr --threads 4\n')
        mmh_statistics.write(f'{WorkPath}/Software/Plink-2-main/plink2 -bfile {WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics --hardy --out {WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics --allow-extra-chr --threads 4\n')
    print('')
    print(f"\033[1;31m  In the 'WorkFile/MissMafHardyFiltering11/' directory, there is a shell script called 'MissMafHardyStatistics15.sh', which contains all the codes to perform this step.\033[m")
    print("\033[1;31mYou can check whether it meets your requirements. Of course, you can also do it immediately without checking it.\033[m")
    print("\033[1;36mIf you don't want to execute it immediately, please enter: 1.\033[m")
    print("\033[1;36mIf you want to execute in the foreground immediately, please enter: 2.\033[m")
    answer = input("\033[1;36mIf you want to execute in the background immediately, please enter: 3.  :\033[m")
    try:
        if answer == '1':
            print('')
            print('')
            print('\033[1;36mOk, just use the "bash XXX.sh" command directly after checking.\033[m')
        elif answer == '2':
            print('')
            print('')
            print('Running...')
            print('')
            os.system(f'bash {WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyStatistics15.sh')
            print('')
            print('Run completed')
        elif answer == '3':
            print('')
            print('')
            print('Running in the background...')
            os.system(
                f'nohup bash {WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyStatistics15.sh >> {WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyStatistics15.log 2>&1 &')
        else:
            print("")
            raise Exception("\033[1;36mYou can only select one character from '1/2/3' and cannot enter other characters.\033[0m")
    except Exception as Error:
        print(Error)
        print('\033[1;36mOk, just use the "bash XXX.sh" command directly after checking.\033[m')
    print("")
    print('\033[1;36mThe data you need is already in the corresponding folder. But simple data are obscure.\033[m')
    print('\033[1;36mI can help you display them graphically. Do you need this? \033[m')
    answer = input('\033[1;36mIf necessary, please enter: y/Y/yes/YES; If not, please enter: n/y/no/no. ：\033[m')
    print("")
    try:
        if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'YES':
            if os.path.exists(f'{WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyStatistics15.r'):
                os.system(f'rm {WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyStatistics15.r')
            else:
                pass
            miss_maf_hard_statistics_plot()
            print("")
            print("\033[1;31mR script is written, do you want to execute it directly? \033[m")
            youranswer = input("\033[1;31mIf it needs to be executed immediately, please enter: 1; If you don't want to execute it immediately, please enter: 2. :\033[m")
            if youranswer == '1':
                print("")
                print("\033[1;36mStart drawing, please wait a moment...\033[m")
                os.system(f"Rscript {WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyStatistics15.r")
                print(f"\033[1;36mThe drawing has been completed, please go to the '{WorkPath}/WorkFile/MissMafHardyFiltering11/miss_maf_hardy.pdf' file to view it.\033[m")
                print("\033[1;36mIt will be an important sentence for you to set the 'miss_maf_hardy_filtering' filter parameters in the next step.\033[m")
            elif youranswer == '2':
                print("")
                print(f"\033[1;36mThe R script is in the '{WorkPath}/WorkFile/MissMafHardyFiltering11/' directory. You can check it and execute it.\033[m")
        elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'NO':
            pass
        else:
            print("")
            raise Exception("\033[1;36mYou can only select one character from 'y/Y/yes/YES/n/y/no/no' and cannot enter other characters.\033[0m")
    except Exception as Error:
        print(Error)


def miss_maf_hard_statistics_plot():
    with open(f'{WorkPath}/WorkFile/MissMafHardyFiltering11/MissMafHardyStatistics15.r', 'w') as statisticsplot:
        statisticsplot.write(f"vmiss <- read.table('{WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics.vmiss', header = T)\n")
        statisticsplot.write(f"smiss <- read.table('{WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics.smiss', header = T)\n")
        statisticsplot.write(f"maf <- read.table('{WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics.afreq', header = T, as.is = T)\n")
        statisticsplot.write(f"hardy <- read.table('{WorkPath}/WorkFile/MissMafHardyFiltering11/AllSample_statistics.hardy', header = T)\n")
        statisticsplot.write(f"pdf(file = '{WorkPath}/WorkFile/MissMafHardyFiltering11/miss_maf_hardy.pdf', width = 12, height = 3)\n")
        statisticsplot.write("par(mfrow = c(1,4))\n")
        statisticsplot.write("hist(smiss[,5], main = 'IndividualMissingness', xlab = '', col = 'red')\n")
        statisticsplot.write("hist(vmiss[,5], main = 'GeneMissingness', xlab = '', col = 'red')\n")
        statisticsplot.write("hist(maf[,5], main = 'Maf', xlab = '', col = 'red')\n")
        statisticsplot.write("hist(hardy[,10], main = 'Hardy', xlab = '', col = 'red')\n")
        statisticsplot.write("dev.off()\n")


def vcf_to_hapmap_16():
    folder_exist_setup(folder='VcfToHapmap16')
    with open(f'{WorkPath}/WorkFile/VcfToHapmap16/VcfToHapmap16.sh', 'w') as vcf_to_hapmap:
        vcf_to_hapmap.write('#!/bin/bash\n')
        vcf_to_hapmap.write(f"{WorkPath}/Software/Tassel-5-main/run_pipeline.pl -Xms10g -Xmx20g -vcf {WorkPath}/WorkFile/MissMafHardyFiltering11/ALLSample_FinalReasult.vcf -sortPositions -export {WorkPath}/WorkFile/VcfToHapmap16/ALLSample_FinalReasult -exportType HapmapDiploid")
    choose(shell_filepath='VcfToHapmap16')
