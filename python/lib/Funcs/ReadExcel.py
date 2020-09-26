import xlwt,xlrd2
Exfile = xlwt.Workbook()
Exfile.add_sheet("s",cell_overwrite_ok=False)

def WriteExcelXls():
    style = xlwt.XFStyle

    f = xlwt.Workbook()
    sheet1 = f.add_sheet("s",cell_overwrite_ok=True)
    row0 = ["姓名","性别","年龄","爱好"]
    colum0 = ["韩瑞凯","男","23","篮球"]
    colum1 = ["张三","女","33","读书"]

    for i in range(0,len(row0)):
        sheet1.write(0,i,label=row0[i])
        print(row0[i])
    f.save("hh.xls")
    print("ss")
WriteExcelXls()

def ReadExcel():
    print()