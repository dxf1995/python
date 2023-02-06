# 第二种获取表格信息方法

from openpyxl import load_workbook
workbook = load_workbook(filename= "D:/learn/python/day12/CPU详细参数汇总.xlsx")
sheet = workbook.active
# 切换到对应 list
sheet = workbook["至强3代Cooperlake"]
print(sheet)

cell_1 = sheet["A4"]
cell_2 = sheet["B4"]
cell_3 = sheet["C4"]
print(cell_1.value, cell_2.value, cell_3.value)
