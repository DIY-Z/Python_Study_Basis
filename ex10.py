a = "I am 6'2\" tall." # 将字符串中的双引号转义
b = 'I am 6\'2" tall.' # 将字符串中的单引号转义

print (a)
print (b)


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

#三个双引号起到转义的效果
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
x = """ 
哈哈哈
            你好
            HHH
            ddd
            """
'''
#该注释部分为print(x)的显示结果
哈哈哈
            你好
            HHH
            ddd
'''

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
print (x)

'''
# 运行下列代码，看看什么效果
while True:
    for i in ["/","-","|","\\","|"]:
        print ("%s\r" % i, end = " ")
'''


