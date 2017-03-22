#
#
#
#
import random

health = 50
difficulty = 1

portion_health = int(random.randint(20, 50) / difficulty)

health = health + portion_health

print (health)