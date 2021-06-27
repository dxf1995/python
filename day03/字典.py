# 例子1
# dictionaries = {
#     'first_name': 'duan',
#     'last_name': 'xiaofeng',
#     'age': '18',
#     'city': 'jiujang',
# }
# print(dictionaries)
# print(dictionaries['first_name'])

#例子2
# luckNumber = {
#     'duanxf2':'7',
#     'xiaoming':"8",
#     'xiaohei':"1",
# }
#
# print(luckNumber['duanxf2'] + " luck Number" )
# print(luckNumber['xiaoming'] + ' luck number')
# print(luckNumber['xiaohei'] + ' luck number')


#列3
dictionariesBook = {
    "English":'中文',
    "number":"数字",
    "Run":'运行',
    "For":"循环",
}

print(dictionariesBook)

#遍历字典
# for key, value in dictionariesBook.items():
#     print("\nkey: " + key)
#     print("Value: " + value)
#
# for key in dictionariesBook:
#     print("\nkey: "+ key)

# 使用sorted() 方法来排序遍历字典
# for key, value in sorted(dictionariesBook.items()):
#     print("\nkey: " + key)
#     print("\nvalue: " + value)

# 使用 values() 遍历字典中所有的值
# for value in dictionariesBook.values():
#     print("\nvalue: " + value)


favorite_languages = {
    'jen':['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
# 在字典中存储字典
users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
    },
    'mcuir' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + "" + user_info['last']
    location = user_info['location']

    print("\nFull name:")