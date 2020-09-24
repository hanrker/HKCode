# import ExCAD as cad
from tkinter import *
import os
root= Tk()
root.title('我的第一个Python窗体')

div = Frame(root,width = 2000, height = 200)
div.place(x=10,y=20)
root.geometry('1600x900') # 这里的乘号不是 * ，而是小写英文字母 x

lab = Label(div, text = '输入路径',  height = 2 ,justify = LEFT)
# lab.pack(fill = X)
lab.grid(row = 0,column=0 , padx = 2)

inp = Entry(div, width = 50 )
inp.grid(row = 0,column=1)

But = Button(div, text = 'read', width = 10,command= test)
But.grid(row = 0,column=2,padx = 2)

resV = StringVar()
resV.set("打开文件路径")
res = Label(div,  textvariable = resV,  height = 5 , width = 10 ,justify = LEFT)

res.grid(row = 2,column=0)

putpath = Button(div,  textvariable = resV,  height = 1 , width = 50   ,justify = LEFT)
putpath.grid(row = 2,column=1)

#批量打包元素
# uiEles = [lab,inp,But,res]
# print(uiEles)
# UIPack(uiEles) 
root.mainloop()

input("ss")

def UIPack(eles):
    for ele in eles:
        ele.pack()

def test():
    print('s')
    print(inp.get())
    resV.set(inp.get())