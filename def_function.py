#
#
# Def function
#
#


def whatsup(x):
    return 'Whats up ' + x
print whatsup("Kazu")


def whatsup_2(y):
    return 'How dy ' + y
print whatsup_2('Cooky')
###

def plusten(y):
    return y+10
plusten(320)

###


def name(first, last):
    print ("%s %s") % (first, last)
name('Kazu', 'Fukushige')


###
def name_1(first='Melita', last='Smith'):
    print ("%s %s") % (first, last)
name_1(first='Kate')


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

profile_2('Kazu', 'Fukushige', 18, 23, 24, 44, 55, lime=10, banna=10)
