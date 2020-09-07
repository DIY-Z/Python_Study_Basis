from sys import argv
from os.path import exists      #这个命令将文件名字符串作为参数， 如果文件存在的话，它将返回 True ， 否则将返回 False

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line, how?   很简单，写成这样即可indata=open(from_file).read()
in_file = open(from_file)   
indata = in_file.read()     #将一个文件的内容全部读出
#indata=open(from_file).read()
print ( "The input file is %d bytes long" % len(indata))

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')   #将另一个文件开启写模式
out_file.write(indata)        #将数据写入

print ("Alright, all done.")

out_file.close()                #最后记得close
in_file.close()