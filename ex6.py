x = ("There are %d types of people." % 10)
binary = "binary"
do_not = "don't"
y = ("Those who know %s and those who %s." % (binary, do_not))


print (x)
print (y)


print ("I said: %r." % x)           #比较第11行与第12行，运行后观看效果发现%r会自动给那个代表的字符串加单引号
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print (joke_evaluation % hilarious) 

w = "This is the left side of..."
e = "a string with a right side."
print (w + e)