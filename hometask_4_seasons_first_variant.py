def func():
	winter = ["January","Fabruary","December"]
	spring = ["March","April","May"]
	summer = ["June","July","August"]
	autumn = ["September","October","November"]
	seasons = ["winter", "spring", "summer", "autumn"]
   	month = raw_input("Input month:")
   	for s in seasons:
   	    if month in winter:
   	    	return "winter"
 	    elif month in spring:
 		    return "spring"
 	    elif month in summer:
 		    return "summer"
 	    elif month in autumn:
 		    return "autumn"
  	    else:
 		    return"Error : Input correct month"
        

result = func()
print result 
	