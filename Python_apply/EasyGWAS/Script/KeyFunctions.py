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
    print('\033[1;36mDownload completed!\033[0m')
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
    print("=====================================================================")
    print("===========================\033[0m\033[1;36mSoftware Menu\033[0m=============================")
    print("")
    print(" 0. Exit download (If not exited, please try several times!)")
    print(" 1. Trimmomatic-0.39")
    print(" 2. Bwa-0.7.17")
    print(" 3. Samtools-1.15.1")
    print(" 4. Gatk-4.4.0.0")
    print(" 5. Picard-3.0.0")
    print(" 6. Plink-2")
    print("")
    print("=====================================================================")


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
            else:
                print("")
                raise Exception("\033[1;36mYou can only select one character from '0/1/2/3/4/5/6' and cannot enter other characters.\033[0m")
        except Exception as Error:
            print(Error)
            print('\033[1;36mAn unknown error has occurred, please contact the author to solve it!\033[m')
        else:
            software_download_menu()


def original_quality_control_01(fq_data_filename, sequencing_mode='PE', threads=8, base_quality_coding_format='-phred33', illuminaclip='TruSeq3-PE.fa:2:30:10:2:true', slidingwindow='4:15', leading=3, trailing=3, minlen=36, headcrop=5):
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
    folder_exist_setup(folder='original_quality_control_01')
    with open(f'{WorkPath}/WorkFile/original_quality_control_01/original_quality_control_01.sh', 'w') as trim:
        trim.write('#!/bin/bash\n')
        for filename in os.listdir(fq_data_filename):
            if '_R1.fq.gz' in filename:
                filename = re.sub('_R1.fq.gz', '', filename)
                trim.write(
                    f'java -jar {WorkPath}/Software/Trimmomatic-0.39-main/trimmomatic-0.39.jar {sequencing_mode} -threads {threads} {base_quality_coding_format} {fq_data_filename}{filename}_R1.fq.gz {fq_data_filename}{filename}_R2.fq.gz -baseout ../WorkFile/original_quality_control_01/{filename}.fq.gz ILLUMINACLIP:../Software/Trimmomatic-0.39-main/adapters/{illuminaclip} SLIDINGWINDOW:{slidingwindow} LEADING:{leading} TRAILING:{trailing} MINLEN:{minlen} HEADCROP:{headcrop}\n')
    choose(shell_filepath='original_quality_control_01')


def build_refseq_index_02(reference_genome):
    """

    :param reference_genome: "参考基因组的绝对路经加文件名"
    """
    folder_exist_setup(folder='build_refseq_index_02')
    os.system(f'cp {reference_genome} {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta')
    os.system(f'rm {WorkPath}/WorkFile/build_refseq_index_02/*.dict')
    with open(f'{WorkPath}/WorkFile/build_refseq_index_02/build_refseq_index_02.sh', 'w') as refseq_index:
        refseq_index.write('#!/bin/bash\n')
        refseq_index.write(f'{WorkPath}/Software/Bwa-0.7.17-main/bwa index -a bwtsw ../WorkFile/build_refseq_index_02/YourReferenceGenome.fasta -p {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta\n')
        refseq_index.write(f'{WorkPath}/Software/Samtools-1.15.1-main/samtools faidx ../WorkFile/build_refseq_index_02/YourReferenceGenome.fasta > {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta.fai\n')
        refseq_index.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar CreateSequenceDictionary -REFERENCE {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta -OUTPUT {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.dict')
    choose(shell_filepath='build_refseq_index_02')


def sam_to_bam_sort_03(threads=8, tmp_dir=f'{WorkPath}/WorkFile/', validation_stringency='SILENT', sort_order='coordinate'):
    """

    :param threads: 线程数
    :param tmp_dir: 提供一个目录，用于放临时文件，完成后会自动删除
    :param validation_stringency: 检验Sam文件的格式正确与否，设置为'SILENT'可提高性能。
    :param sort_order:输出文件的排序方式，默认coordinate（坐标），意思是按照染色体上的顺序排序。
    """
    folder_exist_setup(folder='sam_to_bam_sort_03')
    with open(f'{WorkPath}/WorkFile/sam_to_bam_sort_03/sam_to_bam_sort_03.sh', 'w') as trans_sort:
        trans_sort.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/original_quality_control_01/'):
            if "_1P.fq.gz" in filename:
                filename = re.sub('_1P.fq.gz', '', filename)
                trans_sort.write(f'{WorkPath}/Software/Bwa-0.7.17-main/bwa mem -t {threads} -M -R "@RG\tID:{filename}\tLB:{filename}\tPL:illumina\tPU:{filename}\tSM:{filename}\" {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta {WorkPath}/WorkFile/original_quality_control_01/{filename}_1P.fq.gz {WorkPath}/WorkFile/original_quality_control_01/{filename}_2P.fq.gz > {WorkPath}/WorkFile/sam_to_bam_sort_03/{filename}.sam'+"\n")
                trans_sort.write(f"java -jar {WorkPath}/Software/Picard-3.0.0-main/picard.jar SortSam -TMP_DIR {tmp_dir} -VALIDATION_STRINGENCY {validation_stringency} -INPUT {WorkPath}/WorkFile/sam_to_bam_sort_03/{filename}.sam -OUTPUT {WorkPath}/WorkFile/sam_to_bam_sort_03/{filename}_sort.bam -SORT_ORDER {sort_order}\n")
                trans_sort.write(f'rm {WorkPath}/WorkFile/sam_to_bam_sort_03/{filename}.sam\n')
    os.system(f"sed -i 's/\\t/\\\\t/g' {WorkPath}/WorkFile/sam_to_bam_sort_03/sam_to_bam_sort_03.sh")
    choose(shell_filepath='sam_to_bam_sort_03')


def mark_duplications_04(max_file_handles_for_ends_map=800, remove_duplicates='false', validation_stringency='LENIENT'):
    """

    :param max_file_handles_for_ends_map: 将读取结束溢出到磁盘时保持打开状态的最大文件句柄数。将此数字设置为略低于每个进程可能打开的文件的最大数目。这个数字可以通过在Unix系统上执行“ulimit -n”命令找到
    :param remove_duplicates: 官网是flase。来丢弃duplicated序列。对于是否选择标记或者删除，对结果应该没有什么影响，GATK官方流程里面给出的例子是仅做标记不删除。这里定义的重复序列是这样的：如果两条reads具有相同的长度而且比对到了基因组的同一位置，那么就认为这样的reads是由PCR扩增而来，就会被GATK标记。
    :param validation_stringency: 在BWA 比对生成SAM文件时，将没有map到基因组上的read归到了ref以外的区域，其MAPQ值不为0，而Picard认为这些read是不应该出现的，所以会报错。如果想忽略报错的话，就使用这行代码。
    """
    folder_exist_setup(folder='mark_duplications_04')
    with open(f'{WorkPath}/WorkFile/mark_duplications_04/mark_duplications_04.sh', 'w') as mark_dup:
        mark_dup.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/sam_to_bam_sort_03/'):
            if '_sort.bam' in filename:
                filename = re.sub('.bam', '', filename)
                mark_dup.write(f'java -jar {WorkPath}/Software/Picard-3.0.0-main/picard.jar MarkDuplicates -MAX_FILE_HANDLES_FOR_READ_ENDS_MAP {max_file_handles_for_ends_map} -REMOVE_DUPLICATES {remove_duplicates} -INPUT {WorkPath}/WorkFile/sam_to_bam_sort_03/{filename}.bam -OUTPUT {WorkPath}/WorkFile/mark_duplications_04/{filename}_dedup.bam -METRICS_FILE {WorkPath}/WorkFile/mark_duplications_04/{filename}_dedup.metrics -VALIDATION_STRINGENCY {validation_stringency}\n')
    choose(shell_filepath='mark_duplications_04')


def build_bam_index_05():
    folder_exist_setup(folder='build_bam_index_05')
    with open(f'{WorkPath}/WorkFile/build_bam_index_05/build_bam_index_05.sh', 'w') as bam_index:
        bam_index.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/mark_duplications_04/'):
            if '_sort_dedup.bam' in filename:
                bam_index.write(f'{WorkPath}/Software/Samtools-1.15.1-main/samtools index {WorkPath}/WorkFile/mark_duplications_04/{filename} > {WorkPath}/WorkFile/mark_duplications_04/{filename}.bai\n')
    choose(shell_filepath='build_bam_index_05')


def haplotypecaller_06(lachesis_group='Lachesis_group', chr_number=15):
    folder_exist_setup(folder='haplotypecaller_06')
    with open(f'{WorkPath}/WorkFile/haplotypecaller_06/haplotypecaller_06.sh', 'w') as haplotype:
        haplotype.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/mark_duplications_04'):
            if '.bai' not in filename and '.metrics' not in filename and '_sort_dedup.bam' in filename:
                filename = re.sub('_sort_dedup.bam', '', filename)
                for Lachesis_group in range(1, chr_number+1, 1):
                    haplotype.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar HaplotypeCaller -R {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta -I {WorkPath}/WorkFile/mark_duplications_04/{filename}_sort_dedup.bam -ERC GVCF -L {lachesis_group}{Lachesis_group} -O {WorkPath}/WorkFile/haplotypecaller_06/{filename}_chr{Lachesis_group}.g.vcf\n')
    choose(shell_filepath='haplotypecaller_06')


def gvcf_to_vcf_07(chr_number=15):
    folder_exist_setup(folder='gvcf_to_vcf_07')
    with open(f'{WorkPath}/WorkFile/gvcf_to_vcf_07/gvcf_to_vcf_07.sh', 'w') as gvcftovcf:
        gvcftovcf.write('#!/bin/bash\n')
        for chr_num in range(1, chr_number+1, 1):
            lachesis_group = []
            for filename in os.listdir(f'{WorkPath}/WorkFile/haplotypecaller_06'):
                if '.g.vcf' in filename and '.idx' not in filename and 'chr1' in filename:
                    filename = re.sub('_chr1.g.vcf', '', filename)
                    lachesis_group.append(f'-V {WorkPath}/WorkFile/haplotypecaller_06/{filename}_chr{chr_num}.g.vcf')
            lachesis_group = ' '.join(lachesis_group)
            gvcftovcf.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar CombineGVCFs -R {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta {lachesis_group} -O {WorkPath}/WorkFile/gvcf_to_vcf_07/Chr{chr_num}.g.vcf\n')
            gvcftovcf.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar GenotypeGVCFs -R {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta -V {WorkPath}/WorkFile/gvcf_to_vcf_07/Chr{chr_num}.g.vcf -O {WorkPath}/WorkFile/gvcf_to_vcf_07/Chr{chr_num}.vcf\n')
    choose(shell_filepath='gvcf_to_vcf_07')


def split_snp_indel_08():
    folder_exist_setup(folder='split_snp_indel_08')
    with open(f'{WorkPath}/WorkFile/split_snp_indel_08/split_snp_indel_08.sh', 'w') as splitSnpIndel:
        splitSnpIndel.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/gvcf_to_vcf_07'):
            if '.idx' not in filename and '.g.' not in filename and '.vcf' in filename:
                filename = re.sub('Chr', '', filename)
                filename = re.sub('.vcf', '', filename)
                splitSnpIndel.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar SelectVariants -R {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta -V {WorkPath}/WorkFile/gvcf_to_vcf_07/Chr{filename}.vcf -O {WorkPath}/WorkFile/split_snp_indel_08/Chr{filename}_snp.vcf -L Lachesis_group{filename} --select-type-to-include SNP\n')
                splitSnpIndel.write(f'java -jar {WorkPath}/Software/Gatk-4.4.0.0-main/gatk-package-4.4.0.0-local.jar SelectVariants -R {WorkPath}/WorkFile/build_refseq_index_02/YourReferenceGenome.fasta -V {WorkPath}/WorkFile/gvcf_to_vcf_07/Chr{filename}.vcf -O {WorkPath}/WorkFile/split_snp_indel_08/Chr{filename}_indel.vcf -L Lachesis_group{filename} --select-type-to-include INDEL\n')
    choose(shell_filepath='split_snp_indel_08')


def hard_filtration_09():
    pass


def merge_snp_indel_10():
    pass


def miss_maf_hardy_filtering_11():
    pass