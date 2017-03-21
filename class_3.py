#
#
#
#
# Practive class


class Myclass:
    var_1 = 100
    var_2 = 200

    def foo(selt):
        print("Hello from function foo")

obj_1 = Myclass() 	#Create obj_1 from Myclass
obj_2 = Myclass()	#Second obj_2

obj_1.var_1 = 400    #Change value
 
print (obj_1.var_1)		#Display 400
obj_1.foo() 
print (obj_2.var_2)		#Display 200