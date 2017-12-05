def season(month):
    if month in [1, 2, 12] or month in ["January", "February", "December"] :
        print "winter"
    elif month in [3, 4, 5] or month in ["March", "April", "May"]:
        print "spring"
    elif month in [6, 7, 8] or month in ["June", "July", "August"]:
        print "summer"
    elif month in [9, 10, 11] or month in ["September", "October", "November"]:
        print "autumn"
    else:
        print "Error.Input correct month "

season("June")