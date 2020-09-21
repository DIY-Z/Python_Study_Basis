the_count = [1,2,3,4,5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print ("This is count %d" % number)

# same as above
for fruit in fruits:
	print ("A fruit of type: %s" % fruit)

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print ("I got %r" % i)

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):		#其中range()函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
	# range(0,6)表示从0开始,末尾是6,不包括6
	print ("Adding %d to the list." % i)
	# append is a function that lists understand
	elements.append(i)		#append() 方法用于在列表末尾添加新的对象。

# now we can print them out too
for i in elements:
	print ("Element was: %d" % i)
