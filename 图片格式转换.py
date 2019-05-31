from tkinter import *
import tkinter.filedialog
from PIL import Image
import os
import tkinter.messagebox

root = Tk()
root.geometry('500x200')
# 设置窗口标题
root.title('图片格式转换')
def convert(type='png'):
    path = tkinter.filedialog.askopenfilename()
    file_path=os.path.dirname(path)
    filename=os.path.basename(path)
    front=filename.split('.')[0]
    if path != '':
        try:
            img = Image.open(path)
        except OSError:
            tkinter.messagebox.showerror('错误', '图片格式错误，无法识别')
        img.save(file_path+'\\'+front+'.'+type)
    else:
        lb.config(text = "您没有选择任何文件")


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
btn = Button(root,text="选择图片",command=lambda :convert(type))
btn.pack()
#for循环创建单选框
for lan,num in types:
    Radiobutton(root, text=lan, value=num, command=callRB, variable=v).pack(anchor=W)

root.mainloop()

