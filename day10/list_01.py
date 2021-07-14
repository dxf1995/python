ssdVender = ['koxia', 'intel', 'hynix', 'micron']
print(ssdVender)

#访问列表单个元素
print(ssdVender[0])

# title 首字母大写
print(ssdVender[0].title())

message = "my vender is\n" + ssdVender[0].title() + "."
print(message)

# 修改列表
ssdVender[0] = 'hynix'
print(ssdVender)

# 添加元素
ssdVender.append("sandisk")
print(ssdVender)

# 在指定的位置插入元素

ssdVender.insert(1, 'toshiba')
print(ssdVender)

del ssdVender[0]
print(ssdVender)

del ssdVender[0]
print(ssdVender)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
