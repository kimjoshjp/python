#
#
#
#
# Class

# Define Coles  Class as Parents


class Coles:
    var_1 = "apple"
    var_2 = "banana"
    var_3 = "beer"

# Define Child class of parents.


class Child(Coles):
    var_3 = "sake"

# Create Object name from class
pob = Coles()
cob = Child()

# Parents Coles. object.method
print pob.var_1
print pob.var_2
print pob.var_3

# Child Object method
print cob.var_3

