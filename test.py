#! /usr/bin/python3
# coding=utf-8
# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com

# import requests
# import wget
#
# #url = 'https://codeload.github.com/ziquanzhao/seqtk/zip/refs/heads/main'
#
# url = "https://ppt.pptsupermarket.com/Data/PPT/2022/12_28/72c5bf11-d7f2-4c33-ac46-55661306d24a.pptx"
#
# # r = requests.get(url, allow_redirects=True)
# #
# # with open('r.txt', 'wb') as f:
# #     f.write(r)
#
# wget.download(url, out="./GWAS/A.pptx")

while True:
    print("")
    print("\033[1;36mIf you want to read, enter: y/Y/yes/YES ; if you don't want to read, enter: n/N/no/NO, skip this step \033[0m")
    answer = input("\033[1;31mPlease enter your choice here: \033[0m")
    try:
        if answer == "y" or answer == "Y" or answer == "yes" or answer == "YES":
            with open('./Description_document.txt', "r", encoding="utf-8") as description:
                for i in description.readlines():
                    print(i, end="")
                print("\n")
                print("\033[1;36mOkay, congratulations! you have read the documentation. Follow the main menu prompts below to carry out your research.\033[0m")
                break
        elif answer == "n" or answer == "N" or answer == "no" or answer == "NO":
            break
        else:
            print("")
            raise Exception("\033[1;36mYou can only select one character from 'y/Y/yes/YES/n/N/no/NO' and cannot enter other characters\033[0m")
    except FileNotFoundError:
        print("")
        print("\033[1;36mCheck carefully, have you deleted or renamed Description_document.txt file in yourpath/EasyGWAS/script/ folder?\033[0m")
        print("\033[1;36mThe program currently cannot find the Description_document.txt file in yourpath/EasyGWAS/script/ folder.\033[0m")
    except Exception as Error:
        print(Error)
