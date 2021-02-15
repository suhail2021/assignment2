list=[11,22,13,33,44,55]
print "orginal list:"
print list
for i in list:
	if(1%2==0):
		list.remove(i)
print"list after removeing even numbers:"
print list		