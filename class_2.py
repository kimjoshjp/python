#
#
#
#
#   Multiple Parent Class
#################################
class Dad:
    dad_1 = "This is Dad."
    dad_2 = "40"


class Mon:
    mon_1 = "This is Mon."
    mon_2 = "35"


class Kids(Dad, Mon):
    kids_1 = "This is Me"

 # Create happy_obj (object) from Kids Class
happy_obj = Kids()


# Create method
print (happy_obj.dad_1)
print (happy_obj.mon_2)
print (happy_obj.kids_1)

#################################


class new:

    """ new class """

    def __init__(self):
        print ("This is constructor")
        print ("This also print out.")

obj = new()

####