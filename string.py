# git ip
#
#
#
# String practice

name = "Joshua"
print("Hello, PyCharm my name is %s! " % name)

years = 19
print("I am %d years old " % years)


# lower, Upper case
monty_python = "Monty Python"
print(monty_python)
print(monty_python.lower())
print(monty_python.upper())

# String index
name = "Kazunori"
print("u is " + name[3])

p_letter = name[0]
print(p_letter)

# Negative index
long_string = "This is a very long string!"
exclamation = long_string[-1]
print(exclamation)

# String slice
last_name = "Fukushige Kazunori"
fuku = last_name[:9]
print(fuku)

first_name = last_name[10:]
print(first_name)

### list
list_01 = ["z","a","c","g","j"]
print(list_01)
list_01[2] = "C"   #update c->C
print(list_01)
print sorted(list_01)   #sorting
list_01.append('h')     #append h on last
print list_01
list_01.insert(1,'b')   #insert b at 'i' index
print list_01
print len(list_01)