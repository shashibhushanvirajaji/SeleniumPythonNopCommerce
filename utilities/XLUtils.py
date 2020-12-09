import xlrd

workbook = xlrd.open_workbook('C:\\Users\\svirajaj\\PycharmProjects\\nopCommerceApp\\testdata\\testdata.xlsx')
sheet = workbook.sheet_by_name('login')


def getrows():
    return sheet.nrows


def getcolumns():
    return sheet.ncols


def getdata(r, c):
    return sheet.cell_value(r, c)
