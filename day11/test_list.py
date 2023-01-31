'''
Author: mr.duan 861272006@qq.com
Date: 2023-01-31 00:26:59
LastEditors: mr.duan 861272006@qq.com
LastEditTime: 2023-01-31 21:31:40
FilePath: \learn\python\day11\test_list.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from openpyxl import load_workbook

workbook = load_workbook(filename = "D:/learn/python/day11/Dera SSD_01.xlsx")

#获取sheet名称
#print(workbook.sheetnames)

sheet = workbook["Sheet1"]
print(sheet)