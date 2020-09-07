'''
close -- 关闭文件。 跟你编辑器的 文件->保存.. 一个意思。
read -- 读取文件内容。 你可以把结果赋给一个变量。
readline -- 读取文本文件中的一行。
truncate -- 清空文件， 请谨慎使用该命令。
write('stuff') -- 将stuff写入文件。
'''
from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')        #注意这里的写法,同时需要注意既然这里调用了写权限，你就不能直接read的，比如下面注释掉的部分。默认是只读权限
'''
print ("*******************")

print (target.read())

print ("*******************")
'''
print ("Truncating the file. Goodbye!")
target.truncate()   #清空文件

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it.")
target.close()      #注意只有执行此操作后才会真正把数据写入




