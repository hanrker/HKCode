import funcs as funcs
# import ExCAD as cad
from tkinter import *
root= Tk()
root.title('我的第一个Python窗体')
# root.geometry('1600x900') # 这里的乘号不是 * ，而是小写英文字母 x

uiEles = [Label,lab,inp,But,res]
lab = Label(root, text = 'path',  height = 2 , width = 10)
# lab.pack(fill = X)

inp = Entry(root, width = 50 )
# inp.pack()

But = Button(root, text = 'read', width = 50,command= test)
# But.pack()

resV = StringVar()
resV.set("output")
res = Label(root,  textvariable = resV,  height = 5 , width = 10)
putpath = Button(root,  textvariable = resV,  height = 5 , width = 10)

res.pack()
# putpath.pack()

UIPack(uiEles)


root.mainloop()

def UIPack(eles):
    for ele in eles:
        ele.pack()

def test():
    print('s')
    print(inp.get())
    resV.set(inp.get())