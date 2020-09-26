import os.path
import tkinter.filedialog as tkDlg

import ExTable as ex
import tkinter as tkUI

ex.__int__()


# i = ex.SelectFile()
# print(i)

# if i !=0:
#     list1 = ex.ReadExel(i,name = '',sheet_name='')
#     print(list1)
#     new_list = ex.Exdata(list1,[1,2,1,3,4])

#     out = ex.SaveXlsxFile()
#     print(out)
#     new_file = ex.WriteExcel_xlsx_row(out,new_list)
# input()


def UIgrid(glist):
    # index = len(glist)
    for indexi, row in  enumerate(glist):
        # print(indexi)
        for indexj,ele in enumerate(row):
            # print(indexj)
            ele.grid(row = indexi, column= indexj)
# UIgird([[1,2,3],[2,3]])

def SelectFile():
    temp =  ex.SelectFile()
    input_path.delete(0,"end")
    input_path.insert(0,temp)
    return  temp
#    input_path.    

def SaveFile():
    #改变输出路径
    output_path.delete(0,"end")
    output_path.insert(0,ex.SaveXlsxFile())

def Change():
    rule = input_rule.get().strip(',').split(',')
    print(input_path.get())
    if input_path.get()!=' ':
        li = ex.ReadExel(input_path.get(),sheet_name='Sheet1')
        print(li)
        if li !=1 and li != 2:
            print(rule)
            new_list = ex.Exdata(li,rule)
            if output_path.get()!=' ':
                ex.WriteExcel_xlsx_row(output_path.get(),new_list,sheet_name='Sheet1')
    # return  ex.SaveXlsxFile()

root = tkUI.Tk()
label1 = tkUI.Label(root,text='请选择文件')
input_path = tkUI.Entry(root,width = 100)
input_change = tkUI.Button(root,text='选择', command = SelectFile)


label2 = tkUI.Label(root,text='转换规则：')
input_rule = tkUI.Entry(root,width = 100)

label3 = tkUI.Label(root,text='输出位置')
output_path = tkUI.Entry(root,width = 100)
output_change = tkUI.Button(root,text='选择', command = SaveFile)

change = tkUI.Button(root,text='转换', width = 50, command = Change)
change.grid(row = 3, column =1)


li = [
    [label1,input_path,input_change],
    [label2,input_rule],
    [label3,output_path,output_change],
]

UIgrid(li)

root.mainloop()

