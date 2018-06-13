# 练习一 异常
#1. 在Python程序中，分别使用未定义变量、访问列表不存在的索引、
# 访问字典不存在的关键字观察系统提示的错误信息


try:
    i=j
except NameError:
    print('变量没有定义哦')

try:
    i = '123'
    print(i[3])
except IndexError:
    print('请注意列表的长度哦')


try:
    dict = {'a':1,'b':12,'c':23}
    print(dict['d'])
except KeyError:
    print('请注意调用的关键字是否存在哦')

# try:
#     a = open('name.txt')
# except Exception as e:
#     print(e)
#
# finally:
#     a.close()

#2. 通过Python程序产生IndexError，并用try捕获异常处理


a_list = ['a','b','c','d']



for i in range(0,len(a_list) + 2) :
    try:
        print(a_list[i])
    except IndexError:
        print('请注意列表长度哦')
    finally:
        if i >= len(a_list) :
            print("当前的 i 为 %d" %i)
            break
