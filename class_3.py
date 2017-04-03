#
#
#
#
# Practive class


class Myclass:
    var_1 = 100
    var_2 = 200

    def __init__(self, name, age, home, country):
        self.name = name
        self.age = age
        self.home = home
        self.country = country

        print("Hello {0} san {1} years old and home town is {2} from {3}."
              .format(self.name, self.age, self.home, self.country ))

obj_1 = Myclass("Haru", 34, "Tokyo", "Japan") 	#Create obj_1 from Myclass
obj_2 = Myclass("Kazu", 47, "Brisbane", "Aus")	#Second obj_2

obj_1.var_1 = 400    #Change value
 
print (obj_1.var_1)		#Display 400
print (obj_2.var_2)		#Display 200