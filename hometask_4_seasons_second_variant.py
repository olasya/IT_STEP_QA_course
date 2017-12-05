def returns_season(month):
    months = ['January', 'February', 'March','April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

    index_of_month = months.index(month) + 1
    if index_of_month in [1, 2, 12]:
        print "winter"
    elif index_of_month in [3, 4, 5]:
        print "spring"
    elif index_of_month in [6, 7, 8]:
        print "summer"
    elif index_of_month in [9, 10, 11]:
        print "autumn"
    else:
        print "Error.Input correct month "


returns_season("May")

