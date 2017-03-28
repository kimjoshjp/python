#
#
#
#
#
name = input("What is your name?: ")
age = input("How old are you?: ")
city = input("Where are you from?: ")
like = input("What would you like to do?: ")


string = "Your name is {} and you are {} years old. You live in {} and you like {}."
output = string.format(name,age,city,like)
print (output)