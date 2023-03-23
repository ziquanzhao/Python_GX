#! /usr/bin/python
# _*_ coding: utf-8 _*_
# Author: 29398(赵子权)
# FileName: AllDefineClass.py
# Time: 2023/4/3 20:16   
# Email: zzq@caf.ac.cn
# Software: PyCharm


import wget




class DownloadFromGithub:
    def download_software(self, url, software_name):
        download_url = url
        wget.download(url, f"./Software/{software_name}")


class FolderJudgmentAndSetUp:
    def folder_exist(self):
        pass


    def folder_set_up(self):
        pass

