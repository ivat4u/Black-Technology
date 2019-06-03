from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageFilter
import os
import tkinter.messagebox
import tkinter.ttk
sizex=0
sizey=0
path=''
root = Tk()
root.geometry('730x400')
# 设置窗口标题
root.title('图片格式转换')
def loadimg():
    global path
    global sizex
    global sizey
    path = tkinter.filedialog.askopenfilename()
    lb.config(text=path)
    if path != '':
        try:
            img = Image.open(path).copy()
            sizex=img.size[0]
            sizey=img.size[1]
            x.set(sizex)
            y.set(sizey)
        except OSError:
            tkinter.messagebox.showerror('错误', '图片格式错误，无法识别')


def convert(path,type='png',x=sizex,y=sizey,):
    x=int(x)
    y=int(y)
    file_path=os.path.dirname(path)
    filename=os.path.basename(path)
    front=filename.split('.')[0]
    def function(img):
        try:
            if (0 in cl_dict):
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            if (1 in cl_dict):
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
            if (2 in cl_dict):
                img = img.filter(ImageFilter.GaussianBlur)
            if (3 in cl_dict):
                img = img.filter(ImageFilter.BLUR)
            if (4 in cl_dict):
                img = img.filter((ImageFilter.EDGE_ENHANCE))
            if (5 in cl_dict):
                img = img.filter(ImageFilter.FIND_EDGES)
            if (6 in cl_dict):
                img = img.filter(ImageFilter.EMBOSS)
            if (7 in cl_dict):
                img = img.filter(ImageFilter.CONTOUR)
            if (8 in cl_dict):
                img = img.filter(ImageFilter.SHARPEN)
            if (9 in cl_dict):
                img = img.filter(ImageFilter.SMOOTH)
            if (10 in cl_dict):
                img = img.filter(ImageFilter.DETAIL)
        except ValueError as e:
            tkinter.messagebox.showerror('错误',repr(e))
        return img
    if path != '':
        try:
            img = Image.open(path)
            img=function(img)
            img = img.resize((x, y), Image.ANTIALIAS)
            img.save(file_path + '\\' + front + '.' + type)

        except OSError:
            lb.config(text="您没有选择任何文件")
            tkinter.messagebox.showerror('错误', '图片格式错误，无法识别')
    else:
        tkinter.messagebox.showerror('错误', '未发现路径')
        #im.transpose(Image.FLIP_LEFT_RIGHT)水平镜像 or im.transpose(Image.FLIP_TOP_BOTTOM)垂直镜像



v=IntVar()
#列表中存储的是元素是元组
types=[('png',0),('jpg',1),('bmp',2),('pdf',3),('jpeg',4)]
type='png'
def callRB():
    for i in range(5):
        if (v.get()==i):
            global type
            type=types[i][0]
lb = Label(root,text = '选取格式后会在原路径生成对应格式')
lb.pack()
btn = Button(root,text="转换图片",command=lambda :convert(path,type,x.get(),y.get()))
btn2 = Button(root,text="选择图片",command=loadimg)
btn2.pack()
btn.pack()
fm1 = Frame(root)
#for循环创建单选框
for lan,num in types:
    Radiobutton(fm1, text=lan, value=num, command=callRB, variable=v).pack(anchor=W,side='left')
     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
x=tkinter.StringVar()
y=tkinter.StringVar()
namex='当前x:{}'.format(sizex)
namey='当前y:{}'.format(sizey)
x.set(namex)
y.set(namey)
xEntered = tkinter.ttk.Entry(fm1, width=12, textvariable=x)
xEntered.pack(side='left')
temp_entered = tkinter.Message(fm1,text = '×')
temp_entered.pack(side='left',padx=0.5)
yEntered = tkinter.ttk.Entry(fm1, width=12, textvariable=y)
yEntered.pack(side='left')
fm1.pack(side=TOP, fill=BOTH, expand=YES)
fm2=Frame(root)
lb2 = Label(fm2,text = '警告：如果使用原格式会覆盖原图片',width=27,height=2,font=("Arial", 10),bg="red")
lb2.pack(side='top')
fm2.pack(side=TOP, fill=BOTH, expand=YES)
fm3=Frame(root)
fm3.pack(side=TOP, fill=BOTH, expand=YES)
cl=[IntVar() ,IntVar() ,IntVar() ,IntVar() ,IntVar() ,IntVar() ,IntVar() ,IntVar() ,IntVar() ,IntVar() ,IntVar() ]
cl_dict=[]
'''
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4= IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()
CheckVar10 = IntVar()
CheckVar11 = IntVar()  '''
def call_checkbutton():
    for i in range(11):
        if(cl[i].get()==1):
            cl_dict.append(i)
        else:
            try:
                cl_dict.remove(i)
            except:
                continue

            
l=[]
l.append(tkinter.Checkbutton(fm3,text="水平镜像",command=call_checkbutton,variable=cl[0],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="垂直镜像",command=call_checkbutton,variable=cl[1],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="高斯模糊",command=call_checkbutton,variable=cl[2],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="普通模糊",command=call_checkbutton,variable=cl[3],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="边缘加强",command=call_checkbutton,variable=cl[4],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="寻找边缘",command=call_checkbutton,variable=cl[5],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="浮雕",command=call_checkbutton,variable=cl[6],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="轮廓",command=call_checkbutton,variable=cl[7],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="锐化",command=call_checkbutton,variable=cl[8],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="平滑",command=call_checkbutton,variable=cl[9],onvalue = 1, offvalue = 0))
l.append(tkinter.Checkbutton(fm3,text="细节",command=call_checkbutton,variable=cl[10],onvalue = 1, offvalue = 0))

for bt in l:
    bt.pack(side='left',expand=True)


# 高斯模糊
# im.filter(ImageFilter.GaussianBlur)
# 普通模糊
# im.filter(ImageFilter.BLUR)
# 边缘增强
# im.filter(ImageFilter.EDGE_ENHANCE)
# 找到边缘
# im.filter(ImageFilter.FIND_EDGES)
# 浮雕
# im.filter(ImageFilter.EMBOSS)
# 轮廓
# im.filter(ImageFilter.CONTOUR)
# 锐化
# im.filter(ImageFilter.SHARPEN)
# 平滑
# im.filter(ImageFilter.SMOOTH)
# 细节
# im.filter(ImageFilter.DETAIL)
root.mainloop()

