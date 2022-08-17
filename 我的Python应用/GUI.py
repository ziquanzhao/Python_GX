# 编写人：赵子权
# 编写时间：2022/4/30 19:55
# 邮箱:2939818719@qq.com
from tkinter import *
from tkinter import messagebox
import webbrowser  # 调用浏览器打开网页的


class Application1(Frame):            # Frame是一个虚拟组件，就像是一个空盒子，定一个Frame，然后可以才这个空盒子里再放其他小组件，每个小组件对应若干函数
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(side='left')         # pack是打包函数，是让这个窗口打包到界面中，没有pack的话看不到内容
        # 以上三行代码就是定义一个有隔间的空盒子，下面可以定义很多实质内容的函数

        self.window1()      # 实际应用的函数
        self.window2()
        self.window3()
        self.window4()
        self.window5()
        self.window6()

        '''
        pack()的参数
        anchor	1. 控制组件在 pack 分配的空间中的位置
                2. "n", "ne", "e", "se", "s", "sw", "w", "nw", 或者 "center" 来定位（ewsn 代表东西南北，上北下南左西右东）
                3. 默认值是 "center"
                
        expand	1. 指定是否填充父组件的额外空间
                2. 默认值是 False
                
        fill	1. 指定填充 pack 分配的空间
                2. 默认值是 NONE，表示保持子组件的原始尺寸
                3. 还可以使用的值有："x"（水平填充），"y"（垂直填充）和 "both"（水平和垂直填充）
                
        in_	    1. 将该组件放到该选项指定的组件中
                2. 指定的组件必须是该组件的父组件
                
        ipadx	指定水平方向上的内边距
        
        ipady	指定垂直方向上的内边距
        
        padx	指定水平方向上的外边距
        
        pady	指定垂直方向上的外边距
        
        side	1. 指定组件的放置位置
                2. 默认值是 "top"
                3. 还可以设置的值有："left"，"bottom"，"right"
        '''

    def window1(self):
        """ 定义一个小按钮，然后把这个小组件和函数连接起来，就可以实现点击按钮运行函数 ,按钮是可以点击的 """
        self.btn1 = Button(self, text='点击送花', command=self.songhua, width=8, height=1, anchor=NW, bg='white', fg='black', font=('Times New Roman',16), relief=SUNKEN, justify='center')  #定义文本按钮，和Label基本完全一样
        self.btn1.pack()         # pack打包，将按钮打包到Application组件中

        #显示图片按钮
        global photo1
        photo1 = PhotoImage(file='./XsKCS1+181.gif')
        self.btn2 = Button(self, image=photo1, command=self.songhua, width=30, height=20)
        self.btn2.pack()
    def songhua(self):
        messagebox.showinfo('送花', '送你一朵小红花')  # messagebox.showinfo（title，message），第一个参数是这条信息的名字，然后是信息内容，就类似于window报错弹窗

        '''
        1.state,默认是able，可以设置为disable，state=disabled，此时这个按钮不能点击，是灰色的
        '''




    def window2(self):
        """制作一个标签，一个Label，注意标签是不可点击的，按钮可以，Button可以"""
        self.lable1 = Label(self, text='HMMbuild', width=8, height=1, bg='white', fg='black', font=('华文中宋', 16))
        self.lable1.pack()

        # 显示图像标签怎么办
        global photo       # 声明一个全局变量，因为我们GUI是一个循环式交互对象，而后面调用的Photoimage函数加载的图像信息是一个局部变量，我们想让图像信息一直存在的话，就需要全局变量
        photo = PhotoImage(file='./XsKCS1+181.gif', width=20, height=20)  # 利用Photoimage函数加载图像信息，记住只能是gif格式图像，其他不行
        self.label2 = Label(self, image=photo)
        self.label2.pack()

        #显示多行文本怎么办
        self.label3 = Label(self, text='HMM\nMakeblastdb', justify='center', font=('华文中宋', 16), fg='blue', bg='white', relief=SOLID, borderwidth=1.5, padx=5, pady=10)
        self.label3.pack()
        '''
        Label标签
        作用：用来显示文本信息，也可以显示图片
        常见属性：
        1.width，height：指定区域大小，如果是文本，则一个英文字母站一个单位（一个汉字宽度站2个单位，高度站1个字符），如果是图像，则以像素为单位。
        2.font指定文本字体和大小，如，font = （font_name，size）
        3.image，显示在Label上的图像，只支持gif格式
        4.fg和bg，fg（foregound）是前景色，bg（backgound）是背景色
        5.justify。针对多行文字的对齐，可选’left‘，’right‘，’center‘
        6.anchor,文本或图像在背景内容区的位置，就是如果标签很大而文字很小，此时文字放在标签的什么位置，默认为 center，可选值为（n,s,w,e,ne,nw,sw,se,center）eswn 是东南西北英文的首字母，表示：上北下南左西右东。
        7.relief,边框样式，可选的有：FLAT、SUNKEN、RAISED、GROOVE、RIDGE,SOLID。默认为 FLAT,RIDGE用着较好。borderwidth=1，用来指定宽度，默认为1
        8.padx，x 轴间距，以像素计，默认 1。	pady，y 轴间距，以像素计，默认 1。可以认为这是控制整个标签大小的一个参数，就是标签文字距离标签边界的距离,不支持图像，支持文本
        '''




    def window3(self):
        """创建一个单行文本框，用来输入数据的"""
        self.label4 = Label(self, text='用户名', bg='white', fg='black', font=('华文中宋',13), justify='center')
        self.label4.pack()
        x = StringVar()
        self.entry1 = Entry(self, textvariable=x)
        self.entry1.pack()
        self.label5 = Label(self, text='密码', justify='center', font=('华文中宋', 13))
        self.label5.pack()
        y = StringVar()
        self.entry2 = Entry(self, textvariable=y)
        self.entry2.pack()

        #创建登录按钮
        self.btn3 = Button(self, text='登录', font=('华文中宋',13), command=self.login)
        self.btn3.pack()
    def login(self):
        username = self.entry1.get()
        pwd = self.entry2.get()
        messagebox.showinfo('欢迎回来', username)
        print('用户名：', username)
        print('密码：', pwd)
        """
        x = StringVar()是用来创建一个接收变量的，接受你输入的内容，把你输入的内容传递到x上。
        StringVar（）传递的是字符串类型
        IntVar()传递数字类型
        DoubleVar（）传递浮点型
        BooleanVar传递布尔型
        """



    def window4(self):
        """多行文本操作"""
        self.text1 = Text(self, width=50, height=30, fg='black', bg='white')
        self.text1.pack()
        #如何在这个多行文本框中插入内容
        self.text1.insert(1.0, '123456')  # 意思是在第一行第0列（就是第一列）的位置开始，插入123456
        self.text1.insert(2.3, 'abc\ncd')

        # 可以创建一些按钮，方便输出输入内容
        Button(self, text='插入文本', command=self.inserttest).pack(side='left', padx=5, pady=10)
        Button(self, text='输出指定文本', command=self.returntext).pack(side='left', padx=5, pady=10)  #pack参数配合使用，可以实现固定位置
        Button(self, text='tag', command=self.tagtest).pack(side='left', padx=5, pady=5)
    def inserttest(self):
        self.text1.insert(INSERT, 'AAAA')  # 在光标处插入AAAA
        self.text1.insert(END, 'BBB')  # 在末尾插入BBB
    def returntext(self):
        messagebox.showinfo('输出1', self.text1.get(1.0, 2.2))   # 弹出第一行第一列到第二行第3列的内容
        messagebox.showinfo('输出2', self.text1.get(1.0, END))
    def tagtest(self):
        self.text1.delete(1.0, END)  # 把之前多有内容全部删除
        self.text1.insert(1.0, 'baidu\nbaidu')
        self.text1.tag_add('A', 1.0, 1.5)   # 插入标记，标记的名字记为A，标记的范围只1.0到1.4，就是第一个baidu
        self.text1.tag_config('A', underline=True ,underlinefg='blue', foreground='red', background='yellow')  # 对标记内容添加下划线，下划线颜色为蓝色
        self.text1.tag_bind('A', '<Button-1>', self.webshow)
    def webshow(self, event):        # 注意这里的event不要少
        webbrowser.open('http://www.baidu.com')



    def window5(self):
        """二选一的选择标签创建"""
        self.x = StringVar()     # 设置一个双向传递变量
        self.x.set('男')    # 设置默认值
        self.r1 = Radiobutton(self, text='男性', value='男', variable=self.x)
        self.r1.pack(side='left', padx=5, pady=10)
        self.r2 = Radiobutton(self, text='女性', value='女', variable=self.x)
        self.r2.pack(side='left', padx=5, pady=10)
        Button(self, text='确定', command=self.xingbie).pack(side='left', padx=5, pady=10)
    def xingbie(self):
        messagebox.showinfo('性别判断', '结果为:'+self.x.get())



    def window6(self):
        pass






root = Tk()   # 这几行别问，标准格式，Tk，T大写，k小写，这是创建一个主窗口界面的意思，并且自带最小化，最大化，关闭按钮，root是个变量，代表主窗口，就好像一个本子，可以在本子上创建很多纸你也可以用其他字母
root.geometry('1280x720+320+180')  # 特别注意x，是小写字母x，不是乘号
'''
geometry(’wxh±x±y‘)  w窗口宽度，h窗口高度，+x表示距离屏幕左边界多少像素，-x代表据里屏幕右边界多少，+y表示距离窗口上边界缩少，-y表示下边界
geometry(1600×900+100+100)
特别注意xy其实就是定义你打开这个软件时，这个软件的界面出现在屏幕什么位置，一般电脑都是1920*1080，如果想出现在屏幕中央，就定义+320+180
'''
root.title('GUI')  # 为窗口起一个名字
app1 = Application1(master=root)        # 把root窗口和组件联系起来

root.mainloop()   # 形成交互式循环结构，固定用法，别问



