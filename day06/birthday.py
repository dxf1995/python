"""

age = 23
message = "Happy\n" + str(age) + "\nTom Birthday! "
print (message)

# 整数取余
number = 3/2
print(number)

#遍历整个列表
print(bicycles[0])
for i in bicycles:
    print(i)
print('----------------------------next code --------------------------')

"""

# 列表
bicycles = ['Trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

bicycles.append('wahaha')
print(bicycles)

# 下面这种赋值情况会打印个空，list.appennd()没有返回值，所以是None，且 apped会修改原返回值。
list_01 = bicycles.append('tiantain')
print(list_01)

# 在指定位置插入元素
bicycles.insert(2, 'lushi')
print(bicycles)

# 删除元素 永久性删除
del bicycles[0]
print(bicycles)

print('pop 删除法 '+ bicycles.pop(0))

print(bicycles)
# 查
print(bicycles[2])
