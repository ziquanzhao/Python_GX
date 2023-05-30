#! /usr/bin/python
# _*_ coding: utf-8 _*_
# Author: 29398(赵子权)
# FileName: main.py
# Time: 2023/5/30 8:47   
# Email: zzq@caf.ac.cn
# Software: PyCharm

import KeyFunctions
import os


def welcome():
    print("")
    print("\033[1;31m=================================================\033[0m\033[1;36mWelcome to EasyWGCNA!\033[0m\033[1;31m====================================================\033[0m")
    print('\033[1;31m==\033[0m                                                                                                                      \033[1;31m==\033[0m')
    print("\033[1;31m==\033[0m   Following my steps, you can easily complete the operation from\033[1;31m transcriptome data\033[0m to\033[1;31m gene expression\033[0m.\033[0m              \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m Then you can further analyze WGCNA in R.                                                                             \033[1;31m==\033[0m")
    print('\033[1;31m==\033[0m                                                                                                                      \033[1;31m==\033[0m')
    print("\033[1;31m==========================================================================================================================\033[0m")
    print("")
    print("\033[1;36mOkay, guys, let's get started!\033[0m")
    print("\033[1;36mIf you know your enemy, you will never lose. I have a detailed description of how to use the software, you need to read it carefully before you use it!\033[0m")


def main_menu():
    print("")
    print("\033[1;31m=====================================\033[0m\033[0m\033[1;36mMain Menu\033[0m\033[1;31m=====================================\033[0m")
    print("\033[1;31m==\033[0m 0. Exit script                                                                \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 1. Download the necessary software for genome-wide association analysis       \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 2. Check transcriptome quality                                                \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 3. Original quality control                                                   \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 4. Build_refseq_index                                                         \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 5. Hisat2 mapping refseq                                                      \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 6. Gene expression quantification                                             \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 7. Countstable                                                                \033[1;31m==\033[0m")
    print("\033[1;31m==\033[0m 8. TPM_FPKM_calculate                                                         \033[1;31m==\033[0m")
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
    print("\033[1;36mIf you want to read, enter: y/Y/yes/YES ; if you don't want to read, enter: n/N/no/NO, skip this step. \033[0m")
    answer = input("\033[1;31mPlease enter your choice here: \033[0m")
    print("")
    try:
        if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
            print('')
            print('')
            print('\033[1;31m====================================================\033[0m\033[1;36mDescriptionDocument\033[0m\033[1;31m===========================================================\033[0m')
            print('\033[1;31m==\033[0m  1.Please install Java (version 17 and above), python (version 3.7 and above), R (version 4.0 and above) before use.         \033[1;31m==\033[0m')
            print('\033[1;31m==\033[0m  2.This program needs to download software from Github and Google Cloud Disk. Go online scientifically.                      \033[1;31m==\033[0m')
            print('\033[1;31m==\033[0m  3.Prepare your reference genome and GTF format annotation file, and ensure that the chromosome representation of genome     \033[1;31m==\033[0m')
            print('\033[1;31m==\033[0m     file and annotation file is uniform.                                                                                     \033[1;31m==\033[0m')
            print('\033[1;31m==================================================================================================================================\033[0m')
            print("\033[1;36mOkay, congratulations! you have read the documentation. Follow the main menu prompts below to carry out your research!\033[0m")
            print('')
            print('')
            break
        elif answer == "n" or answer == "N" or answer == "no" or answer == "NO":
            break
        else:
            print("")
            raise Exception("\033[1;36mYou can only select one character from 'y/Y/yes/YES/n/N/no/NO' and cannot enter other characters.\033[0m")
    except FileNotFoundError:
        print("")
        print(f"\033[1;36mCheck carefully, have you deleted or renamed Description_document.txt file in yourpath/EasyGWAS/DescriptionDocument/ folder?\033[0m")
        print(f"\033[1;36mThe program currently cannot find the Description_document.txt file in yourpath/EasyGWAS/DescriptionDocument/ folder.\033[0m")
    except Exception as Error:
        print(Error)


while True:
    main_menu()
    try:
        choose = int(input("\033[1;31mPlease enter the number of the step you wish to perform:\033[0m"))
        if choose == 0:
            print("")
            print("\033[1;36mAre you going to continue using EasyWGCNA?(y/Y/yes/YES/n/no/N/NO)\033[0m")
            answer = input("\033[1;31mPlease enter your choice here: \033[0m")
            try:
                if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
                    continue
                elif answer == "n" or answer == "N" or answer == "no" or answer == "NO":
                    print("")
                    print("\033[1;36mThanks for using EasyWGCNA and good luck!\033[0m")
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
            KeyFunctions.check_transcriptome_quality_1(fq_data_filename=fq_data_filename)
        elif choose == 3:
            fq_data_filename = input("\033[1;31mOk, now please tell me the absolute path of your resequencing data. For example: /mnt/e/Python/ (Be sure to pay attention to the last '/'symbol.): \033[0m")
            KeyFunctions.original_quality_control_2(fq_data_filename=fq_data_filename)
            print('')
        elif choose == 4:
            reference_genome = input("\033[1;31mPlease tell me the absolute path to your reference genome (be sure to include the genome file name)：\033[0m")
            KeyFunctions.build_refseq_index_3(reference_genome=reference_genome)
            print('')
        elif choose == 5:
            KeyFunctions.hisat2_mapping_refseq_4()
            print('')
        elif choose == 6:
            gtf_file = input("\033[1;31mPlease tell me the absolute path to your GTF file (be sure to include the genome file name)：\033[0m")
            KeyFunctions.gene_expression_quantification_5(gtf_file_path=gtf_file)
            print("")
        elif choose == 7:
            KeyFunctions.countstable_6()
            print('')
        elif choose == 8:
            KeyFunctions.TPM_FPKM_calculate_7()
            print('')
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
        print("\033[1;36mAre you going to continue using EasyWGCNA?(y/Y/yes/YES/n/no/N/NO)\033[0m")
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