import xlwt,xlrd2
import win32ui
import os

workpath =str(os.getcwd()) + "\ExcelToSQL"

SQLFrom ='[PCMS.TEST].[dbo].[PcTagElmt]'

dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
dlg.SetOFNInitialDir(workpath)  # 设置打开文件对话框中的初始显示目录
dlg.DoModal()
filename = dlg.GetPathName()  # 获取选择的文件名称
print(filename)
ExcelToSQL(filename)



def ExcelToSQL(file):
    # 判断是否文件是否为空
    if file is not None:
        # 读取文件
        data = xlrd2.open_workbook(file)
        sheet = data.sheet_names()


        # 读取第一个sheet表格
        table = data.sheet_by_name(sheet[0])   

        rowNum = table.nrows    #获取有效总行数
        col = table.ncols       #获取有效总列数

        print("You select "+str(file)  + "中的"+ str(table))
        print("The total rows is " + str(table.nrows))
        print("The total cols is " + str(table.ncols))

        # 初始化数据库语句
        sql = []
        for r in range(rowNum):
            if r > 0 :
                sql.append('update '+ SQLFrom + ' set ')
                for c in range(col):
                    # print(table.cell(r,c).value)
                    sql[r-1] = sql[r-1] + SetVa(table.cell(0,c).value,table.cell(r,c).value) 
                    if c < (col-1) :
                        sql[r-1]  = sql[r-1] +', '
                
                sql[r-1] =  sql[r-1] + " where " + SetVa("id",table.cell(r,0).value)
                print(sql[r-1])
        #输出SQL语句至txt文件
        WriteTxt("sql",str(workpath),sql)

def SetVa(title,value):
    if is_number(value):
        res = str(title) + "=" + str(value) +""
    else:
        res = str(title) + "='" + str(value) +"'"
    # print(res)
    return res

#判断是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def WriteTxt(name,path,content):
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
# WriteTxt("11","D:\\HKFiles\\Code\\HKCODE\\python\\ExcelToSQL\\","21")
