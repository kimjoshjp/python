#
#
#
#
# Sample Def

food = ['apple', 'lemon', 'banana', 'water', 'peach']

# Pick up from apple,lemon and banana only.
for a in food[:3]:
    print[a]
    print(len(a))

print food[0]  # appple
print food[4]  # peach

food.append("lime")
print food

# apple in food list , yes
if 'apple' in food:
    print "Yeah"
