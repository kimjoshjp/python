#
#
#
#
#

#name = input ("What is your name:?")
#print ("Hello {} san!".format(name))

vowels = 0
consonants = 0

for letter in "superc alifragexceptionsoccerball":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter ==" ":
        pass
    else:
        consonants = consonants + 1

print("There is {} vowels".format(vowels))
print("There is {} consonants".format(consonants))
