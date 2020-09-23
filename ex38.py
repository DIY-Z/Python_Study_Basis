ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')		#将字符串按照空格分割，放到一个列表中
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print ("Adding: ", next_one)
	stuff.append(next_one)
	print ("There are %d items now." % len(stuff))

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])		#输出列表中下标为1的那个元素
print (stuff[-1])		
print (stuff.pop())		#弹出列表中最后一个元素并把它输出
print (' '.join(stuff))	#使用空格将列表中的元素连接起来
print ('#'.join(stuff[3:5]))	#使用#符号将列表中的下标为3和下标为4的元素连接起来,和range(3,5)工作原理相近