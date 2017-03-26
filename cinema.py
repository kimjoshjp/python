#
#
#
#
#

# ages and number of seats
films ={"Finding Dory":[5,5],
       "Bourne":[18,5],
       "Tarzan":[16,5],
       "Ghost":[12,5]
      }


while True:
    choice = input("What file would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        #Check age
        if age >= films[choice][0]:
            num_seats = films[choice][1]   #Set number of seat second element

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] -1 #Reduce number of ticket from 5 (elements)

            else:
                print("Sorry we are sold out.")

        else:
            print("You are too young to see that film!")

    else:
        print("There is no such a movie")