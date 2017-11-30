# def func(a, b):
# 	summ = a + b
# 	return summ
# print func(5,7)
def func():
	winter = ["January","Fabruary","December"]
	spring = ["March","April","May"]
	summer = ["June","July","August"]
	autumn = ["September","October","November"]
	seasons = [winter, spring, summer, autumn]
   	month = raw_input("Input month:")
   	for s in seasons:
   	    if month in s:
   	    	names = seasons
 	        return s
 	    # elif month in spring:
 		   #  return spring
 	    # elif month in summer:
 		   #  return summer
 	    # elif month in autumn:
 		   #  return autumn
  	    else:
 		    return"error"
        

result = func()
print result 