import xlrd

# 打开文件
xlsx = xlrd.open_workbook('singapore-residents.xlsx')

# 打开对应的sheet
sheet = xlsx.sheet_by_index(0)
# 取出对应位置的内容
data = sheet.cell_value(3, 3)

print(data)

