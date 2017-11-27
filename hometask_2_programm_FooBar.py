
a= int(input("Input number:"))

if a <= 0:
	print "Input positive number"
elif a % 3 == 0 and a % 5 == 0:
 	print "FooBar"
elif a % 3 == 0:
	print "Foo"
elif a % 5 == 0:
	print "Bar"
else:
 	print "GoodBy"	

