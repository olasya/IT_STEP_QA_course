def tree(a):
	# a = 30
	for number in range(a):
		print ( " " * (a - number)) + "*"  + ( "*" * number) * 2
def reverse_tree(a):
	for number_1 in range(a):
		print ( " " * number_1) + ("*" * (a - number_1)) * 2
tree(30)
reverse_tree(30)