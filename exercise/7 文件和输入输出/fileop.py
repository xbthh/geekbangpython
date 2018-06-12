# # 练习一 文件的创建和使用
# 1. 创建一个文件，并写入当前日期

file1 = open('today.txt','w')
file1.write('20180612')
file1.close()
#print(file1)

# 2. 再次打开这个文件，读取文件的前4个字符后退出
file2 = open('today.txt')
#file2_r = file2.read()
print(file2.read(4))
#print(file2_r[-4:])

file2.close()
