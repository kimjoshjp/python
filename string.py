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
name = "Fukushige Kazunori"
fuku = name[:9]
print(fuku)

last = name[10:]
print(last)

# String length
phrase = """
It is a really long string triple-quoted strings are used  to define multi-line strings
"""

first_half = phrase[0:len(
    phrase)/2]
print(first_half)

print('It\'s me')            # need \ with sigle quotation
print("She said \"Hello\"")  # need \ with double quotation
