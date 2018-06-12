# # 练习一 字典的使用
#
# 1. 定义一个字典，分部使用a、b、c、d作为字典的关键字，值为任意内容

dic = {'a':110,'b':120,'c':119,'d':95536}

print(dic)

# 2. 为该字典增加一个元素‘c':'cake'后，将字典输出到屏幕

dic['c'] = 'cake'

print(dic)

# 3. 取出字典中关键字为d的值

print(dic['d'])
#
# # 练习二 集合的使用
# 1. 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕

str_a = 'hello'
print(str_a)

dict_a = {str_a[i]:str_a.count(str_a[i]) for i in range(0,len(str_a))}
list_a = [str_a[i] for i in range(0,len(str_a)) ]

print(dict_a)
print(list_a)

# i= 0
# for i in len(str_a) :
#     print(i)
#     i += 1