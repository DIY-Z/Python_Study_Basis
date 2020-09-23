states = {
	'Oregon': 'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
}

cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print ("-" * 10)		#乘以10后可以连续输出10个-
print ("NY State has: ", cities['NY'])
print ("OR State has: ", cities['OR'])

print ("-" * 10)
print ("Michigan's abbreviation is: ", states['Michigan'])
print ("Florida's abbreviation is: ", states['Florida'])

print ("-" * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Florida']])

print ('-' * 10)
for state,abbrev in cities.items():	 #dict.items()可以列表形式返回可遍历的(键,值)元组数组
	print ("%s is abbreviated %s" % (state, abbrev))

print ("-" * 10)
for state, abbrev in states.items():
	print ("%s state is abbreviated %s and has city %s" % (state,abbrev,cities[abbrev]))

print ("-" * 10)
state = states.get('Texas')		#dic.get(key),返回指定键的值,如果没有,则返回None

if not state:			#类似C语言中的非!
	print ("Sorry, no Texas")

city = cities.get('TX', 'Does Not Exist')		#dic.get(key,default=None),返回指定键的值，若没有则返回第二个参数，若没有第二个参数，则返回None
print ("The city for the state 'TX' is: %s" % city)