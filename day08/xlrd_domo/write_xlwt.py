import xlwt


# 新建Excel 表格
new_workbool = xlwt.Workbook()

# 创建sheet
worksheet = new_workbool.add_sheet('new_test')

# 新建单元格， 并写入内容
worksheet.write(0, 0, 'oneMeng')

# 保存
new_workbool.save('write_one.xls')
