import xlrd2,win32ui
import os
import tkinter


inputFile = '结果'
outputPath = ''
outputFile =''
workpath =str(os.getcwd()) + "\ExcelToSQL"

# master = tkinter.Tk()

# inputLabel = tkinter.Label(master,text = '输入文件', justify="left")
# inputButton = tkinter.Button(master,text = '选择文件',command = SelectFile)
# filename = tkinter.Label(master,text =str(inputFile) )

# inputLabel.pack()
# inputButton.pack()
# filename.pack()
# # 进入消息循环
# master.mainloop()

inputFile = SelectFile()


#选择文件
def SelectFile():
    dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
    dlg.SetOFNInitialDir(workpath)  # 设置打开文件对话框中的初始显示目录
    dlg.DoModal()
    filename = dlg.GetPathName()  # 获取选择的文件名称
    print(filename)
    return filename


def WriteExcel(name,path,content):
    full_path = str(path) + "\\" + str(name)  + '.txt' 
    print(full_path)
    file = open(full_path, 'w')

    #如果内容是list，则循环写入
    if(type(content) ==list ):
        for i in range(len(content)):
            file.write(content[i]) #写入内容
            file.write('\n')
    else:
        file.write(str(content)) #写入内容
        file.write('\n')
    # file.write("end") #写入内容
    print("export file:"+ full_path)
    file.close()
