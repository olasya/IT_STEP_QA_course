def reverse_tree(a):
	for number_1 in range(a):
		print ( " " * number_1) + "*" + ("*" * (a - number_1)) * 2 
reverse_tree(30)