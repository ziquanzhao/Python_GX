# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
import tkinter
import os
from tkinter import *
import tkinter.filedialog
import time
import threading
import pygame
from PIL import Image, ImageTk

# 新建一个GUI界面
Frame = Tk()
Frame.title("属于自己的音乐播放器")

# 设置长和款
width = 600
height = 400

screenwidth = Frame.winfo_screenwidth()
screenheight = Frame.winfo_screenheight()

alignstr = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
Frame.geometry(alignstr)

Frame.resizable(False, False)
file = Image.open('./music player/picture/image.jpg')
img = ImageTk.PhotoImage(file)
background = tkinter.Label(Frame, image=img)
background.image = img
background.pack()

# 设置一个图标
# Frame.iconbitmap("")

# 设置全局变量
folder = ""  # 文件路径
music_dir = []  # 音乐文件路径
music_name = []  # 音乐文件名称
num = 0  # 当前所播放的音乐序号
playing = False  # 音乐是否在播放
flag = 0  # 单曲循环 or 顺序播放
skip = 0  # 上一首下一首的标记


# 选择播放音乐所在文件夹
def buttonAddClick():
    # global限定全局变量
    global folder
    global music_dir
    global music_name
    global playing
    # 选择一个文件夹并其返回路径
    folder = tkinter.filedialog.askdirectory()
    if not folder:
        return
    music_name.clear()
    music_dir.clear()
    # 读取文件夹里的音乐文件
    for each in os.listdir(folder):
        if each.endswith((".mp3", ".wav", ".ogg")):
            music_name.append(each)
            music_dir.append(folder + "\\" + each)
    if (len(music_dir) == 0):
        return
        # 将文件名列出到GUI上
    var = StringVar()
    var.set(music_name)
    music_list = Listbox(Frame, listvariable=var)
    music_list.place(x=200, y=240, width=260, height=150)

    playing = True
    buttonPlay["state"] = "normal"
    start_stop.set("播放")
    buttonAdd["state"] = "disabled"
    pygame.mixer.init()


# 播放音乐函数
def play():
    global num
    global playing
    global flag
    global skip
    if len(music_dir):
        pre = 0  # 上一首
        while playing:
            if not pygame.mixer.music.get_busy():  # 没有音乐播放
                if flag:
                    if not skip:
                        num = pre
                skip = 0
                next_music = music_dir[num]
                pygame.mixer.music.load(next_music.encode())
                pygame.mixer.music.play(1)
                musicName.set("正在播放:" + music_name[num])
                pre = num
                if len(music_dir) - 1 == num:
                    num = 0
                else:
                    num = num + 1
            else:
                time.sleep(0.1)


# 播放暂停切换
def buttonPlayClick():
    buttonNext["state"] = "normal"
    buttonPrev['state'] = 'normal'
    buttonCircle['state'] = 'normal'
    if start_stop.get() == "播放":
        start_stop.set("暂停")
        # 新建一个线程来后台播放音乐
        t = threading.Thread(target=play)
        t.start()
    elif start_stop.get() == "暂停":
        pygame.mixer.music.pause()
        start_stop.set("继续")
    elif start_stop.get() == "继续":
        pygame.mixer.music.unpause()
        start_stop.set("暂停")


# 回到上一首
def buttonPrevClick():
    global skip
    skip = 1
    pygame.mixer.music.stop()
    global num
    if num == 0:
        num = len(music_dir) - 2
    elif num == 1:
        num = len(music_dir) - 1
    else:
        num -= 2

    # 切换下一首


def buttonNextClick():
    global skip
    skip = 1
    pygame.mixer.music.stop()


# 播放模式的切换
def buttonCircClick():
    global flag
    if mode_change.get() == "单曲循环":
        flag = 1
        mode_change.set("顺序播放")
    else:
        flag = 0
        mode_change.set("单曲循环")

    # 调整音量


def controlVoice(value):
    global playing
    if playing:
        pygame.mixer.music.set_volume(float(value))


def closeWindow():
    # playing 变 False，从而结束循环,t线程退出
    global playing
    playing = False
    time.sleep(0.3)
    if len(music_name) > 0:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    Frame.destroy()


# 设置关闭窗口协议
Frame.protocol("WM_DELETE_WINDOW", closeWindow)

# 添加音乐按钮
buttonAdd = Button(Frame, text="添加音乐", command=buttonAddClick)
buttonAdd.place(x=30, y=210, width=60, height=30)

# 播放/暂停按钮
start_stop = StringVar(Frame, value="播放")
buttonPlay = Button(Frame, textvariable=start_stop, command=buttonPlayClick)
buttonPlay.place(x=100, y=210, width=60, height=30)
buttonPlay["state"] = "disabled"

# 下一首按钮
buttonNext = tkinter.Button(Frame, text="下一首", command=buttonNextClick)
buttonNext.place(x=100, y=250, width=60, height=30)
buttonNext["state"] = "disabled"

# 上一首按钮
buttonPrev = tkinter.Button(Frame, text="上一首", command=buttonPrevClick)
buttonPrev.place(x=30, y=250, width=60, height=30)
buttonPrev["state"] = "disabled"

# 单曲循环/循序播放按钮
mode_change = StringVar(Frame, value="单曲循环")
buttonCircle = tkinter.Button(Frame, textvariable=mode_change, command=buttonCircClick)
buttonCircle.place(x=30, y=290, width=60, height=30)
buttonCircle["state"] = "disabled"

# 当前播放音乐
musicName = StringVar(Frame, value="暂时没有播放音乐")
labelName = Label(Frame, textvariable=musicName, justify=LEFT, fg="red")
labelName.place(x=200, y=210, width=260, height=20)

# 调节音量
labelvoice = Label(Frame, text="音量", justify=LEFT)
labelvoice.place(x=20, y=350, width=30, height=20)
s = tkinter.Scale(Frame, from_=0, to=1, orient=tkinter.HORIZONTAL, length=200, resolution=0.1, command=controlVoice)
s.set(1)
s.place(x=50, y=330, width=100)

# 循环刷新
Frame.mainloop()