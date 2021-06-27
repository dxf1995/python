'''
# 1 + 100
# count 代表次数
count = 1
# sum 累加的和
sum = 0
while count <= 100:
    sum = sum + count
    print(sum)
    count = count + 1
    print(count)

print("hello Python world")


# 变量
message = "Hello Python world"
print(message)

message = "Hello Python Crash Course world!"
print(message)

'''


#字符串

'''
在这个示例中，小写的字符串 "ada lovelace" 存储到了变量 name 中。在 print() 语句中，方法 title() 出现在这个变量的后面。 方法 是 Python 可对数据执行的操作。
在 name.title() 中， name 后面的句点（ . ）让 Python 对变量 name 执行方法 title() 指定的操作。每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成
其工作。这种信息是在括号内提供的。函数 title() 不需要额外的信息，因此它后面的括号是空的。
'''
'''
name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())
'''


#合并拼接字符串
'''
first_name = "ada"
last_name = ' lovelace'
full_name = first_name + last_name
print(full_name)

'''

'''
#使用制表符或者换行符来增加空格 \t \n  \n 换行， \t 制表符
print('\t duanxf')
print('\n duanxf')


print("languaes:\n\tPython\n\tC\n\tJavaScript")


'''

#删除空白区域
favorite_language = 'python '
print(favorite_language)
favorite_language.rstrip()
print(favorite_language)

add = 0.2 + 0.2
print(add)