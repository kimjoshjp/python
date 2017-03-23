#
#
#
#
#
member = {'Josh':18,
       'Matt':23,
       'Alex':13,
       'Kim':40,
       'Kazu':47,
       #'Dick':55,
}

aaa = member.get('Dick', 'Unknown') # If Dick is not listed in member lists then display Unknown
print ("Dick is %s years old" % aaa)