#! /usr/bin/python
# _*_ coding: utf-8 _*_
# Author: 29398(赵子权)
# FileName: main.py
# Time: 2023/4/3 20:39   
# Email: zzq@caf.ac.cn
# Software: PyCharm

import KeyFunctions
import os


def welcome():
    print("")
    print("\033[1;31m=================================================\033[0m\033[1;36mWelcome to EasyGWAS!\033[0m\033[1;31m====================================================\033[0m")
    print('\033[1;31m==\033[0m                                                                                                                     \033[1;31m==\033[0m')
    print("\033[1;31m==\033[0m   Following my steps, you can easily complete the operation from\033[1;31m raw resequencing data\033[0m to\033[1;31m Hapmap.txt format file\033[0m.\033[0m   \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m Then you can use GAPIT3 or Tassel software to perform genome-wide association analysis.                             \033[1;31m==\033[0m")
    print('\033[1;31m==\033[0m                                                                                                                     \033[1;31m==\033[0m')
    print("\033[1;31m=========================================================================================================================\033[0m")
    print("")


def main_menu():
    print("")
    print("\033[1;31m=====================================\033[0m\033[0m\033[1;36mMain Menu\033[0m\033[1;31m=====================================\033[0m")
    print("\033[1;31m==\033[0m 0. Exit script                                                                \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 1. Download the necessary software for genome-wide association analysis       \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 2. Filtering the raw resequencing data                                        \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 3. Building reference genome index                                            \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 4. Conversion and sorting of Sam and Bam formats                              \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 5. Removal of duplicates from PCR preference amplification                    \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 6. Building an index of Bam files                                             \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 7. Searching for SNP and INDEL variants                                       \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 8. Conversion of gvcf and vcf file formats                                    \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 9. Splitting SNP and INDEL variants                                           \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 10. Filtering low quality SNP and INDEL                                       \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 11. Merge filtered SNP and INDEL                                              \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 12. Missing rate, minimum allele frequency and Harwin equilibrium filtering   \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 13. FastQC software to check the quality of resequenced data                  \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 14. Check SNP and INDEL data quality                                          \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 15. Missing rate, minimum allele frequency and Harwin equilibrium statistics  \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 16. Vcf format file to Hapmap format file                                     \033[1;31m==\033[0m")
    print("\033[1;31m===================================================================================\033[0m")


welcome()

if os.path.exists('../Software'):
    pass
else:
    os.mkdir('../Software')

if os.path.exists('../WorkFile'):
    pass
else:
    os.mkdir('../WorkFile')


while True:
    main_menu()
    try:
        choose = int(input("\033[1;31mPlease enter the number of the step you wish to perform:\033[0m"))
        if choose == 0:
            print("")
            print("\033[1;36mAre you going to continue using EasyGWAS?(y/Y/yes/YES/n/no/N/NO)\033[0m")
            answer = input("\033[1;31mPlease enter your choice here: \033[0m")
            try:
                if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
                    continue
                elif answer == "n" or answer == "N" or answer == "no" or answer == "NO":
                    print("")
                    print("\033[1;36mThanks for using EasyGWAS and good luck!\033[0m")
                    break
                else:
                    print("")
                    raise Exception("\033[1;36mYou can only select one character from 'y/Y/yes/YES/n/N/no/NO' and cannot enter other characters.\033[0m")
            except Exception as Error:
                print(Error)
        elif choose == 1:
            KeyFunctions.software_download_menu()
        elif choose == 2:
            fq_data_filename = input("\033[1;31mOk, now please tell me the absolute path of your resequencing data. For example: /mnt/e/Python/ (Be sure to pay attention to the last '/'symbol.): \033[0m")
            KeyFunctions.original_quality_control_01(fq_data_filename=fq_data_filename)
            print('')
        elif choose == 3:
            reference_genome = input("\033[1;31mPlease tell me the absolute path to your reference genome (be sure to include the genome file name)：\033[0m")
            KeyFunctions.build_refseq_index_02(reference_genome=reference_genome)
        elif choose == 4:
            KeyFunctions.sam_to_bam_sort_03()
        elif choose == 5:
            KeyFunctions.mark_duplications_04()
        elif choose == 6:
            KeyFunctions.build_bam_index_05()
        elif choose == 7:
            KeyFunctions.haplotypecaller_06()
        elif choose == 8:
            KeyFunctions.gvcf_to_vcf_07()
        elif choose == 9:
            KeyFunctions.split_snp_indel_08()
        elif choose == 10:
            KeyFunctions.hard_filtration_09()
        elif choose == 11:
            KeyFunctions.merge_snp_indel_10()
            KeyFunctions.gvcfmerge()
        elif choose == 12:
            KeyFunctions.miss_maf_hardy_filtering_11()
        elif choose == 13:
            fq_data_filename = input("\033[1;31mOk, now please tell me the absolute path of your resequencing data. For example: /mnt/e/Python/ (Be sure to pay attention to the last '/'symbol.): \033[0m")
            KeyFunctions.check_resequencing_quality_13(fq_data_filename=fq_data_filename)
        elif choose == 14:
            KeyFunctions.check_snp_indel_quality_14()
        elif choose == 15:
            KeyFunctions.miss_maf_hardy_statistics_15()
        elif choose == 16:
            KeyFunctions.vcf_to_hapmap_16()
            print("")
            PATH = KeyFunctions.WorkPath
            print("\033[1;36m===============================================================================\033[0m")
            print("\033[1;36m==\033[0m    \033[1;31m========   ==   ========   ==   ========   ==    ==            ==   \033[0m   \033[1;36m==\033[0m")
            print("\033[1;36m==\033[0m    \033[1;31m==              ==    ==        ==         ==    ==           ===   \033[0m   \033[1;36m==\033[0m")
            print("\033[1;36m==\033[0m    \033[1;31m======     ==   ==    ==   ==   ========   ========      ======   ==\033[0m   \033[1;36m==\033[0m")
            print("\033[1;36m==\033[0m    \033[1;31m==         ==   ==    ==   ==         ==   ==    ==      ======   ==\033[0m   \033[1;36m==\033[0m")
            print("\033[1;36m==\033[0m    \033[1;31m==         ==   ==    ==   ==   ========   ==    ==      ===========\033[0m   \033[1;36m==\033[0m")
            print("\033[1;36m===============================================================================\033[0m")
        else:
            print('\033[1;36mThe number you entered is not a list number.\033[0m')
    except ValueError:
        print("\033[1;36mError! You have not entered a number, please enter a numeric number!\033[0m")
        print("")
    except Exception as error:
        print(f"\033[1;36mAn unknown error occurred, as follows: {error}. Please contact the author to resolve!\033[0m")
        print("")
    else:
        print("")
        print("\033[1;36mAre you going to continue using EasyGWAS?(y/Y/yes/YES/n/no/N/NO)\033[0m")
        answer = input("\033[1;31mPlease enter your choice here: \033[0m")
        try:
            if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
                continue
            elif answer == "n" or answer == "N" or answer == "no" or answer == "NO":
                print("")
                print("\033[1;36mThanks for using EasyGWAS and good luck!\033[0m")
                break
            else:
                print("")
                raise Exception("\033[1;36mYou can only select one character from 'y/Y/yes/YES/n/N/no/NO' and cannot enter other characters.\033[0m")
        except Exception as Error:
            print(Error)
