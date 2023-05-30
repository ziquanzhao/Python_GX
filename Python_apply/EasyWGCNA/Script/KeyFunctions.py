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
    print("\033[1;31m==\033[0m 0. Exit download (If not exited, please try several times!)     \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 1. Fastqc-0.12.1                                                \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 2. Trimmomatic-0.39                                             \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 3. Hisat2-2.2.1                                                 \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 4. Samtools-1.15.1                                              \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 5. FeatureCounts-2.0.3                                          \033[1;31m==\033[0m")
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
                if os.path.exists(f'{WorkPath}/Software/Fastqc-0.12.1-main'):
                    print("\033[1;31mThe 'Fastqc-0.12.1-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Fastqc-0.12.1' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Fastqc-0.12.1' software is not installed, please delete the 'Fastqc-0.12.1-main' folder and the 'Fastqc-0.12.1.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_01 = 'https://codeload.github.com/ziquanzhao/Fastqc-0.12.1/zip/refs/heads/main'
                    download_software(url=your_url_01, software_name='Fastqc-0.12.1')
            elif answer == '2':
                if os.path.exists(f'{WorkPath}/Software/Trimmomatic-0.39-main'):
                    print("\033[1;31mThe 'Trimmomatic-0.39-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Trimmomatic-0.39' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Trimmomatic-0.39' software is not installed, please delete the 'Trimmomatic-0.39-main' folder and the 'Trimmomatic-0.39.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_02 = 'https://codeload.github.com/ziquanzhao/Trimmomatic/zip/refs/heads/main'
                    download_software(url=your_url_02, software_name='Trimmomatic-0.39')
            elif answer == '3':
                if os.path.exists(f'{WorkPath}/Software/Hisat2-2.2.1-main'):
                    print("\033[1;31mThe 'Hisat2-2.2.1-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Hisat2-2.2.1' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Hisat2-2.2.1' software is not installed, please delete the 'Hisat2-2.2.1-main' folder and the 'Hisat2-2.2.1.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_03 = 'https://codeload.github.com/ziquanzhao/Hisat2-2.2.1/zip/refs/heads/main'
                    download_software(url=your_url_03, software_name='Hisat2-2.2.1')
            elif answer == '4':
                if os.path.exists(f'{WorkPath}/Software/Samtools-1.15.1-main'):
                    print("\033[1;31mThe 'Samtools-1.15.1-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'Samtools-1.15.1' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'Samtools-1.15.1' software is not installed, please delete the 'Samtools-1.15.1-main' folder and the 'Samtools-1.15.1.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_04 = 'https://codeload.github.com/ziquanzhao/Samtools-1.15.1/zip/refs/heads/main'
                    download_software(url=your_url_04, software_name='Samtools-1.15.1')
            elif answer == '5':
                if os.path.exists(f'{WorkPath}/Software/FeatureCounts-2.0.3-main'):
                    print("\033[1;31mThe 'FeatureCounts-2.0.3-main' folder already exists in the 'Workfile' directory. I think you have successfully installed the 'FeatureCounts-2.0.3' software, so this step is skipped.\033[0m")
                    print("\033[1;31mIf you are sure that 'FeatureCounts-2.0.3' software is not installed, please delete the 'FeatureCounts-2.0.3-main' folder and the 'FeatureCounts-2.0.3.zip' compressed package and perform this step again.\033[0m")
                    pass
                else:
                    your_url_05 = 'https://codeload.github.com/ziquanzhao/FeatureCounts-2.0.3/zip/refs/heads/main'
                    download_software(url=your_url_05, software_name='FeatureCounts-2.0.3')
            else:
                print("")
                raise Exception("\033[1;36mYou can only select one character from '0/1/2/3/4/5' and cannot enter other characters.\033[0m")
        except Exception as Error:
            print(Error)
            print('\033[1;36mAn unknown error has occurred, please contact the author to solve it!\033[m')
        else:
            software_download_menu()


def check_transcriptome_quality_1(fq_data_filename, threads=8):
    """

    :param threads: 线程数
    :param fq_data_filename:转录组数据的绝对路径，注意符合命名规范。XXX_R1.fq.gz和XXX_R2.fq.gz
    -o --outdir FastQC生成的报告文件的储存路径
    --extract 结果文件解压缩
    --noextract 结果文件压缩
    -t --threads 选择程序运行的线程数，每个线程会占用250MB内存，越多越快咯
    -c --contaminants 污染物选项，输入的是一个文件，格式是Name [Tab] Sequence，里面是可能的污染序列，如果有这个选项，FastQC会在计算时候评估污染的情况，并在统计的时候进行分析，一般用不到
    -a --adapters 也是输入一个文件，文件的格式Name [Tab] Sequence，储存的是测序的adpater序列信息，如果不输入，目前版本的FastQC就按照通用引物来评估序列时候有adapter的残留
    -q --quiet 安静运行模式，一般不选这个选项的时候，程序会实时报告运行的状况。
    """
    folder_exist_setup(folder='check_transcriptome_quality_1')
    with open(f'{WorkPath}/WorkFile/check_transcriptome_quality_1/check_transcriptome_quality_1.sh', 'w') as check_trans_quality:
        check_trans_quality.write('#!/bin/bash\n')
        for filename in os.listdir(fq_data_filename):
            if '_R1.fq.gz' in filename:
                filename = re.sub('_R1.fq.gz', '', filename)
                check_trans_quality.write(f'{WorkPath}/Software/Fastqc-0.12.1-main/fastqc  -t {threads} {fq_data_filename}{filename}_R1.fq.gz {fq_data_filename}{filename}_R2.fq.gz -o {WorkPath}/WorkFile/check_transcriptome_quality_1/\n')
    choose(shell_filepath='check_transcriptome_quality_1')
    print('\033[1;31mPlease carefully review the results, which will be an important basis for parameter setting of raw data filtering in the next step!\033[m')
    print("\033[1;31mIt's very important, please take it seriously!\033[m")


def original_quality_control_2(fq_data_filename, sequencing_mode='PE', threads=8, base_quality_coding_format='-phred33', illuminaclip='TruSeq3-PE.fa:2:30:10:2:true', slidingwindow='4:15', leading=3, trailing=3, minlen=36, headcrop=5):
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
    folder_exist_setup(folder='original_quality_control_2')
    with open(f'{WorkPath}/WorkFile/original_quality_control_2/original_quality_control_2.sh', 'w') as trim:
        trim.write('#!/bin/bash\n')
        for filename in os.listdir(fq_data_filename):
            if '_R1.fq.gz' in filename:
                filename = re.sub('_R1.fq.gz', '', filename)
                trim.write(
                    f'java -jar {WorkPath}/Software/Trimmomatic-0.39-main/trimmomatic-0.39.jar {sequencing_mode} -threads {threads} {base_quality_coding_format} {fq_data_filename}{filename}_R1.fq.gz {fq_data_filename}{filename}_R2.fq.gz -baseout {WorkPath}/WorkFile/original_quality_control_2/{filename}.fq.gz ILLUMINACLIP:{WorkPath}/Software/Trimmomatic-0.39-main/adapters/{illuminaclip} SLIDINGWINDOW:{slidingwindow} LEADING:{leading} TRAILING:{trailing} MINLEN:{minlen} HEADCROP:{headcrop}\n')
    choose(shell_filepath='original_quality_control_2')


def build_refseq_index_3(reference_genome, threads=8):
    """

    :param threads:线程数
    :param reference_genome: "参考基因组的绝对路经加文件名"
    """
    folder_exist_setup(folder='build_refseq_index_3')
    os.system(f'cp {reference_genome} {WorkPath}/WorkFile/build_refseq_index_3/YourReferenceGenome.fasta')
    with open(f'{WorkPath}/WorkFile/build_refseq_index_3/build_refseq_index_3.sh', 'w') as refseq_index:
        refseq_index.write('#!/bin/bash\n')
        refseq_index.write(f'{WorkPath}/Software/Hisat2-2.2.1-main/hisat2-build -p {threads} {WorkPath}/WorkFile/build_refseq_index_3/YourReferenceGenome.fasta {WorkPath}/WorkFile/build_refseq_index_3/YourHisat2Refseq\n')
    choose(shell_filepath='build_refseq_index_3')


def hisat2_mapping_refseq_4(threads=8):
    folder_exist_setup(folder='hisat2_mapping_refseq_4')
    with open(f'{WorkPath}/WorkFile/hisat2_mapping_refseq_4/hisat2_mapping_refseq_4.sh', 'w') as mapping:
        mapping.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/original_quality_control_2/'):
            if "_1P.fq.gz" in filename:
                filename = re.sub('_1P.fq.gz', '', filename)
                mapping.write(f'{WorkPath}/Software/Hisat2-2.2.1-main/hisat2 -p {threads} -x {WorkPath}/WorkFile/build_refseq_index_3/YourHisat2Refseq -1 {WorkPath}/WorkFile/original_quality_control_2/{filename}_1P.fq.gz -2 {WorkPath}/WorkFile/original_quality_control_2/{filename}_2P.fq.gz -S {WorkPath}/WorkFile/hisat2_mapping_refseq_4/{filename}.sam\n')
                mapping.write(f'{WorkPath}/Software/Samtools-1.15.1-main/samtools view -@ {threads} -bhS {WorkPath}/WorkFile/hisat2_mapping_refseq_4/{filename}.sam -o {WorkPath}/WorkFile/hisat2_mapping_refseq_4/{filename}.bam\n')
                mapping.write(f'{WorkPath}/Software/Samtools-1.15.1-main/samtools sort -@ {threads} -m 10G {WorkPath}/WorkFile/hisat2_mapping_refseq_4/{filename}.bam -o {WorkPath}/WorkFile/hisat2_mapping_refseq_4/{filename}_final.bam\n')
                mapping.write(f'rm {WorkPath}/WorkFile/hisat2_mapping_refseq_4/{filename}.sam {WorkPath}/WorkFile/hisat2_mapping_refseq_4/{filename}.bam\n')
    choose(shell_filepath='hisat2_mapping_refseq_4')


def gene_expression_quantification_5(gtf_file_path, threads=8):
    """

    input_files (files)：包含read mapping结果的read文件名称，程序会自动检测文件格式(SAM或BAM)，可同时提供多个文件。
    -a <string>：注释文件的名称，支持Gzipped文件格式
    -A (chrAliases)：染色体名称别名文件，使注释中的chr名称与read中的名称相匹配。这是一个两列逗号分隔的文本文件，第一列为注释中的chr名称，第二列为read中的chr名称。Chr名称区分大小写，文件中不应包含任何列标题。
    -B：如果指定，则只考虑两端成功对齐的片段进行summarization。此选项仅适用于fragments count(read pairs)
    -C：如果指定，chimeric fragments(那些两端与不同染色体对齐的片段)将不被计算在内。此选项仅适用于fragments count (read pairs)
    -d <int>：最小fragment/template长度，默认值50
    -D：最大fragment/template长度，默认值600
    -f：如果指定，将在feature水平(例如外显子)执行read summarization，否则在meta-feature水平(例如基因)上进行。
    -F：指定注释文件的格式。可接受的格式包括GTF和SAF。默认情况下，C版本的featureCounts程序接受GTF格式注释，R版本接受SAF格式注释。
    -g <string>：指定在提供GTF注释时用于将feature(例如外显子)分组为meta-feature(例如基因)的属性类型。默认为gene-id。这种属性类型通常是基因标识符。该参数对于meta-feature水平的summarization非常有用。
    -G <string>：提供FASTA格式文件的名称，该文件包含生成所提供的SAM/BAM文件的read映射中使用的参考序列。该可选参数可以与-J一起使用，以提高连接(junctions)的read count。
    -J：计算支持每个exon-exon junction的reads数量。将从输入数据中包括的所有exon-spanning reads(在CIGAR字符串中包含"N")中识别junction(注意，该参数不考虑选项-splitOnly和-nonSplitOnly)。输出结果包括与junction的两个剪接位点中的至少一个重叠的primary和secondary基因的名称。只有一个primary基因被报道，但可能有不止一个secondary基因被报道。secondary基因与primary基因重叠的剪接位点并不多。当primary基因和secondary基因重叠相同数量的剪接位点时，选择最左边碱基位置最小的基因作为primary基因。输出结果中还包括接头的左剪接位置(Site1)和右剪接位置(Site2)的位置信息。其中包括染色体名称、坐标和剪接位点的链。在输出的最后一列中，为每个库的每个junction提供了支持reads的数量。
    -L：打开long-read count模式。此选项应用于count long-read，如Nanopore或PacBio reads。
    -M：如果指定，将对多重映射read/fragment进行count，使用"NH"标记来查找多重映射read。
    -o：输出文件的名称。输出文件包含分配给每个meta-feature(如果指定了-f，则为每个feature)的read count。注意，Rsubrad中的featureCounts函数不使用此参数。它返回一个列表对象，包括read的摘要结果和其他数据。
    -O：如果指定，read/fragment将被允许分配给多个匹配的meta-feature(如果指定-f，则为feature)。与多个meta-feature/feature重叠的read/fragment将被count多次。注意，在执行meta-feature水平summarization时，如果read/fragment与同一meta-feature内的多个feature重叠(只要它不与其他meta-feature重叠)，则它仍将被count一次。
    -p：指定输入数据包含paired-end reads。如果输入read的类型（单端或成对端）与指定的类型不同，featureCounts将终止。要计算paired-end reads的fragment(而不是read)，还应指定--countReadPairs参数。
    -P：如果指定，将fragment分配给meta-feature或feature时，将检查fragment长度。此选项仅适用于fragment count。应该使用-d和-D选项指定fragment长度阈值。
    -Q <int>：读取必须满足的最小映射质量分数才能count。对于paired-end reads，至少有一个末端应满足此标准。0为默认值。
    -R <string>：输出每个read的详细read分配结果(如果是paired end，则输出fragment)。详细的分配结果可以保存为三种不同的格式，包括CORE、SAM和BAM(注意，这些值区分大小写)。当指定CORE格式时，将为每个输入文件生成一个制表符分隔的文件。每个生成文件的名称是添加了".featureCounts"后缀。每个生成文件包含四列，包括read名称、状态(已分配或未分配原因）、target数量和target列表。target是一个feature或meta-feature。target列表中的项目用逗号分隔。如果未分配read，则其target数将设置为-1。当指定SAM或BAM格式时，详细的分配结果将保存到SAM和BAM格式文件中。生成文件的名称是添加了".featureCounts.sam"或".featureCount.bam"后缀。三个标记用于描述read分配结果：XS、XN和XT。XS给出分配状态。XN给出了target数量。XT给出逗号分隔的target列表。
    -s <intorstring>：链特异性参数。应提供单个整数值(应用于所有输入文件)或逗号分隔的值字符串(应用于每个对应的输入文件)。可能的值包括：0(un-stranded，默认值)、1(stranded)和2(reversely stranded)。对于paired-end reads，第一次读取的链被视为整个片段的链。FLAG字段用于判断read是一对中的first read还是second read。
    -t <string>：指定feature类型。如果提供了多个feature类型，则应使用","(无空格)分隔。只有在所提供的GTF注释文件中具有匹配feature类型的行才会被包括在内进行read count，默认"exon"。
    -T <int>：运行线程数，1~32，默认1
    -v：输出程序版本
    −−byReadGroup：按read分组count read。read分组在BAM/SAM输入文件的表头中标识，生成的count表将包括每个库中每个组的counts。
    −−countReadPairs：reads对将被计数，而不是reads。该参数仅适用于paired-end数据。
    −−donotsort：如果指定，即使在输入中发现来自同一对的reads不相邻，paired-end reads也不会重新排序。
    −−extraAttributes <string>：从提供的GTF注释中提取额外的属性类型，并将它们包含在count输出中。这些属性类型将不会用于对features进行分组。如果提供了多个属性类型，则应使用逗号分隔(在Rsubread featureCounts中为字符向量)。
    −−fraction：为features指定分数counts。此选项必须与-M或-O或两者同时使用。当指定-M时，多重映射read(通过"NH"标记识别)中报告的每个alignment的count为1/x，而不是1，其中x是针对相同read报告的alignment总数。当指定-O时，每个重叠的features的count为1/y，其中y是与read重叠的features总数。当同时指定-M和-O时，每个alignment的count为1/(x*y)。
    −−fracOverlap <float>：read assignment所需的read中重叠碱基的最小分数。范围是0(默认值)到1。若是paired-end，则从两个read中计算重叠碱基的数量。计算总read长度时会计算Soft-clipped碱基(但在计算重叠碱基时会忽略)。read assignment需要同时满足该选项和–minOverlap选项。
    −−fracOverlapFeature <float>：与read或read对重叠所需的features中包含的碱基的最小分数。范围是0(默认值)到1。
    −−ignoreDup：如果指定，则将忽略标记为重复的read。SAM/BAM文件的FLAG字段中的bit Ox400用于识别重复read。在paired-end数据中，如果发现至少有一个末端是重复read，则将忽略整个read对。
    −−largestOverlap：如果指定，reads/fragments将分配给具有最大数量重叠碱基的target。
    −−maxMOp <int>：指定CIGAR字符串中允许的最大M操作数(匹配或不匹配)。默认值为10。X和=操作都被视为M，相邻的M操作被合并到CIGAR字符串中。当M操作的数量超过限制时，read分配中将只使用第一个maxMOp数量的M操作。
    −−minOverlap <int>：read assignment所需的read中重叠碱基的最小数目。默认值为1。
    −−nonOverlap <int>：分配给feature时，read/read pair中允许的最大非重叠碱基数，默认不限制。
    −−nonOverlapFeature <int>：read assignment中允许的feature中的最大非重叠碱基数，默认不限制。
    −−nonSplitOnly：如果指定，则仅对non-split alignments(CIGAR字符串不包含N)进行count，所有其他alignments将被忽略。
    −−primary：如果指定，则仅对primary alignments进行count。使用SAM/BAM文件的Flag字段中的bit 0x100来标识primary/secondary alignments。数据集中的所有primary alignments都将被count，无论它们是否来自多重映射read(即忽略-M)。
    −−read2pos <int>：
    −−readExtension3 <int>：
    −−readExtension5 <int>：
    −−readShiftSize <int>：read按<int>碱基数移位，默认值0，不允许使用负值。
    −−readShiftType <int>：指定read偏移的方向，可能取值包括upstream(默认)、downstream、left和right。
    −−Rpath <string>：指定一个目录以保存详细的assignment结果。如果未指定，则使用保存count结果的目录。
    −−splitOnly：如果指定，则只对split alignments进行count(CIGAR字符串包含N)。所有其他alignments都将被忽略。
    −−tmpDir <string>：保存中间文件(稍后删除)的目录。默认中间文件保存到-o参数中指定的目录(在R中默认中间文件保存到当前工作目录)。
    −−verbose：输出详细的调试信息，例如read和注释之间不匹配的染色体/contigs。
    :param gtf_file_path:
    :param threads:
    """
    folder_exist_setup(folder='gene_expression_quantification_5')
    os.system(f'cp {gtf_file_path} {WorkPath}/WorkFile/gene_expression_quantification_5/YourReferenceGenomeGTF.gtf')
    with open(f'{WorkPath}/WorkFile/gene_expression_quantification_5/gene_expression_quantification_5.sh', 'w') as quantification:
        quantification.write('#!/bin/bash\n')
        for filename in os.listdir(f'{WorkPath}/WorkFile/hisat2_mapping_refseq_4/'):
            if '_final.bam' in filename:
                filename = re.sub('_final.bam', '', filename)
                quantification.write(f'{WorkPath}/Software/FeatureCounts-2.0.3-main/bin/featureCounts -a {WorkPath}/WorkFile/gene_expression_quantification_5/YourReferenceGenomeGTF.gtf -T {threads} -p --countReadPairs -g gene_id -t exon -o {WorkPath}/WorkFile/gene_expression_quantification_5/{filename}.txt {WorkPath}/WorkFile/hisat2_mapping_refseq_4/{filename}_final.bam\n')
                quantification.write(f'cat {WorkPath}/WorkFile/gene_expression_quantification_5/{filename}.txt | cut -f 1,7 > {WorkPath}/WorkFile/gene_expression_quantification_5/{filename}.count\n')
    choose(shell_filepath='gene_expression_quantification_5')


def countstable_6():
    folder_exist_setup(folder='countstable_6')
    with open(f'{WorkPath}/WorkFile/countstable_6/countstable_6.sh', 'w') as counts:
        counts.write('#!/bin/bash\n')
        countID = []
        countsNUM = 0
        for countfilename in os.listdir(f'{WorkPath}/WorkFile/gene_expression_quantification_5/'):
            if '.count' in countfilename:
                countID.append(f'{WorkPath}/WorkFile/gene_expression_quantification_5/{countfilename}')
                countsNUM = countsNUM + 1
        countID = ' '.join(countID)
        counts.write(f'paste {countID} > {WorkPath}/WorkFile/countstable_6/final_countstable\n')
        counts.write(f"sed -i '/#/d' {WorkPath}/WorkFile/countstable_6/final_countstable\n")
        counts.write(f"sed -i 's#/mnt/e/Python/Python_apply/EasyWGCNA/WorkFile/hisat2_mapping_refseq_4/##g' {WorkPath}/WorkFile/countstable_6/final_countstable\n")
        counts.write(f"sed -i 's/_final.bam//g' {WorkPath}/WorkFile/countstable_6/final_countstable\n")
        delete_column = []
        for i in range(1, countsNUM, 1):
            i = i*2+1
            delete_column.append(f'${i}="";')
        delete_column = ''.join(delete_column)
        delete_column = "{"f'{delete_column}print $0'"}"
        counts.write(f"awk \'{delete_column}\' {WorkPath}/WorkFile/countstable_6/final_countstable > {WorkPath}/WorkFile/countstable_6/YourFinalCounts.txt")
    choose(shell_filepath='countstable_6')

def TPM_FPKM_calculate_7():
    folder_exist_setup(folder='TPM_FPKM_calculate_7')
    with open(f'{WorkPath}/WorkFile/TPM_FPKM_calculate_7/TPM_FPKM_calculate_7.sh', 'w') as tpm_fpkm:
        tpm_fpkm.write('#!/bin/bash\n')
        tpm_fpkm.write(f'cp {WorkPath}/WorkFile/countstable_6/YourFinalCounts.txt {WorkPath}/Script/\n')
        tpm_fpkm.write(f'Rscript {WorkPath}/Script/TPM_FPKM.R\n')
        tpm_fpkm.write(f'rm {WorkPath}/Script/YourFinalCounts.txt\n')
        tpm_fpkm.write(f'mv {WorkPath}/Script/YourFinalFPKM.xls {WorkPath}/Script/YourFinalTPM.xls {WorkPath}/WorkFile/TPM_FPKM_calculate_7/')
    choose(shell_filepath='TPM_FPKM_calculate_7')