# numbers = list(range(1,6))
# print(numbers)
# 数到20：使用一个for循环打印数字1~20
# for numbers in range(1,21):
#     print(numbers)
#


#4-4 一百万
# for numbers in range(1,1000001):
#     print(numbers)

#4-5 创建一个列表，其中包含数字1~1 000 000的总和“创建一个列表，其中包含1~1 000 000，在使用min()和max()核实该列表确实是从1开始，到1 000 000 结束的， 另外，对这个列表调用函数sum(),看看python一百万个数字相加需要多长时间

# list = range(1,1000001)
# print(min(list))
# print(max(list))
# print(sum(list))

#4-6 奇数： 通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数，再使用一个for循环将这些数字打印出来

jishu = range(1,21,2)
for vlaue in jishu:
    print(vlaue)