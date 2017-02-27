#
#
# Def function 
#
#


def whatsup(x):
    return 'Whats up ' + x
print whatsup('Kazu')

###
def plusten(y):
    return y+10
print plusten(320)

###

def name(first, last):
    print '%s %s' % (first, last)
name('Kazu', 'Fukushige')


###
def name_1(first='Melita', last='Smith'):
    print '%s %s' % (first, last)
name_1(first='Kate')
