#! /usr/bin/python
# _*_ coding: utf-8 _*_
# Author: 29398(赵子权)
# FileName: main.py
# Time: 2023/4/3 20:39   
# Email: zzq@caf.ac.cn
# Software: PyCharm

import KeyFunctions


def welcome():
    print("")
    print("\033[1;34m=====================================================================================================================\033[0m")
    print(
        "\033[1;37m===============================================\033[0m\033[1;36mWelcome to EasyGWAS!\033[0m\033[0;37m==================================================\033[0m")
    print("")
    print(
        "   Following my steps, you can easily complete the operation from\033[1;31m raw resequencing data\033[0m to\033[1;31m Hapmap.txt format file\033[0m.\033[0m")
    print(" Then you can use GAPIT3 or Tassel software to perform genome-wide association analysis.")
    print("")
    print("\033[1;34m=====================================================================================================================\033[0m")
    print("")


def main_menu():
    print("")
    print("\033[1;34m===============================================================================\033[0m")
    print("\033[1;37m===================================\033[0m\033[1;36mMain Menu\033[0m\033[1;37m===================================\033[0m")
    print("")
    print(" \033[1;31m0.\033[0m Exit script")
    print(" \033[1;31m1.\033[0m Download the necessary software for genome-wide association analysis")
    print(" \033[1;31m2.\033[0m Filtering the raw resequencing data")
    print(" \033[1;31m3.\033[0m Building reference genome index")
    print(" \033[1;31m4.\033[0m Conversion and sorting of Sam and Bam formats")
    print(" \033[1;31m5.\033[0m Removal of duplicates from PCR preference amplification")
    print(" \033[1;31m6.\033[0m Building an index of Bam files")
    print(" \033[1;31m7.\033[0m Searching for SNP and INDEL variants")
    print(" \033[1;31m8.\033[0m Conversion of gvcf and vcf file formats")
    print(" \033[1;31m9.\033[0m Splitting SNP and INDEL variants")
    print(" \033[1;31m10.\033[0m Filtering low quality SNP and INDEL")
    print(" \033[1;31m11.\033[0m Merge filtered SNP and INDEL")
    print(" \033[1;31m12.\033[0m Missing rate, minimum allele frequency and Harwin equilibrium filtering")
    print("")
    print("\033[1;34m===============================================================================\033[0m")
    print("")


welcome()

print("\033[1;36mOkay, guys, let's get started!\033[0m")
print(
    "\033[1;36mIf you know your enemy, you will never lose. I have a detailed description of how to use the software, you need to read it carefully before you use it!\033[0m")

while True:
    print("")
    print("\033[1;36mIf you want to read, enter: y/Y/yes/YES ; if you don't want to read, enter: n/N/no/NO, skip this step. \033[0m")
    answer = input("\033[1;31mPlease enter your choice here: \033[0m")
    print("")
    try:
        if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
            with open('../DescriptionDocument/MainDescription.txt', "r", encoding="utf-8") as description:
                for i in description.readlines():
                    print(i, end="")
                print("\n")
                print("\033[1;36mOkay, congratulations! you have read the documentation. Follow the main menu prompts below to carry out your research!\033[0m")
                break
        elif answer == "n" or answer == "N" or answer == "no" or answer == "NO":
            break
        else:
            print("")
            raise Exception("\033[1;36mYou can only select one character from 'y/Y/yes/YES/n/N/no/NO' and cannot enter other characters.\033[0m")
    except FileNotFoundError:
        print("")
        print("\033[1;36mCheck carefully, have you deleted or renamed Description_document.txt file in yourpath/EasyGWAS/script/ folder?\033[0m")
        print("\033[1;36mThe program currently cannot find the Description_document.txt file in yourpath/EasyGWAS/script/ folder.\033[0m")
    except Exception as Error:
        print(Error)

main_menu()

while True:
    try:
        choose = int(input("\033[1;31mPlease enter the number of the step you wish to perform:\033[0m"))
        if choose == 0:
            print("")
            print("\033[1;36mThanks for using EasyGWAS and good luck!\033[0m")
        elif choose == 1:
            KeyFunctions.assistant_menu()
        elif choose == 2:
            KeyFunctions.original_quality_control_01()
        elif choose == 3:
            KeyFunctions.build_refseq_index_02()
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
        elif choose == 12:
            KeyFunctions.miss_maf_hardy_filtering_11()
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
