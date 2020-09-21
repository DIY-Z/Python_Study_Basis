from sys import argv    #你可以认为sys 是一个包， 这句代码的意思是从 sys 的包中引入 argv 功能模块。

script, first, second, third = argv

print ("The script is called:",script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

#注意在命令行输入时需要再添加3个参数，例如python ex13.py first 2nd 3rd

#argv与input()的区别
'''
如果你希望用户在脚本执行的过程中输入参数， 那就就要用到 input() 
如果你想让用户在命令行输入你的参数， 你应该使用 argv
'''