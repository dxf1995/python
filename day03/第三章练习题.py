test = ['Aaaaa', 'Bbbbb', 'Ccccc']
print(str(test) + ' 请名单的朋友2月3号来我家里玩')
print(str(test[0])+ '\t由于天气原因无法来了' )
test[0] = 'Eeeee'
print(test)
print(str(test) + '\t那你2月3号来我家里玩吧')
print('老子找到了 一群妹子来，有没有人来玩啊 加我微信\n')
test.insert(0,'Ttttt')
print(test)
test.insert(2,'Ooooo')
print(test)
test.append('Duan')
print(test)
print(str(test) + '\t兄弟们来玩吧来呀快活呀')
print(str(len(test)) + '有这么兄弟要来呀')
print('操 你麻痹有几个妹子不来了，玩个鸡毛啊')
test.pop()
print(test)
test.pop()
print(test)
test.pop()
print(test)
test.pop()
print(test)

del test[0]
print(test)

del test[0]
print(test)
