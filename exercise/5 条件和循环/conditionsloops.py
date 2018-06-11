
# 练习一 条件语句的使用

1. 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出

str_a = str(input('请输入任意长度字符串：\n'))

if len(str_a) == 10:
    print('输入的字符串长度等于10')
else:
    print('输入的字符串长度不等于10')

# 2. 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出

int_a = int(input('输入一个1-40之间的数字：\n'))

if int_a >= 1 and int_a <= 10 :
    print('输入的数字在 1-10')
elif int_a >= 11 and int_a <= 20 :
    print('输入的数字在 11-20')
elif int_a >= 21 and int_a <= 30 :
    print('输入的数字在 21-30')
elif int_a >= 31 and int_a <= 40 :
    print('输入的数字在 31-40')

# # 练习二 循环语句的使用
# 1. 使用for语句输出1-100之间的所有偶数
import numpy as np

for i in np.arange(1,101):
    if i % 2 :
        #print("%s 是奇数" %i)
        continue
    else:
        print("%s 是偶数" % i)

# 2. 使用while语句输出1-100之间能够被3整除的数字
i = 0
while i <= 100:
    i += 1
    if i%3 == 0 :
        #continue
        print(i)


