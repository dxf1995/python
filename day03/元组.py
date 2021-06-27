# python 将不能修改的值称为不可变的， 而不可变的列表被称为元组。
# 元组是使用圆括号（）， 列表是使用[] 方括号
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 元组的值是不可以修改的，所以以下的写法是错误的
# dimensions[0] = 10
# print(dimensions)

# 元组的遍历 和 修改元组的变量
dimensions= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
for vlue in dimensions:
    print(vlue)

·