
def bread(func):
    """bread"""
    def my_bread(some_meat):
        print " /''''''''''\ "
        func(some_meat)
        print " \__________/ "
        return " "
    return my_bread

def cheese(func):
    """ cheese """
    def my_cheese(some_meat):
        print " [[[cheese]]] "
        func(some_meat)
        print " [[[cheese]]] "
    return my_cheese

def cotlet(func):
    """ cotlet """
    def my_cotlet(some_meat):
        print " ==cotlet== "
        func(some_meat)
        print " ==cotlet== "
    return my_cotlet

def tomato_salad(func):
    """ tomato and salad """
    def my_vegatable(some_meat):
        print "  _tomato_  "
        func(some_meat)

        print " ~~~salad~~~ "
    return my_vegatable

def some_meat(some_meat):
    """ some meat """    
    print some_meat 


sandvich = bread(cheese(cotlet(tomato_salad(some_meat))))

print sandvich("  --ham-- ")


