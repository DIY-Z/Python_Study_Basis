# this one is like your scripts with argv
def print_two (*args):      #*args中*告诉python把函数的所有参数组织一个列表放在 args 里。类似之前用过的 argv ， 只不过 *args 是用在函数里
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
    
# this just takes one argument
def print_one(arg1):
    print ("arg1: %r" % arg1)
    
# this one takes no arguments
def print_none():
    print ("I got nothin'.")
    
print_two("Zed", "Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# 冒号以下， 使用4个空格缩进(一个tab键解决)的行都是属于 print_two 这个函数的内容
# 这里的*args,用处和脚本的 argv 非常相似