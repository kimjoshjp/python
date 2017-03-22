##
#
#
# Condition

yourAge = int(input("How old are you:"))

if (yourAge > 0) and (yourAge < 120):
    if (yourAge == 47):
        print ("Same as me")
    elif (yourAge > 47):
        print ("Older that me")
    else:
        print ("Younger than me")

else:
    print ("Don't lie about your age")
