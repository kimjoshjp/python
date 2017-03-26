#
#
#
#
# Travis game / Remove name and Register

known_user = ["Alex","Bob","Claire","Don","Erick","Fred","Georgia","Harry"]
user_number = len(known_user) # number of users

while True:
    print ("Hello My name is Travis.")
    print("We have a %s users in system." % user_number)
    name = input("What is your name?: ").strip().capitalize() #Accept lower case

    if name in known_user:
        print ("Hello {}! We recognized your user name. \n".format(name) ) #Display known_user name
        remove = input ("Would you like to be removed from the system (y/n)?:  ").lower()
        if remove == "y":
            known_user.remove(name)   #Remove name from lists
            print(known_user)

    else:
        print("Sorry. %s Name Not recognize your name. \n" %name)  #Display name value
        add_me = input("Shall I register your name in system (y/n)?:").lower()
        if add_me == "y":
            known_user.append(name)   #Add name in lists.
            print (known_user)

        elif add_me == "n":
            print("See you again")


