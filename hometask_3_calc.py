def addition(a,b):
	return float(a) + float(b)
result = addition(5,9)
print (result)

def substraction(a,b):
	return float(a) - float(b)
result_1 = substraction(5,9)
print (result_1)

def multiplication(a,b):
	return float(a) * float(b)
result_2 = multiplication(0,9)
print (result_2)

def division(a,b):
	return float(a) / float(b)
result_3 = division(5,8)
print (result_3)


def addition_all(*args):
	return sum(args)
result_4 = addition_all(1,3,6)
print (result_4)

def substraction_all(first_element,*args):
    rezult = first_element
    for a in args:
       rezult = rezult - a
    return rezult
rezult_5 = substraction_all(10,9,5,2)
print (rezult_5) 

def multiplication_all(first_element,*args):
	rezult_1 = first_element
	for a in args:
		rezult_1 = rezult_1 * a
	return rezult_1
result_6 = multiplication_all(0,2,3)
print (result_6)
