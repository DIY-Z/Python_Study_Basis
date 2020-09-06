from sys import argv

script, filename = argv

txt = open(filename)    #txt = open(filename)返回的是文件对象

print ("Here's your file %r:" % filename)
print (txt.read())      #执行txt.read()时就把文件的内容读出来了

print ("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())

