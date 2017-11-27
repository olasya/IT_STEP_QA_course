a = [1, 33, 7, 18, 7, 9, 11, -5, 0, 12, 32]

def my_min(list_argument):
	x = list_argument[0]
	for current_number in list_argument[1:]:
		if x > current_number:
			x = current_number
	return x

rezult_2 = my_min(a)
print rezult_2
