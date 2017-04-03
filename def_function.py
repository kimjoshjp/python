#
#
# Def function
#
#


def whatsup(x):
    return 'Whats up ' + x
print (whatsup('Kazu'))   #What's up Kazu


def plusten(y):
    return y+10
print (plusten(320))  #answer is 330


def list(*food):
    print ("food")
list('apple', 'lemon', 'banana')

##


def profile(name, *ages):
    print ("name")
    print ("ages")

profile('Kazu', 18, 22, 33, 47)

##


def profile_2(first, last, *ages, **items):
    print ("first", "last")
    print ("ages")
    print ("items")

print (profile_2('Kazu', 'Fukushige', 18, 23, 24, 44, 55, lime=10, banna=10))
