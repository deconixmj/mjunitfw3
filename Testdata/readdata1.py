import xlrd

wb = xlrd.open_workbook("D:\Py_projects\mjunitfw3_testsuite_nose\Testdata\Excel_data\\tdata.xlsx")
# sheet = wb.sheet_by_name("dataset1")
sheet1 = wb.sheet_by_name("dataset2")


def getData1():
    entirelist=[]
    for i in range(1,sheet1.nrows):
        data=[]
        for j in range(0,sheet1.ncols):
            data.append(sheet1.cell_value(i,j))
        entirelist.append(data)
    return entirelist
#
# print(getData1())