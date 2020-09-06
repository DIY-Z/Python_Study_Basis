#python3.x版本中输入用input(),而python2.x版本中输入用raw_input()
print ("How old are you?"),
age = input()
print ("How tall are you?"),
height = input()
print ("How much do you weigh?")
weight = input()

print ("So, you're %r old, %r tall and %r heavy." % (age,height,weight))
